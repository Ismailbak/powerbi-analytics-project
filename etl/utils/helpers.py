"""Utility helpers for ETL scripts"""
from pathlib import Path
import yaml
import logging

logger = logging.getLogger(__name__)


def load_config(path: str):
    """Load YAML configuration file.

    Args:
        path: path to YAML file

    Returns:
        dict parsed configuration
    """
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def ensure_dir(path: str):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
