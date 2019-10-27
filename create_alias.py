import click
import os


@click.command()
@click.argument("alias")
@click.argument("command")
def create_alias(alias, command):
    filepath = build_filepath(os.environ["SHELL"])
    append_line_to_file(filepath, prepare_alias_statement(alias, command))


def build_filepath(shell):
    return f"~/.{shell.split('/')[-1]}rc"


def prepare_alias_statement(alias, command):
    return f"alias {alias}='{command}'\n"


def append_line_to_file(filepath, line):
    with open(os.path.expanduser(filepath), "a") as file:
        file.write(line)


if __name__ == '__main__':
    create_alias()
