---
tags:

---

# SGBSTDN

Student Base Table


## Schema

| Column | Type | Description | Definition |
| --- | --- | --- | --- |
| `SGBSTDN_STST_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the students status for the effective term. |  |
| `SGBSTDN_LEVL_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the level of the student for the effective term. |  |
| `SGBSTDN_STYP_CODE` | `VARCHAR2(1 CHAR)` | This field identifies the student type for the effective term. |  |
| `SGBSTDN_TERM_CODE_MATRIC` | `VARCHAR2(6 CHAR)` | This field identifies the effective term of matriculation. |  |
| `SGBSTDN_TERM_CODE_ADMIT` | `VARCHAR2(6 CHAR)` | This field identifies the term student was first admitted to institution. |  |
| `SGBSTDN_EXP_GRAD_DATE` | `DATE` | This field identifies expected graduation date. |  |
| `SGBSTDN_CAMP_CODE` | `VARCHAR2(3 CHAR)` | This field identifies the campus location associated with the student for the effective term. |  |
| `SGBSTDN_FULL_PART_IND` | `VARCHAR2(1 CHAR)` | This field identifies whether the student is a full or part-time student. |  |
| `SGBSTDN_SESS_CODE` | `VARCHAR2(1 CHAR)` | This field identifies the session student is attending for the effective term. |  |
| `SGBSTDN_RESD_CODE` | `VARCHAR2(1 CHAR)` | This field identifies the residency status of the student for the effective term. |  |
| `SGBSTDN_COLL_CODE_1` | `VARCHAR2(2 CHAR)` | This field identifies the college associated with the primary curriculum for the effective term.. |  |
| `SGBSTDN_DEGC_CODE_1` | `VARCHAR2(6 CHAR)` | This field identifies the degree within the primary curriculum for the effective term. | [STVDEGC](STVDEGC.md) |
| `SGBSTDN_MAJR_CODE_1` | `VARCHAR2(4 CHAR)` | This field identifies the primary major within the primary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_MINR_1` | `VARCHAR2(4 CHAR)` | This field identifies the primary minor within the primary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_MINR_1_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary minor of the student for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_1` | `VARCHAR2(4 CHAR)` | This field identifies the primary concentration within the primary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_1_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary concentration within the primary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_1_3` | `VARCHAR2(4 CHAR)` | This field identifies the third concentration within the primary curriculum for the effective term. |  |
| `SGBSTDN_COLL_CODE_2` | `VARCHAR2(2 CHAR)` | This field identifies the college within the secondary curriculum for the effective term. |  |
| `SGBSTDN_DEGC_CODE_2` | `VARCHAR2(6 CHAR)` | This field identifies the degree within the secondary curriculum for the effective term. | [STVDEGC](STVDEGC.md) |
| `SGBSTDN_MAJR_CODE_2` | `VARCHAR2(4 CHAR)` | This field identifies the primary major within the secondary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_MINR_2` | `VARCHAR2(4 CHAR)` | This field identifies the primary minor within the secondary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_MINR_2_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary minor within the secondary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_2` | `VARCHAR2(4 CHAR)` | This field identifies the primary concentration within the secondary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_2_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary concentration within the secondary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_CONC_2_3` | `VARCHAR2(4 CHAR)` | This field identifies the third concentration within the secondary curriculum for the effective term. |  |
| `SGBSTDN_ORSN_CODE` | `VARCHAR2(1 CHAR)` | This field identifies the orientation session assigned to the student for the effective term. |  |
| `SGBSTDN_PRAC_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the practical training experience of the student for the effective term. |  |
| `SGBSTDN_ADVR_PIDM` | `NUMBER(8,0)` | This field identifies the internal identification number for the advisor assigned to the student for the effective term. |  |
| `SGBSTDN_GRAD_CREDIT_APPR_IND` | `VARCHAR2(1 CHAR)` | This field identifies eligibility of student to take graduate courses for credit for the effective term. Valid values are Y or blank only. |  |
| `SGBSTDN_CAPL_CODE` | `VARCHAR2(2 CHAR)` | This field identifies career plan of the student for the effective term. |  |
| `SGBSTDN_LEAV_CODE` | `VARCHAR2(1 CHAR)` | This field identifies reason of leave of absence of student for the effective term. |  |
| `SGBSTDN_LEAV_FROM_DATE` | `DATE` | This field identifies the begin date of leave of absence of student for the effective term. |  |
| `SGBSTDN_LEAV_TO_DATE` | `DATE` | This field identifies the end date of leave of absence of student for the effective term. |  |
| `SGBSTDN_ASTD_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the academic standing override for a student for the effective term. |  |
| `SGBSTDN_TERM_CODE_ASTD` | `VARCHAR2(6 CHAR)` | This field identifies the term associated with the academic standing override. |  |
| `SGBSTDN_RATE_CODE` | `VARCHAR2(5 CHAR)` | This field identifies a specific assessment rate of the student for the effective term. |  |
| `SGBSTDN_ACTIVITY_DATE` | `DATE` | This field identifies the most current date record was created or updated. |  |
| `SGBSTDN_MAJR_CODE_1_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary major within the primary curriculum for the effective term. |  |
| `SGBSTDN_MAJR_CODE_2_2` | `VARCHAR2(4 CHAR)` | This field identifies the secondary major within the secondary curriculum for the effective term. |  |
| `SGBSTDN_EDLV_CODE` | `VARCHAR2(3 CHAR)` | A two position alphanumeric field which indicate the highest level of the education that the student completed |  |
| `SGBSTDN_INCM_CODE` | `VARCHAR2(2 CHAR)` | A two position alphanumeric field which indicate the income range of the student |  |
| `SGBSTDN_ADMT_CODE` | `VARCHAR2(2 CHAR)` | Admissions type from the admissions application |  |
| `SGBSTDN_EMEX_CODE` | `VARCHAR2(2 CHAR)` | General Student Employment Expectation Code |  |
| `SGBSTDN_APRN_CODE` | `VARCHAR2(2 CHAR)` | General Student Apprenticeship Code |  |
| `SGBSTDN_TRCN_CODE` | `VARCHAR2(2 CHAR)` | General Student Transfer Center Code |  |
| `SGBSTDN_GAIN_CODE` | `VARCHAR2(2 CHAR)` | This field identifies the employment and training code of the student for the effective term. |  |
| `SGBSTDN_VOED_CODE` | `VARCHAR2(2 CHAR)` | General Student Vocation Eduaction Status Code |  |
| `SGBSTDN_BLCK_CODE` | `VARCHAR2(10 CHAR)` | Block Schedule Code |  |
| `SGBSTDN_TERM_CODE_GRAD` | `VARCHAR2(6 CHAR)` | Term student intends to graduate. |  |
| `SGBSTDN_ACYR_CODE` | `VARCHAR2(4 CHAR)` | Year student intends to graduate. |  |
| `SGBSTDN_DEPT_CODE` | `VARCHAR2(4 CHAR)` | Department Code. |  |
| `SGBSTDN_SITE_CODE` | `VARCHAR2(3 CHAR)` | Site Code. |  |
| `SGBSTDN_DEPT_CODE_2` | `VARCHAR2(4 CHAR)` | Department Code for second curriculum. |  |
| `SGBSTDN_EGOL_CODE` | `VARCHAR2(2 CHAR)` | Educational Goal code. |  |
| `SGBSTDN_DEGC_CODE_DUAL` | `VARCHAR2(6 CHAR)` |  |  |
| `SGBSTDN_LEVL_CODE_DUAL` | `VARCHAR2(2 CHAR)` |  |  |
| `SGBSTDN_DEPT_CODE_DUAL` | `VARCHAR2(4 CHAR)` |  |  |
| `SGBSTDN_COLL_CODE_DUAL` | `VARCHAR2(2 CHAR)` |  |  |
| `SGBSTDN_MAJR_CODE_DUAL` | `VARCHAR2(4 CHAR)` |  |  |
| `SGBSTDN_BSKL_CODE` | `VARCHAR2(2 CHAR)` | Student Basic Skills Code |  |
| `SGBSTDN_PRIM_ROLL_IND` | `VARCHAR2(1 CHAR)` | Indicates whether the Primary Curriculum should be Rolled to Academic History |  |
| `SGBSTDN_PROGRAM_1` | `VARCHAR2(12 CHAR)` | Curriculum 1 Program Code |  |
| `SGBSTDN_TERM_CODE_CTLG_1` | `VARCHAR2(6 CHAR)` | Curriculum 1 Catalog Term Code |  |
| `SGBSTDN_DEPT_CODE_1_2` | `VARCHAR2(4 CHAR)` | Curriculum 1 - Department 2 |  |
| `SGBSTDN_MAJR_CODE_CONC_121` | `VARCHAR2(4 CHAR)` | Concentration Code 1 on Second Major of First Curriculum |  |
| `SGBSTDN_MAJR_CODE_CONC_122` | `VARCHAR2(4 CHAR)` | Concentration Code 2 on Second Major on First Curriculum |  |
| `SGBSTDN_MAJR_CODE_CONC_123` | `VARCHAR2(4 CHAR)` | Concentration Code 3 on Second Major on First Curriculum |  |
| `SGBSTDN_SECD_ROLL_IND` | `VARCHAR2(1 CHAR)` | Indicates whether the Secondary Curriculum should be Rolled to Academic History |  |
| `SGBSTDN_TERM_CODE_ADMIT_2` | `VARCHAR2(6 CHAR)` | Admission Term Code associated with the Secondary Curriculum |  |
| `SGBSTDN_ADMT_CODE_2` | `VARCHAR2(2 CHAR)` | Admissions Type Code associated with the Secondary Curriculum |  |
| `SGBSTDN_PROGRAM_2` | `VARCHAR2(12 CHAR)` | Curriculum 2 Program Code |  |
| `SGBSTDN_TERM_CODE_CTLG_2` | `VARCHAR2(6 CHAR)` | Curriculum 2 Catalog Term Code |  |
| `SGBSTDN_LEVL_CODE_2` | `VARCHAR2(2 CHAR)` | Curriculum 2 Level Code |  |
| `SGBSTDN_CAMP_CODE_2` | `VARCHAR2(3 CHAR)` | Curriculum 2 Campus Code |  |
| `SGBSTDN_DEPT_CODE_2_2` | `VARCHAR2(4 CHAR)` | Curriculum 2 - Department 2 |  |
| `SGBSTDN_MAJR_CODE_CONC_221` | `VARCHAR2(4 CHAR)` | Concentration 1 on Second Major of Second Curriculum |  |
| `SGBSTDN_MAJR_CODE_CONC_222` | `VARCHAR2(4 CHAR)` | Concentration 2 on Second Major of Second Curriculum |  |
| `SGBSTDN_MAJR_CODE_CONC_223` | `VARCHAR2(4 CHAR)` | Concentration 3 on Second Major of Second Curriculum |  |
| `SGBSTDN_CURR_RULE_1` | `NUMBER(8,0)` | Curriculum 1 Rule reference |  |
| `SGBSTDN_CMJR_RULE_1_1` | `NUMBER(8,0)` | Curriculum 1 Major 1 Rule Reference |  |
| `SGBSTDN_CCON_RULE_11_1` | `NUMBER(8,0)` | Concentration 1, Major 1, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CCON_RULE_11_2` | `NUMBER(8,0)` | Concentration 2, Major 1, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CCON_RULE_11_3` | `NUMBER(8,0)` | Concentration 3, Major 1, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CMJR_RULE_1_2` | `NUMBER(8,0)` | Major 2, Curriculum Rule Reference |  |
| `SGBSTDN_CCON_RULE_12_1` | `NUMBER(8,0)` | Concentration 1, Major 2, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CCON_RULE_12_2` | `NUMBER(8,0)` | Concentration 2, Major 2, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CCON_RULE_12_3` | `NUMBER(8,0)` | Concentration 3, Major 2, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CMNR_RULE_1_1` | `NUMBER(8,0)` | Minor 1, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CMNR_RULE_1_2` | `NUMBER(8,0)` | Minor 2, Curriculum 1 Rule Reference |  |
| `SGBSTDN_CURR_RULE_2` | `NUMBER(8,0)` | Curriculum 2 Rule Reference |  |
| `SGBSTDN_CMJR_RULE_2_1` | `NUMBER(8,0)` | Major 1, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_21_1` | `NUMBER(8,0)` | Concentration 1, Major 1, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_21_2` | `NUMBER(8,0)` | Concentration 2, Major 1, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_21_3` | `NUMBER(8,0)` | Concentration 3, Major 1, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CMJR_RULE_2_2` | `NUMBER(8,0)` | Major 2, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_22_1` | `NUMBER(8,0)` | Concentration 1, Major 2, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_22_2` | `NUMBER(8,0)` | Concentration 2, Major 2, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CCON_RULE_22_3` | `NUMBER(8,0)` | Concentration 3, Major 2, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CMNR_RULE_2_1` | `NUMBER(8,0)` | Minor 1, Curriculum 2 Rule Reference |  |
| `SGBSTDN_CMNR_RULE_2_2` | `NUMBER(8,0)` | Minor 2, Curriculum 2 Rule Reference |  |
| `SGBSTDN_PREV_CODE` | `VARCHAR2(2 CHAR)` | General Student record Progress Evaluation code. This code overrides the code in SHRTTRM. |  |
| `SGBSTDN_TERM_CODE_PREV` | `VARCHAR2(6 CHAR)` | General Student record Progress Evaluation term. This is the term for which the progress evaluation code override becomes effective. |  |
| `SGBSTDN_CAST_CODE` | `VARCHAR2(2 CHAR)` | General Student record Combined Academic Standing code. This code overrides the code in SHRTTRM. |  |
| `SGBSTDN_TERM_CODE_CAST` | `VARCHAR2(6 CHAR)` | General Student record Combined Academic Standing term. This is the term for which the combined academic standing code override becomes effective. |  |
| `SGBSTDN_DATA_ORIGIN` | `VARCHAR2(30 CHAR)` | DATA SOURCE: Source system that created or updated the row |  |
| `SGBSTDN_USER_ID` | `VARCHAR2(30 CHAR)` | USER ID: The most recent user to create or update a record. |  |
| `SGBSTDN_SCPC_CODE` | `VARCHAR2(6 CHAR)` | STUDENT CENTRIC PERIOD CYCLE CODE: Cycle Code for the student centric period. |  |
| `SGBSTDN_SURROGATE_ID` | `NUMBER(19,0)` | SURROGATE ID: Immutable unique key |  |
| `SGBSTDN_VERSION` | `NUMBER(19,0)` | VERSION: Optimistic lock token. |  |
| `SGBSTDN_VPDI_CODE` | `VARCHAR2(6 CHAR)` | VPDI CODE: Multi-entity processing code. |  |
| `SGBSTDN_GUID` | `VARCHAR2(36 BYTE)` | GUID: Global Unique Identifier to uniquely identify the record of a resource for integration. |  |


## Queries
- - -

### Most Recent Record for Student

Find the most recent SGBSTDN record for each student.

```sql title="most_recent.sql"
--8<-- "table-definitions/SGBSTDN/sql/most_recent.sql"
```

### 1st Major, Minor, Concentration for Student

Find the 1st major, minor, and concentration for each student based on the most recent SGBSTDN record.

```sql title="majr_minor_conc.sql"
--8<-- "table-definitions/SGBSTDN/sql/majr_minor_conc.sql"
```
