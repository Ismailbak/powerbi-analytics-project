"""extract.py

Small extraction example: fetch data from an API or query a DB and save raw files.
"""
import argparse
import logging
import json
from pathlib import Path
import requests
from etl.utils.helpers import load_config, ensure_dir

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("etl.extract")


def extract_from_api(cfg: dict):
    base = cfg.get("etl", {}).get("api", {}).get("base_url")
    if not base:
        raise ValueError("No API base_url in config")
    resp = requests.get(base)
    resp.raise_for_status()
    return resp.json()


def save_raw(data, path: str):
    p = ensure_dir(path)
    out = Path(p) / "raw_data.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
    logger.info("Wrote raw data to %s", out)
    return str(out)


def main(config_path: str):
    cfg = load_config(config_path)
    src = cfg.get("etl", {}).get("source")
    if src == "api_or_db":
        data = extract_from_api(cfg)
    else:
        data = {}
    save_raw(data, cfg.get("paths", {}).get("raw", "data/raw"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", dest="config", default="config.yaml")
    args = parser.parse_args()
    main(args.config)
