"""This module provides the mrtodo database functionality."""
# mrtodo/database.py

import configparser
import json
from pathlib import Path
from typing import Any, Dict, List, NamedTuple

from mrtodo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

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


class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int


class DatabaseHandler:
    """DatabaseHandler allows reading and writing data to the to-do database (json)"""
    def __init__(self, db_path: Path) -> None:
        """Explanation of __init__ and self

        self: used to represent the instance of a class. By using "self" we access the attribute and methods of the
        class

        __init__: This method is called when an object is created from a class, and it allows the class to initialize
        the attribute of the class
        """
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        """Takes instance of a class as input and returns a DBResponse"""
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:  # Catch wrong JSON format
                    return DBResponse([], JSON_ERROR)
        except OSError:  # Catch file IO problems
            return DBResponse([], DB_READ_ERROR)

    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError:  # Catch file IO problems
            return DBResponse(todo_list, DB_WRITE_ERROR)
