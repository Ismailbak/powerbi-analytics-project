"""load.py

Example loader: either publish dataset to Power BI or export processed files for Power BI Desktop.
This is a placeholder — replace with your Power BI REST or file upload logic.
"""
import argparse
import logging
from pathlib import Path
from etl.utils.helpers import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("etl.load")


def export_for_powerbi(processed_dir: str, out_path: str = 'powerbi/export.xlsx'):
    from pathlib import Path
    import pandas as pd

    p = Path(processed_dir)
    files = list(p.glob('*.csv'))
    if not files:
        logger.warning('No processed CSV files found in %s', processed_dir)
        return

    writer = pd.ExcelWriter(out_path, engine='openpyxl')
    for f in files:
        name = f.stem[:30]
        df = pd.read_csv(f)
        df.to_excel(writer, sheet_name=name, index=False)
    writer.save()
    logger.info('Wrote excel export to %s', out_path)
    return out_path


def main(config_path: str):
    cfg = load_config(config_path)
    processed_dir = cfg.get('paths', {}).get('processed', 'data/processed')
    out = export_for_powerbi(processed_dir)
    logger.info('Export complete: %s', out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', dest='config', default='config.yaml')
    args = parser.parse_args()
    main(args.config)
