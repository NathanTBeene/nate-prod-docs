---
tags:

---

# SFRSTCR

Student Course Registration Repeating Table


## Schema

| Column | Type | Description |
| --- | --- | --- |
| `SFRSTCR_CRN` | `VARCHAR2(5 CHAR)` | This field identifies the course reference number associated with the class section. |
| `SFRSTCR_PIDM` | `NUMBER(8,0)` | Internal Identification Number of the person registered. |
| `SFRSTCR_TERM_CODE` | `VARCHAR2(6 CHAR)` | This field identifies the registration term code. |
| `SFRSTCR_CLASS_SORT_KEY` | `NUMBER(4,0)` | This field identifies the class of the registrant. |
| `SFRSTCR_REG_SEQ` | `NUMBER(4,0)` | This field identifies the sequence in which the student enrolled in the associated class section. |
| `SFRSTCR_PTRM_CODE` | `VARCHAR2(3 CHAR)` | This field identifies the part-of-term code associated with this CRN. |
| `SFRSTCR_RSTS_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the course registration status associated with this CRN. |
| `SFRSTCR_RSTS_DATE` | `DATE` | This field identifies the date associated with the course registration status of this CRN. |
| `SFRSTCR_ERROR_FLAG` | `VARCHAR2(1 CHAR)` | This field identifies an error associated with the registration of this CRN. Valid values are F=Fatal, D=Do not count in enrollment, L=WaitListed, O=Override, W=Warning, X=Delete (used only by SFRSTCR POSTUPDATE DB trigger). |
| `SFRSTCR_MESSAGE` | `VARCHAR2(200 CHAR)` | This field identifies a message associated with the registration of the CRN |
| `SFRSTCR_BILL_HR` | `NUMBER(7,3)` | This field identifies the billing hours associated with this CRN. |
| `SFRSTCR_WAIV_HR` | `NUMBER(7,3)` | This field identifies the waived hours associated with this CRN. |
| `SFRSTCR_CREDIT_HR` | `NUMBER(7,3)` | This field identifies the credit hours associated with this CRN. |
| `SFRSTCR_BILL_HR_HOLD` | `NUMBER(7,3)` | This field identifies the billing hours to hold for reinstatements. |
| `SFRSTCR_CREDIT_HR_HOLD` | `NUMBER(7,3)` | This field identifies the credit hours to hold for reinstatements. |
| `SFRSTCR_GMOD_CODE` | `VARCHAR2(1 CHAR)` | This field identifies the grade mode associated with this CRN. |
| `SFRSTCR_GRDE_CODE` | `VARCHAR2(6 CHAR)` | This field identifies the grade code associated with this CRN. |
| `SFRSTCR_GRDE_CODE_MID` | `VARCHAR2(6 CHAR)` | This field identifies the mid-term grade code associated with this CRN. |
| `SFRSTCR_GRDE_DATE` | `DATE` | This field identifies the date associated with the grade of this CRN. |
| `SFRSTCR_DUPL_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the duplicate course override of this CRN. |
| `SFRSTCR_LINK_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the link override of this CRN. |
| `SFRSTCR_CORQ_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the corequisite override of this CRN. |
| `SFRSTCR_PREQ_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the prerequisite override of this CRN. |
| `SFRSTCR_TIME_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the time conflict override of this CRN. |
| `SFRSTCR_CAPC_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the capacity override of this CRN. |
| `SFRSTCR_LEVL_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the level restriction override of this CRN. |
| `SFRSTCR_COLL_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the college restriction override of this CRN. |
| `SFRSTCR_MAJR_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the major restriction override of this CRN. |
| `SFRSTCR_CLAS_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the class restriction override of this CRN. |
| `SFRSTCR_APPR_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the special approval override of this CRN. |
| `SFRSTCR_APPR_RECEIVED_IND` | `VARCHAR2(1 CHAR)` | This field identifies the special approval received indicator for this CRN. |
| `SFRSTCR_ADD_DATE` | `DATE` | This field identifies the add date of the registrant in this CRN. |
| `SFRSTCR_ACTIVITY_DATE` | `DATE` | This field identifies the most current date record was created or updated. |
| `SFRSTCR_LEVL_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the level the registrant is enrolled for this CRN. |
| `SFRSTCR_CAMP_CODE` | `VARCHAR2(3 CHAR)` | This field identifies the campus code of this CRN. |
| `SFRSTCR_RESERVED_KEY` | `VARCHAR2(82 CHAR)` | Student Course Registration Table Reserved Key. |
| `SFRSTCR_ATTEND_HR` | `NUMBER(9,3)` | This column contains the number of hours the student attended this class |
| `SFRSTCR_REPT_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the repeat course restriction override of the CRN |
| `SFRSTCR_RPTH_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the repeat course hour restriction override of the CRN |
| `SFRSTCR_TEST_OVER` | `VARCHAR2(1 CHAR)` | This field identifies the test score restriction override of the CRN |
| `SFRSTCR_CAMP_OVER` | `VARCHAR2(1 CHAR)` | The Campus Registration Restriction override code |
| `SFRSTCR_USER` | `VARCHAR2(30 CHAR)` | Identifies the user who entered the registration request. |
| `SFRSTCR_DEGC_OVER` | `VARCHAR2(1 CHAR)` | Degree restriction override indicator |
| `SFRSTCR_PROG_OVER` | `VARCHAR2(1 CHAR)` | Program restriction override indicator |
| `SFRSTCR_LAST_ATTEND` | `DATE` | Date student last attended this class |
| `SFRSTCR_GCMT_CODE` | `VARCHAR2(7 CHAR)` | GRADE COMMENT CODE: This field indicates the grade comment (result code) for the section. |
| `SFRSTCR_DATA_ORIGIN` | `VARCHAR2(30 CHAR)` | DATA SOURCE: Source system that created or updated the row |
| `SFRSTCR_ASSESS_ACTIVITY_DATE` | `DATE` | This field identifies the date when registration activity impacting Fee Assessment occurred. This date is used in flat charge refunding to determine courses that have been updated since the student's last assessment. |
| `SFRSTCR_DEPT_OVER` | `VARCHAR2(1 CHAR)` | DEPARTMENT OVERRIDE: This field identifies the department restriction override of this CRN. |
| `SFRSTCR_ATTS_OVER` | `VARCHAR2(1 CHAR)` | STUDENT ATTRIBUTE OVERRIDE: This field identifies the student attribute restriction override of this CRN. |
| `SFRSTCR_CHRT_OVER` | `VARCHAR2(1 CHAR)` | COHORT OVERRIDE: This field identifies the cohort restriction override of this CRN. |
| `SFRSTCR_RMSG_CDE` | `VARCHAR2(4 CHAR)` | MESSAGE CODE: Specifies the type of error message. |
| `SFRSTCR_WL_PRIORITY` | `NUMBER(11,6)` | WAITLIST PRIORITY: The Waitlist priority. |
| `SFRSTCR_WL_PRIORITY_ORIG` | `VARCHAR2(1 CHAR)` | PRIORITY ORIGIN: Waitlist priority origin. Valid values are S-system originated, M-manually originated. |
| `SFRSTCR_GRDE_CODE_INCMP_FINAL` | `VARCHAR2(6 CHAR)` | INCOMPLETE FINAL DEFAULT GRADE CODE: Grade code to identify default final grade for incomplete coursework. |
| `SFRSTCR_INCOMPLETE_EXT_DATE` | `DATE` | INCOMPLETE DEFAULT EXTENSION DATE: Date to identify when the default final grade will be applied to academic history if coursework is incomplete. |
| `SFRSTCR_MEXC_OVER` | `VARCHAR2(1 CHAR)` | MUTUAL EXCLUSION OVERRIDE: This field identifies the mutual exclusion restriction override of this CRN |
| `SFRSTCR_STSP_KEY_SEQUENCE` | `NUMBER(2,0)` | STUDY PATH SEQUENCE: Key sequence of the study path under which the CRN is registered. |
| `SFRSTCR_BRDH_SEQ_NUM` | `NUMBER(7,0)` | BLOCK RULE SEQUENCE NUMBER: Sequence number that uniquely identifies the rule for block assignment. |
| `SFRSTCR_BLCK_CODE` | `VARCHAR2(10 CHAR)` | BLOCK: Block code student is registered. |
| `SFRSTCR_SURROGATE_ID` | `NUMBER(19,0)` | SURROGATE ID: Immutable unique key |
| `SFRSTCR_VERSION` | `NUMBER(19,0)` | VERSION: Optimistic lock token. |
| `SFRSTCR_USER_ID` | `VARCHAR2(30 CHAR)` | USER ID: The user ID of the person who inserted or last updated this record. |
| `SFRSTCR_VPDI_CODE` | `VARCHAR2(6 CHAR)` | VPDI CODE: Multi-entity processing code. |
| `SFRSTCR_STRH_SEQNO` | `NUMBER(8,0)` | STRUCTURED REGISTRATION HEADER SEQUENCE NUMBER: The Unique Id of the Structured Registration Header Record which contains type of requirement and program. |
| `SFRSTCR_STRD_SEQNO` | `NUMBER(8,0)` | STRUCTURED REGISTRATION SEQUENCE NUMBER: The Unique Id within the Structured Registration Program and Requirement for the requirement detail. |
| `SFRSTCR_SESSIONID` | `VARCHAR2(30 CHAR)` | SESSIONID: The session id value for the registration. |
| `SFRSTCR_CURRENT_TIME` | `TIMESTAMP(9)` | CURRENT TIME: The current time of the registration. |


## Queries
- - -

### Student Classes By Term

Get each student enrolled for the term and all of their valid classes.

```sql title="student_classes_by_term.sql"
--8<-- "table-definitions/SFRSTCR/sql/student_classes_by_term.sql"
```

### Student Hours By Term

Get each student enrolled for the term and their total hours enrolled.

```sql title="student_hours_by_term.sql"
--8<-- "table-definitions/SFRSTCR/sql/student_hours_by_term.sql"
```
