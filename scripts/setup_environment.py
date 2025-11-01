"""Create venv and install requirements (Windows PowerShell friendly)."""
import subprocess
import sys
from pathlib import Path

venv_dir = Path('.venv')

if __name__ == '__main__':
    if not venv_dir.exists():
        print('Creating virtual environment...')
        subprocess.check_call([sys.executable, '-m', 'venv', str(venv_dir)])
    else:
        print('Virtual environment already exists.')
    print('To activate (PowerShell):')
    print('.\\.venv\\Scripts\\Activate.ps1')
    print('Then: pip install -r requirements.txt')
