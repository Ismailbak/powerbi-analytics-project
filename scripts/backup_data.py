"""backup_data.py

Simple script to copy processed data to a dated backup folder.
"""
import shutil
from datetime import datetime
from pathlib import Path
import argparse


def main(processed_dir='data/processed', backup_root='data/backups'):
    p = Path(processed_dir)
    if not p.exists():
        print('No processed data to backup.')
        return
    ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    dest = Path(backup_root) / ts
    dest.mkdir(parents=True, exist_ok=True)
    for f in p.glob('*'):
        shutil.copy2(f, dest / f.name)
    print('Backed up processed data to', dest)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--processed', default='data/processed')
    parser.add_argument('--backup', default='data/backups')
    args = parser.parse_args()
    main(args.processed, args.backup)
