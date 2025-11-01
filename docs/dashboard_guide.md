# Dashboard Guide & Power BI Best Practices

- Keep the data model star-shaped: facts + dimension tables.
- Use Power Query for light transformations; keep complex joins in ETL.
- Avoid calculated columns in Power BI when the ETL can compute them.
- Use incremental refresh for large datasets and publish datasets to a workspace.
- Document measures, DAX logic and expected card values in `powerbi/data_model.docx`.

Performance tips:
- Reduce columns to only what's needed.
- Push heavy aggregations to the ETL layer.
- Use proper data types (Date, Decimal, Integer) to enable compression.
