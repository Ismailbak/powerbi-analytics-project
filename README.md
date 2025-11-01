# powerbi-analytics-project

Repository scaffold for a Power BI analytics pipeline including ETL, data validation, notebooks, and CI/CD for automated updates.

Structure (key files):
- `etl/` — Python ETL scripts (extract, transform, load)
- `data/` — raw / processed / external datasets
- `docs/` — project requirements, data dictionary, dashboard guide
- `notebooks/` — analysis & feature engineering notebooks
- `powerbi/` — Power BI file and supporting docs
- `.github/workflows/data-pipeline.yml` — automated ETL/test pipeline

Getting started:
1. Create a Python virtual environment and install requirements:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

2. Update `config.yaml` with your data source credentials and Power BI identifiers.
3. Run `python etl/extract.py` then `python etl/transform.py` and `python etl/load.py` (or use the orchestrator you prefer).

CI/CD:
The included GitHub Actions workflow runs ETL and tests on a schedule or on-demand; see `.github/workflows/data-pipeline.yml`.

Notes:
- This repo provides a scaffold and examples. Replace placeholders with production credentials and robust error handling before using in production.
