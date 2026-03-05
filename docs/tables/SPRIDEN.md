---
tags:

---

# SPRIDEN

Person Identification/Name Repeating Table


## Schema

| Column | Type | Description |
| --- | --- | --- |
| `SPRIDEN_PIDM` | `NUMBER(8,0)` | Internal identification number of the person. |
| `SPRIDEN_ID` | `VARCHAR2(9 CHAR)` | This field defines the identification number used to access person on-line. |
| `SPRIDEN_LAST_NAME` | `VARCHAR2(60 CHAR)` | This field defines the last name of person. |
| `SPRIDEN_FIRST_NAME` | `VARCHAR2(60 CHAR)` | This field identifies the first name of person. |
| `SPRIDEN_MI` | `VARCHAR2(60 CHAR)` | This field identifies the middle name of person. |
| `SPRIDEN_CHANGE_IND` | `VARCHAR2(1 CHAR)` | This field identifies whether type of change made to the record was an ID number change or a name change. Valid values: I - ID change, N - name change. |
| `SPRIDEN_ENTITY_IND` | `VARCHAR2(1 CHAR)` | This field identifies whether record is person or non-person record. It does not display on the form. Valid values: P - person, C - non-person. |
| `SPRIDEN_ACTIVITY_DATE` | `DATE` | This field defines the most current date record is created or changed. |
| `SPRIDEN_USER` | `VARCHAR2(30 CHAR)` | USER: The ID for the user that most recently updated the record. |
| `SPRIDEN_ORIGIN` | `VARCHAR2(30 CHAR)` | ORIGIN: The name of the Banner Object that was used most recently to update the row in the spriden table. |
| `SPRIDEN_SEARCH_LAST_NAME` | `VARCHAR2(60 CHAR)` | The Last Name field with all spaces and punctuation removed and all letters capitalized. |
| `SPRIDEN_SEARCH_FIRST_NAME` | `VARCHAR2(60 CHAR)` | The First Name field with all spaces and punctuation removed and all letters capitalized. |
| `SPRIDEN_SEARCH_MI` | `VARCHAR2(60 CHAR)` | The MI (Middle Initial) field with all spaces and punctuation removed and all letters capitalized. |
| `SPRIDEN_SOUNDEX_LAST_NAME` | `CHAR(4 CHAR)` | The Last Name field in SOUNDEX phonetic format. |
| `SPRIDEN_SOUNDEX_FIRST_NAME` | `CHAR(4 CHAR)` | The First Name field in SOUNDEX phonetic format. |
| `SPRIDEN_NTYP_CODE` | `VARCHAR2(4 CHAR)` | NAME TYPE CODE: The field is used to store the code that represents the name type associated with a person's name. |
| `SPRIDEN_CREATE_USER` | `VARCHAR2(30 CHAR)` | Record Create User: This field contains Banner User ID which created new record |
| `SPRIDEN_CREATE_DATE` | `DATE` | Record Create Date: This field contains date new record created |
| `SPRIDEN_DATA_ORIGIN` | `VARCHAR2(30 CHAR)` | DATA SOURCE: Source system that generated the data |
| `SPRIDEN_CREATE_FDMN_CODE` | `VARCHAR2(30 CHAR)` | PII DOMAIN: PII Domain of the user who created the spriden row. |
| `SPRIDEN_SURNAME_PREFIX` | `VARCHAR2(60 CHAR)` | SURNAME PREFIX: Name tag preceding the last name or surname. (Van, Von, Mac, etc.) |
| `SPRIDEN_SURROGATE_ID` | `NUMBER(19,0)` | SURROGATE ID: Immutable unique key |
| `SPRIDEN_VERSION` | `NUMBER(19,0)` | VERSION: Optimistic lock token. |
| `SPRIDEN_USER_ID` | `VARCHAR2(30 CHAR)` | USER ID: The user ID of the person who inserted or last updated this record. |
| `SPRIDEN_VPDI_CODE` | `VARCHAR2(6 CHAR)` | VPDI CODE: Multi-entity processing code. |


## Queries
- - -

### Find Name by ID

Find a person's name by their ID.

```sql title="find_name.sql"
--8<-- "table-definitions/SPRIDEN/sql/find_name.sql"
```
