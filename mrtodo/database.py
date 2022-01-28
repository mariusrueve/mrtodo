"""This module provides the RP To-Do database functionality."""
# mrtodo/database.py

import configparser
from pathlib import Path

from mrtodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database.

    Args:
        config_file: A Path object from pathlib

    Returns:
        A Path object from pathlib
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    """Create the to-do database.

    Args:
        db_path: A Path object from pathlib

    Returns:
        An int value. SUCCESS(0) if no error, DB_WRITE_ERROR if error.
    """
    try:
        db_path.write_text("[]")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
