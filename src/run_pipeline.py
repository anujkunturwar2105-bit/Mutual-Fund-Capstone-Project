"""
Bluestock Mutual Fund Master Pipeline.

Executes the main data ingestion, database loading,
star-schema creation, and validation steps in sequence.
"""

import subprocess
import sys
from pathlib import Path


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"


# Scripts executed by the master pipeline
PIPELINE_STEPS = [
    "data_ingestion.py",
    "create_database.py",
    "load_database.py",
    "load_star_schema.py",
    "verify_row_counts.py",
]


def run_script(script_name):
    """
    Execute a pipeline script.

    Parameters
    ----------
    script_name : str
        Name of the Python script to execute.

    Raises
    ------
    FileNotFoundError
        If the script does not exist.

    RuntimeError
        If the script exits with an error.
    """

    script_path = SRC_DIR / script_name

    if not script_path.exists():
        raise FileNotFoundError(
            f"Pipeline script not found: {script_path}"
        )

    print("\n" + "=" * 70)
    print(f"Running: {script_name}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed "
            f"with exit code {result.returncode}."
        )

    print(f"✓ {script_name} completed successfully.")


def main():
    """Run all pipeline steps in sequence."""

    print("=" * 70)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 70)

    for script in PIPELINE_STEPS:
        run_script(script)

    print("\n" + "=" * 70)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()