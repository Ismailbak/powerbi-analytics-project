# File and Folder Descriptions

This document lists each file and folder in the repository and gives a short explanation of what should go in each. Use this as a guide for what to implement, expand, or replace with production-ready code and artifacts.

Root files
- `README.md` — Project overview, quick start instructions, commands to run ETL and tests, and notes about secrets and configuration. Keep it up to date with setup steps and CI behavior.
- `.gitignore` — Patterns for git to ignore (virtual envs, large data, .pbix, OS artifacts). Keep sensitive files out of the repo.
- `requirements.txt` — Pin or list Python libraries required by ETL, tests, and scripts. Update when adding new dependencies.
- `config.yaml` — Environment- and pipeline-specific configuration (file paths, API endpoints, DB connection details, Power BI identifiers). Do NOT keep secrets here in production — use environment variables / GitHub Secrets.

.github/
- `workflows/data-pipeline.yml` — GitHub Actions workflow that installs dependencies, runs ETL steps, runs tests, and optionally publishes or exports artifacts. Configure secrets and schedule here.

data/
- `data/raw/` — Save raw/original data fetched from sources (APIs, DB exports, vendor CSVs). These files are append-only and should not be modified by the ETL once written. Keep provenance metadata alongside files (timestamp, source).
- `data/processed/` — Cleaned, transformed datasets ready to be consumed by Power BI. Store CSV/Parquet/Feather here. Prefer column types and consistent schemas.
- `data/external/` — Third-party reference data (lookup tables, mapping files) that should be versioned separately from raw source data.

docs/
- `docs/project_requirements.md` — Functional and non-functional requirements for the analytics pipeline. Include acceptance criteria and SLAs.
- `docs/data_dictionary.md` — Data schema documentation: tables, columns, types, allowed values, null rules, and example records.
- `docs/dashboard_guide.md` — Power BI design and performance best practices, recommended visuals, incremental refresh guidance, measures to document, accessibility and naming conventions.
- `docs/file_descriptions.md` — (This file) concise descriptions of files and their intended contents.

etl/
- `etl/extract.py` — Functions and CLI to extract data from sources (API calls, database queries, S3, etc.). Responsibilities: authenticate to sources, fetch data, save raw payloads to `data/raw/` and emit provenance metadata (timestamps, parameters). Keep this code idempotent and robust to partial failures.
- `etl/transform.py` — Load raw files, apply cleaning and transformation logic (type casting, canonicalization, joins, aggregations), validate output schemas, write processed data to `data/processed/`. Include logging, small/large data handling (chunking), and optional profiling.
- `etl/load.py` — Prepare outputs for Power BI consumption. Options:
  - Export processed CSV/XLSX for Power BI Desktop.
  - Push data into a Power BI dataset via REST API (service principal) or upload to a data store used by Power BI (Azure SQL, ADLS).
  - Trigger dataset refresh if using Power BI Service.
- `etl/utils/helpers.py` — Small reusable helpers: config loader, path helpers, retry wrappers, common logging setup, secrets helpers (reading from env), and simple I/O utilities.

notebooks/
- `notebooks/01_data_exploration.ipynb` — Exploratory analysis: load raw/processed data, summary statistics, distributions, and simple visual checks to understand content and quality.
- `notebooks/02_feature_engineering.ipynb` — Prototype feature creation and aggregations. Keep exploratory code here when building new measures or columns that may later be moved to `transform.py`.
- `notebooks/03_data_validation.ipynb` — Data validation experiments: demonstrate pandera or custom checks, expected distributions, and examples for schema assertions.

powerbi/
- `powerbi/dashboard.pbix` — Main Power BI Desktop file (binary). Keep the file in the repo only if necessary; otherwise store it in artifact storage. Add a clear versioning strategy when updating this file.
- `powerbi/data_model.docx` — Human-readable documentation for the data model: tables, relationships, measures, and incremental-refresh details.
- `powerbi/screenshots/` — Store screenshots of the dashboard for documentation and PR reviews.

scripts/
- `scripts/setup_environment.py` — Convenience script to create and initialize a Python virtual environment and install dependencies. Document platform-specific activation commands.
- `scripts/deploy_dashboard.py` — Script to automate deployment to Power BI Service (publish PBIX, set dataset credentials, configure refresh). Implement secure authentication (service principal) and GitHub Secrets for credentials.
- `scripts/backup_data.py` — Utilities to copy processed data to backups or an archive location (timestamped). Use for disaster recovery or before destructive transformations.

tests/
- `tests/test_etl.py` — Unit tests for ETL functions (transformations and helpers). Keep tests fast and deterministic, use small sample files or fixtures.
- `tests/test_data_quality.py` — Tests for data-quality functions and schema assertions (null checks, uniqueness, range checks). Integrate these into CI so pipeline fails early on broken data.

Other notes and recommendations
- Inline comments vs central doc: This document provides a central overview. For code files (`etl/*.py`, `scripts/*.py`) also add short header comments in the top of each file that include: purpose, inputs, outputs, side effects, and expected config keys. Keep functions documented with docstrings and explicit contracts (types, return values).
- Secrets & credentials: Never store credentials in `config.yaml` in a public repo. Use environment variables during local runs and GitHub Secrets for CI.
- Productionization steps: add retry/backoff, observability (metrics/logging), idempotency, schema migrations, and incremental processing for large tables.

If you want me to also insert short header docstrings/comments directly into each Python file (so the comment appears at the top of the source file), I can do that next. Which would you prefer: a single central doc (this file) or inline header comments inside each source file?"}]}{