#!/usr/bin/env python3

import click
from tabulate import tabulate
from todox.data import tododata

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx=None):
    if ctx.invoked_subcommand is None:
        showtodos()

@cli.command()
@click.argument("content", nargs=-1)
def add(content):
    if content:
        content = " ".join(content)
        tododata.save_todo(content)
    else:
        add_with_editor()

def add_with_editor():
    content = click.edit()
    if content is not None:
        content = "".join(content)
        tododata.save_todo(content)

@cli.command(name="list")
def showtodos():
    todos = tododata.get_todos()
    click.echo(tabulate(todos, headers=["Content"]))

@cli.command()
@click.argument("id")
def delete(id):
    tododata.delete_todo(id)
    click.echo(f"Todo {id} deleted")

def main():
    cli()

if __name__ == "__main__":
    main()