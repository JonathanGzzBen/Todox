#!/usr/bin/env python3

import click
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

def showtodos():
    click.echo("Printing todos")
    pass

def main():
    cli()

if __name__ == "__main__":
    main()