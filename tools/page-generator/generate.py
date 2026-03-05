#!/usr/bin/env python3
"""Generate MkDocs pages from table definition folders."""

import json
import re
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT = SCRIPT_DIR.parent.parent
DEFS_DIR = ROOT / "table-definitions"
DOCS_DIR = ROOT / "docs"
TABLES_DIR = DOCS_DIR / "tables"
SQL_DIR = DOCS_DIR / "sql"
MKDOCS_YML = ROOT / "mkdocs.yml"
INDEX_MD = DOCS_DIR / "index.md"
DATA_INDEX = DOCS_DIR / "data-tables.md"
DEF_INDEX = DOCS_DIR / "definition-tables.md"


def read_definitions_file(file_path: Path, headers: list[str] | None = None) -> str | None:
    """Read a .dat file and return it as a markdown table."""
    if not file_path.exists():
        return None

    text = file_path.read_text(encoding="utf-8")
    rows = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if "\t" in line:
            parts = line.split("\t", 1)
        else:
            parts = re.split(r"\s{2,}", line, maxsplit=1)

        while len(parts) < 2:
            parts.append("")

        rows.append([p.strip() for p in parts])

    if not rows:
        return None

    if not headers:
        headers = ["Code", "Description"]

    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    data_rows = []
    for row in rows:
        data_rows.append("| " + " | ".join(row) + " |")

    return header_row + "\n" + separator + "\n" + "\n".join(data_rows)


def generate_table_page(table: dict, table_dir: Path) -> str:
    tags_yaml = "\n".join(f"  - {t}" for t in table["tags"])
    table_type = table.get("type", "data")
    table_name = table["name"]

    # Check if any column has a non-empty definition table link
    has_definitions = any(
        col.get("definition_table", "").strip()
        for col in table["columns"]
    )

    # Schema table
    if has_definitions:
        header = "| Column | Type | Description | Definition |\n| --- | --- | --- | --- |"
    else:
        header = "| Column | Type | Description |\n| --- | --- | --- |"

    col_rows = []
    for col in table["columns"]:
        desc = col.get("description", "")
        if has_definitions:
            def_table = col.get("definition_table", "").strip()
            if def_table:
                def_link = f"[{def_table}]({def_table}.md)"
            else:
                def_link = ""
            col_rows.append(f"| `{col['name']}` | `{col['type']}` | {desc} | {def_link} |")
        else:
            col_rows.append(f"| `{col['name']}` | `{col['type']}` | {desc} |")

    schema_table = header + "\n" + "\n".join(col_rows)

    # Type badge
    if table_type == "definition":
        type_badge = "!!! abstract \"Definition Table\"\n    This is a validation/lookup table that defines valid codes for other tables.\n"
    else:
        type_badge = ""

    # Definitions section - auto-detect .dat file
    definitions_section = ""
    if table_type == "definition":
        dat_path = table_dir / f"{table_name}.dat"
        headers = table.get("definitions_headers")
        md_table = read_definitions_file(dat_path, headers)
        if md_table:
            definitions_section = f"## Values\n\n{md_table}\n"
        else:
            definitions_section = "## Values\n\n*No values loaded. Add a .dat file to populate this section.*\n"

    # Queries section
    queries_section = ""
    for q in table.get("queries", []):
        queries_section += f"\n### {q['name']}\n\n"
        queries_section += f"{q.get('description', '')}\n\n"
        queries_section += f'```sql title="{q["file"]}"\n'
        queries_section += f'--8<-- "table-definitions/{table_name}/sql/{q["file"]}"\n'
        queries_section += "```\n"

    if not table.get("queries"):
        queries_section = "\n*No queries documented yet.*\n"

    # Build search index content - column names and descriptions
    search_terms = []
    for col in table["columns"]:
        search_terms.append(col["name"])
        if col.get("description"):
            search_terms.append(col["description"])
    search_block = " ".join(search_terms)

    md = f"""---
tags:
{tags_yaml}
hide:
  - toc
---

# {table_name}

<div style="display:none">{search_block}</div>

{table['description']}

{type_badge}
## Schema

{schema_table}

{definitions_section}
## Queries
{queries_section}"""

    return md


def build_cards(table_list: list[dict]) -> str:
    cards = []
    for t in table_list:
        tags = " ".join(f"`{tag}`" for tag in t["tags"]) if t["tags"] else "*untagged*"
        cards.append(f"""-   **{t['name']}**

    ---

    {t['description']}

    **Tags:** {tags}

    [:octicons-arrow-right-24: View table](tables/{t['name']}.md)""")
    return "\n\n".join(cards)


def generate_index(data_count: int, def_count: int) -> str:
    return f"""---
hide:
  - navigation
  - toc
---

# Banner Table Dictionary

Search for tables, schemas, and queries using the search bar above, or browse by category.

---

<div class="grid cards" markdown>

-   :material-database:{{ .lg .middle }} **Data Tables**

    ---

    {data_count} tables containing application and business data.

    [:octicons-arrow-right-24: Browse data tables](data-tables.md)

-   :material-book-open-variant:{{ .lg .middle }} **Definition Tables**

    ---

    {def_count} validation and lookup tables that define valid codes.

    [:octicons-arrow-right-24: Browse definition tables](definition-tables.md)

</div>
"""


def generate_type_index(tables: list[dict], title: str, description: str) -> str:
    return f"""---
hide:
  - navigation
  - toc
---

# {title}

{description}

---

<div class="grid cards" markdown>

{build_cards(tables)}

</div>
"""


def update_nav():
    """Rewrite nav to static structure - individual tables accessed via search and cards."""
    text = MKDOCS_YML.read_text()

    new_nav = """nav:
  - Home: index.md
  - Data Tables: data-tables.md
  - Definition Tables: definition-tables.md
  - Tags: tags.md
"""

    text = re.sub(
        r"nav:\n(  - .*\n)+",
        new_nav,
        text
    )

    MKDOCS_YML.write_text(text)


def main():
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    SQL_DIR.mkdir(parents=True, exist_ok=True)

    # Each subfolder in table-definitions/ is a table
    table_dirs = sorted(
        d for d in DEFS_DIR.iterdir() if d.is_dir()
    )

    if not table_dirs:
        print(f"No table folders found in {DEFS_DIR}")
        return

    tables = []
    for table_dir in table_dirs:
        json_files = list(table_dir.glob("*.json"))
        if not json_files:
            print(f"  WARNING: No JSON file in {table_dir.name}/, skipping")
            continue

        table = json.loads(json_files[0].read_text())
        tables.append(table)

        # Generate markdown page
        out_path = TABLES_DIR / f"{table['name']}.md"
        out_path.write_text(generate_table_page(table, table_dir))
        print(f"  Generated {out_path.relative_to(ROOT)}")

    # Split by type
    data_tables = [t for t in tables if t.get("type", "data") == "data"]
    def_tables = [t for t in tables if t.get("type") == "definition"]

    # Generate index pages
    INDEX_MD.write_text(generate_index(len(data_tables), len(def_tables)))
    print(f"  Updated {INDEX_MD.relative_to(ROOT)}")

    DATA_INDEX.write_text(generate_type_index(
        data_tables,
        "Data Tables",
        "Application and business data tables."
    ))
    print(f"  Updated {DATA_INDEX.relative_to(ROOT)}")

    DEF_INDEX.write_text(generate_type_index(
        def_tables,
        "Definition Tables",
        "Validation and lookup tables that define valid codes used across the system."
    ))
    print(f"  Updated {DEF_INDEX.relative_to(ROOT)}")

    update_nav()
    print(f"  Updated {MKDOCS_YML.relative_to(ROOT)}")

    print(f"\nGenerated {len(tables)} table page(s) ({len(data_tables)} data, {len(def_tables)} definition)")


if __name__ == "__main__":
    main()
