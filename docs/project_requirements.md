# Project Requirements

Purpose: Build a repeatable pipeline to extract, transform and load data into Power BI with automated updates and validation.

Functional requirements:
- Extract data from APIs and/or databases.
- Clean and standardize data into `data/processed`.
- Run validation tests and notifications on failures.
- Publish dataset to Power BI or export clean files for report refresh.

Non-functional:
- Scheduled CI for daily updates.
- Modular ETL functions to support testing and reuse.
- Documentation for data dictionary and dashboard design.

Security:
- Do not store secrets in the repo. Use GitHub Secrets or environment variables.
