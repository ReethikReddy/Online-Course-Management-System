#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    project_root = Path(__file__).resolve().parents[1]
    venv_python = project_root / "env" / "Scripts" / "python.exe"
    current_python = Path(sys.executable).resolve()

    # Use the project's virtualenv interpreter if available.
    if venv_python.exists() and current_python != venv_python.resolve():
        raise SystemExit(subprocess.call([str(venv_python), *sys.argv]))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocms.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
