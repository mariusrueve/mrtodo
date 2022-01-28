# mrtodo
Command-Line To-Do App With Python and Typer

## Installation

To run **mrtodo**, you need to run the following steps:

1. Download the application's source code to a `mrtodo/` directory
2. Create a Python virtual environment and activate it:

```sh
$ cd mrtodo/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

3. Install the dependencies:

```sh
(venv) $ python -m pip install -r requirements.txt
```

4. Initialize the application:

```sh
(venv) $ python -m mrtodo init
```

This command asks you to introduce the file path to store the application's database. You can also accept the default file path by pressing Enter.

## Usage

Once you've downloaded the source code and run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python -m mrtodo --help
Usage: mrtodo [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  add       Add a new to-do with a DESCRIPTION.
  clear     Remove all to-dos.
  complete  Complete a to-do by setting it as done using its TODO_ID.
  init      Initialize the to-do database.
  list      List all to-dos.
  remove    Remove a to-do using its TODO_ID.
```

You can also access the help message for specific commands by typing the command and then `--help`. For example, to display the help content for the `add` command, you can run the following:

```sh
$ python -m mrtodo add --help
Usage: mrtodo add [OPTIONS] DESCRIPTION...

  Add a new to-do with a DESCRIPTION.

Arguments:
  DESCRIPTION...  [required]

Options:
  -p, --priority INTEGER RANGE  [default: 2]
  --help                        Show this message and exit.
```

Calling `--help` on each command provides specific and useful information about how to use the command at hand.

## Features

**mrtodo** has the following features:

| Command            | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `init`             | Initializes the application's to-do database.                |
| `add DESCRIPTION`  | Adds a new to-do to the database with a `DESCRIPTION`.       |
| `list`             | Lists all the to-dos in the database.                        |
| `complete TODO_ID` | Completes a to-do by setting it as done using its `TODO_ID`. |
| `remove TODO_ID`   | Removes a to-do from the database using its `TODO_ID`.       |
| `clear`            | Removes all the to-dos by clearing the database.             |


# Notes
## Interesting Libraries
### Rich
[Rich](https://github.com/Textualize/rich) is a Python library for rich text and beautiful formatting in the terminal.

### Python Fire
[Python Fire](https://github.com/google/python-fire) is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

### Gooey
Turn (almost) any Python command line program into a full GUI application with one line
Link: https://github.com/chriskiehl/Gooey

# Credits
https://realpython.com/python-typer-cli/