"""Module for reading and writing persistent variables."""

import os
from datetime import datetime

VAR_FOLDER = "_variables"
SUFFIX_INDEX = "-index.txt"
SUFFIX_START_DATE = "-run-started.txt"
SUFFIX_END_DATE = "-run-completed.txt"


# INDEX


def read_index(prefix):
    """Read the variable from the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_INDEX}"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return int(file.read().strip())
    return "error"


def write_index(value, prefix):
    """Write the variable to the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_INDEX}"
    with open(path, "w", encoding="utf-8") as file:
        file.write(str(value))


# DATE_RUN_STARTED


def read_run_start_date(prefix):
    """Read the date from the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_START_DATE}"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            start_date_str = file.read().strip()
            start_date = datetime.strptime(
                start_date_str, "%Y-%m-%d %H:%M:%S"
            ).timestamp()
            return start_date
    return datetime(1982, 7, 22).timestamp()


def write_run_start_date(prefix):
    """Write the current date to the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_START_DATE}"
    with open(path, "w", encoding="utf-8") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# DATE_RUN_CPMPLETED


def read_last_completed_date(prefix):
    """Read the date from the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_END_DATE}"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            last_completed_date_str = file.read().strip()
            last_completed_date = datetime.strptime(
                last_completed_date_str, "%Y-%m-%d %H:%M:%S"
            ).timestamp()
            return last_completed_date
    return datetime(1982, 7, 22).timestamp()


def write_last_completed_date(prefix):
    """Write the current date to the file."""
    path = f"{VAR_FOLDER}/{prefix}{SUFFIX_END_DATE}"
    with open(path, "w", encoding="utf-8") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
