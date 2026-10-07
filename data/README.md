# Data

The datasets are not stored in this repository: each notebook downloads its data
from the public IBM Skills Network storage when it runs, and any file it writes
(CSV, SQLite) is ignored by git.

| Dataset | Used in | Source |
|---|---|---|
| `jobs.json`: job postings (subset of *Jobs on Naukri.com*, Kaggle, public domain) | 01 | [IBM Skills Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json) |
| `survey-data-duplicates.csv`: Stack Overflow Developer Survey with injected duplicates (65,447 rows) | 02–05 | [IBM Skills Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/UDKAZw-kz18Yj8P6icf_qw/survey-data-duplicates.csv) |
| `survey-data.csv`: Stack Overflow Developer Survey (65,437 rows × 114 columns) | 06–10, 13–18 | [IBM Skills Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv) |
| `survey-results-public.sqlite`: the same survey as a SQLite database | 11–12 | [IBM Skills Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/QR9YeprUYhOoLafzlLspAw/survey-results-public.sqlite) |

The job-postings counts (`job-postings.xlsx`) and the salaries by language
(`popular-languages.csv`, collected via web scraping) used in the presentation are
the outputs of the data-collection step.
