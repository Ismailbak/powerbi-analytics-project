"""transform.py

Load raw files, do cleaning and transformations, write processed outputs.
"""
import argparse
import logging
from pathlib import Path
import pandas as pd
from etl.utils.helpers import load_config, ensure_dir

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("etl.transform")


def transform_sales(raw_path: str):
    # Example: read JSON or CSV and normalize into DataFrame
    p = Path(raw_path)
    if p.suffix == '.json':
        df = pd.read_json(p)
    else:
        df = pd.read_csv(p)

    # Basic cleaning examples
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    # Drop duplicates
    df = df.drop_duplicates()

    # Cast types and fill nans where appropriate
    for col in df.select_dtypes(include=['float']).columns:
        df[col] = df[col].fillna(0.0)

    return df


def save_processed(df: pd.DataFrame, out_dir: str, name: str = 'processed.csv'):
    out = ensure_dir(out_dir)
    path = Path(out) / name
    df.to_csv(path, index=False)
    logger.info("Saved processed file: %s", path)
    return str(path)


def main(config_path: str):
    cfg = load_config(config_path)
    raw_dir = cfg.get('paths', {}).get('raw', 'data/raw')
    processed_dir = cfg.get('paths', {}).get('processed', 'data/processed')

    # naive: look for raw_data.json
    raw_file = Path(raw_dir) / 'raw_data.json'
    if not raw_file.exists():
        logger.warning('No raw file at %s', raw_file)
        return

    df = transform_sales(str(raw_file))
    save_processed(df, processed_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', dest='config', default='config.yaml')
    args = parser.parse_args()
    main(args.config)
