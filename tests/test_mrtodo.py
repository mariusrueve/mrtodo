# tests/test_mrtodo.py

import json
import pytest
from typer.testing import CliRunner
from mrtodo import DB_READ_ERROR, SUCCESS, __app_name__, __version__, cli, mrtodo

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


@pytest.fixture
def mock_json_file(tmp_path):
    """Creates and returns a temporary json file (db_file) with a single item to-do list in it"""
    todo = [{"Description": "Get some milk.", "Priority": 2, "Done": False}]
    db_file = tmp_path / "todo.json"  # tmp_path is a pathlib.Path object
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file


test_data1 = {
    "description": ["Clean", "the", "house"],  # Data to test Todoer.add()
    "priority": 1,
    "todo": {  # Expected return value of Todoer.add() with given input
        "Description": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}


@pytest.mark.parametrize(  # This decorator marks test_add() for parametrization
    # Called two times, for each given dataset
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS)
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS)
        )
    ]
)
def test_add(mock_json_file, description, priority, expected):
    todoer = mrtodo.Todoer(mock_json_file)
    assert todoer.add(description, priority) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2
