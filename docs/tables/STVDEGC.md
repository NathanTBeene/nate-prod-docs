---
tags:

---

# STVDEGC

Degree Code Validation Table

!!! abstract "Definition Table"
    This is a validation/lookup table that defines valid codes for other tables.

## Schema

| Column | Type | Description | Definition |
| --- | --- | --- | --- |
| `STVDEGC_CODE` | `VARCHAR2(6 CHAR)` | This field identifies the degree code referenced in the Recruiting, Admissions, Gen. Student, Registration, Academic History and Degree Audit Modules. 000000 - Degree Not Declared. | [TEST](TEST.md) |
| `STVDEGC_DESC` | `VARCHAR2(30 CHAR)` | This field specifies the degree (e.g. Bachelor of Business Administration, Master of Arts, Juris Doctor, etc.) associated with the degree code. |  |
| `STVDEGC_LEVEL_ONE` | `VARCHAR2(2 CHAR)` | This field is not currently in use. |  |
| `STVDEGC_LEVEL_TWO` | `VARCHAR2(2 CHAR)` | This field is not currently in use. |  |
| `STVDEGC_LEVEL_THREE` | `VARCHAR2(2 CHAR)` | This field is not currently in use. |  |
| `STVDEGC_FA_COUNT_IND` | `VARCHAR2(1 CHAR)` | This field indicates whether the degree will count toward financial aid. Y - Count in financial aid. |  |
| `STVDEGC_ACTIVITY_DATE` | `DATE` | This field identifies the most recent date a record was created or updated. |  |
| `STVDEGC_ACAT_CODE` | `VARCHAR2(2 CHAR)` | Degree Award Catagory Code. |  |
| `STVDEGC_SYSTEM_REQ_IND` | `VARCHAR2(1 CHAR)` | System Required Indicator |  |
| `STVDEGC_DLEV_CODE` | `VARCHAR2(2 CHAR)` | Degree Level Code. |  |
| `STVDEGC_VR_MSG_NO` | `NUMBER(6,0)` | The Voice Response message number assigned to the recorded message that describes the degree code. |  |
| `STVDEGC_DISP_WEB_IND` | `VARCHAR2(1 CHAR)` | 'N' Web display indicator |  |
| `STVDEGC_SURROGATE_ID` | `NUMBER(19,0)` | SURROGATE ID: Immutable unique key |  |
| `STVDEGC_VERSION` | `NUMBER(19,0)` | VERSION: Optimistic lock token. |  |
| `STVDEGC_USER_ID` | `VARCHAR2(30 CHAR)` | USER ID: The user ID of the person who inserted or last updated this record. |  |
| `STVDEGC_DATA_ORIGIN` | `VARCHAR2(30 CHAR)` | DATA ORIGIN: Source system that created or updated the data. |  |
| `STVDEGC_VPDI_CODE` | `VARCHAR2(6 CHAR)` | VPDI CODE: Multi-entity processing code. |  |

## Values

| Code | Description |
| --- | --- |
| AGS | Associate of General Studies |
| MSL | Master of School Leadership |
| MSBL | Master of Studies in Bus Law |
| MSM | Master of Science in Mgmt |
| MHCL | Master of Health Leadership |
| MMIS | Master of Management Info Sys |
| MSPM | Master of Svc/Prod Mgmt |
| PHD | Ph.D |
| MA | Master of Arts |
| BA | Bachelor of Arts |
| BS | Bachelor of Science |
| MS | Master of Science |
| MBA | Master of Business Admin. |
| BBA | Bachelor of Business Admin. |
| 000000 | Undeclared |
| JD | Juris Doctor |
| MD | Doctor of Medicine |
| AS | Associate in Science |
| AA | Associate in Arts |
| AAS | Associate in Applied Science |
| BED | Bachelor of Education |
| MED | Master of Education |
| EDD | Doctor of Education |
| BFA | Bachelor of Fine Arts |
| BSW | Bachelor of Social Work |
| DDS | Doctor of Dental Surgery |
| MFA | Master of Fine Arts |
| MSW | Master of Social Work |
| CERT | Certificate Program |
| BA/MA | 5 yr Bachelors and Masters |
| BAR | Bachelor of Architecture |
| BM | Bachelor of Music |
| DMD | Doctor of Dental Medicine |
| AT | Associate in Technology |
| DIPL | Diploma |
| BSN | Bachelor of Science in Nursing |
| CPR | CPR Certification |
| NODEG | No Degree |
| BMS | Bachelor of Management Studies |
| DOC | Doctorate/PhD |
| MD/PHD | Medical |
| MSN | Master of Science in Nursing |
| BCOMM | Bachelor of Commerce |
| MBA/JD | MBA/JD Joint Program |
| MBE | Master of Business Education |
| MPHIL | Master of Philosophy |
| BSAD | Bachelor of Science, Bus Admin |
| BMED | Bachelor of Music Education |
| BPA | Bachelor of Prof Accountancy |
| BSE | Bachelor of Science in Educati |
| DD | Doctor of Divinity |
| DHL | Doctor of Humane Letters |
| DL | Doctor of Laws |
| DM | Doctor of Music |
| DS | Doctor of Science |
| A | Associates |
| ALA | Associate of Liberal Arts |
| BSCE | Bachelor of Science Civil Eng |
| DA | Doctor of Arts |
| DMA | Doctor of Music Arts |
| DO | Doctor of Osteopathy |
| EDS | Educational Specialist |
| MACC | Master of Accountancy |
| MALS | Master of Arts in Library Sci |
| MAR | Master of Arts in Religion |
| MAT | Master of Arts in Technology |
| MDIV | Master of Divinity |
| MENGR | Master of Engineering |
| MHR | Master of Human Relations |
| MLIS | Master of Library and Info Sci |
| MLS | Master of Library Science |
| MM | Master of Music |
| MME | Master of Music Education |
| MMED | Master of Music Education |
| MPA | Master of Public Admin |
| MSE | Master of Science Education |
| MSLS | Master of Science in Lib Sci |
| MT | Master of Technology |
| MVS | Master of Vision Science |
| MLINS | Master of Liberal Ind Studies |
| ZZ | Degree from other institution |
| BAED | Bachelor of Arts in Education |
| BGS | Bachelor of General Studies |
| BME | Bachelor of Music Education |
| BSED | Bachelor of Science in Educati |
| BSHEA | Bachelor of Health Care Adm |
| BSSCED | Bachelor of Science in Sci Ed |
| BT | Bachelor of Technology |
| MSED | Master of Science in Education |
| OD | Doctor of Optometry |
| UCERT | Undergraduate Certificate |
| GCERT | Certificate after Masters |
| B | Bachelors |
| M | Masters |
| ASSOC | Associates |
| MHA | Master of Hospitality Admin |
| PHARMD | Doctor of Pharmacy |
| BAS | Bachelor of Applied Science |
| BUS | Bachelor of University Studies |
| BSSLP | Bach of Sci in Spch Lang Path |
| BARSC | Bachelor of Arts & Sciences |
| BCERTM | Grad Cert Betw Bach Masters |
| AFA | Associate of Fine Arts |
| BLS | Bachelor of Liberal Studies |
| BSRCT | Bach of Sci in Resp Care Thera |
| DVM | Doctor of Veterinary Medicine |
| MLST | Master of Legal Studies |
| AUD | Doctor of Audiology |
| MHSC | Master of Health Sciences |
| DC | Doctor of Chiropractic |
| BSHES | Bach of Sci in Human Env Sci |
| MSSWE | Master of Software Engin |
| BSMLS | Bach of Sci in Med Lab Sci |
| OTD | Doctor of Occupational Therapy |
| AB | Associate in Business |
| AAB | Associate in Applied Business |
| AAA | Associate in Applied Arts |
| MSMLS | Master of Sci in Med Lab Sci |
| DE | Doctor of Engineering |
| BENG | Bachelor of Engineering |
| BAA | Bachelor of Applied Arts |
| BCERT | Certificate after Bachelors |
| ASN | Associate of Sci in Nursing |
| BL | Bachelor of Law |
| BMDS | Bachelor of Multidisc Studies |
| MPH | Master of Public Health |
| HBD | Honors Baccalaureate Degree |
| MPAS | Master of Physician Asst. Stud |
| DBA | Doctor of Business Admin |
| MMS | Master of Medical Science |
| MAFM | Master of Accnt & Fin Mgmt |

## Queries
- - -

*No queries documented yet.*
