---
tags:

---

# STVTERM

Term Code Validation Table


## Schema

| Column | Type | Description |
| --- | --- | --- |
| `STVTERM_DESC` | `VARCHAR2(30 CHAR)` | This field specifies the term associated with the term code. The term is identified by the academic year and term number and is formatted YYYYTT. |
| `STVTERM_START_DATE` | `DATE` | This field identifies the term start date and is formatted DD-MON-YY. |
| `STVTERM_END_DATE` | `DATE` | This field identifies the term end date and is fomatted DD-MON-YY. |
| `STVTERM_FA_PROC_YR` | `VARCHAR2(4 CHAR)` | This field identifies the financial aid processing start and end years (e.g. The financial aid processing year 1988 - 1989 is formatted 8889.). |
| `STVTERM_ACTIVITY_DATE` | `DATE` | This field identifies the most recent date a record was created or updated. |
| `STVTERM_FA_TERM` | `VARCHAR2(1 CHAR)` | This field identifies the financial aid award term. |
| `STVTERM_FA_PERIOD` | `NUMBER(2,0)` | This field identifies the financial aid award beginning period. |
| `STVTERM_FA_END_PERIOD` | `NUMBER(2,0)` | This field identifies the financial aid award ending period. |
| `STVTERM_ACYR_CODE` | `VARCHAR2(4 CHAR)` | This field is not currently in use. |
| `STVTERM_HOUSING_START_DATE` | `DATE` | Housing Start Date. |
| `STVTERM_HOUSING_END_DATE` | `DATE` | Housing End Date. |
| `STVTERM_SYSTEM_REQ_IND` | `VARCHAR2(1 CHAR)` | System Required Indicator |
| `STVTERM_TRMT_CODE` | `VARCHAR2(1 CHAR)` | Term type for this term. Will default from SHBCGPA_TRMT_CODE. |
| `STVTERM_FA_SUMMER_IND` | `VARCHAR2(1 CHAR)` | SUMMER INDICATOR: Indicates a summer term to financial aid. |
| `STVTERM_SURROGATE_ID` | `NUMBER(19,0)` | SURROGATE ID: Immutable unique key |
| `STVTERM_VERSION` | `NUMBER(19,0)` | VERSION: Optimistic lock token. |
| `STVTERM_USER_ID` | `VARCHAR2(30 CHAR)` | USER ID: The user ID of the person who inserted or last updated this record. |
| `STVTERM_DATA_ORIGIN` | `VARCHAR2(30 CHAR)` | DATA ORIGIN: Source system that created or updated the data. |
| `STVTERM_VPDI_CODE` | `VARCHAR2(6 CHAR)` | VPDI CODE: Multi-entity processing code. |
| `STVTERM_GUID` | `VARCHAR2(36 BYTE)` | GUID: Global Unique Identifier to uniquely identify the record of a resource for integration. |
| `STVTERM_APPORT_CDE` | `VARCHAR2(1 BYTE)` | APPORTIONMENT CATEGORY: Valid values are (null) = the same as "N", "N" = not reported (skipped on apportionment reports), "1" = first primary term, "2" = second primary term, "3" = third primary term, "I" = intersession term. |
| `STVTERM_MIS_TERM_CTG` | `VARCHAR2(1 BYTE)` | MIS TERM CATALOG: Obsolete; will be dropped from the table at a future date. |
| `STVTERM_MIS_TERM_ID` | `VARCHAR2(3 BYTE)` | MIS TERM INDICATOR: 3-character; user-entered; the field is mandatory when adding new terms or updating existing terms (This entry is used in the majority of the MIS Reports as field GI03 TERM-IDENTIFIER). |
| `STVTERM_TERM_LEN_MULT` | `NUMBER(5,2)` | TERM LENGTH MULTIPLIER: Optional, but required if STVTERM_APPORT_CDE not in ("N",null); 999.99 valid values. |
| `STVTERM_TERM_LEN_MULT_IS` | `NUMBER(5,2)` | TERM LENGTH MULTIPLIER IS: Independent study term length multiplier for apportionment reporting and calculation of FTES. |
| `STVTERM_CATALOG_GUID` | `VARCHAR2(36 BYTE)` | CATALOG GUID: Global Unique Identifier to uniquely identify the record of a resource for integration. |


## Queries
- - -

*No queries documented yet.*
