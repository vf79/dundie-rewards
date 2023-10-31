"""Cli Dundie module."""
import json
from importlib.metadata import version

import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

# from sqlalchemy.exc import SAWarning
# from sqlmodel.sql.expression import Select, SelectOfScalar


# import warnings


# SelectOfScalar.inherit_cache = True  # type: ignore
# Select.inherit_cache = True  # type: ignore
#
# warnings.filterwarnings("ignore", category=SAWarning)


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True
click.rich_click.STYLE_ERRORS_SUGGESTION = "magenta italic"
click.rich_click.ERRORS_SUGGESTION = (
    "Try running the '--help' flag for more information."
)


@click.group()
@click.version_option(version)
def main():
    """Dunder Mifflin Rewards System.

    This cli application controls DM rewards.
    - admins can load information to the people database and assign points.
    - users can view reports and transfer points.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Load the file to the database.

    ## Features
    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dunder Mifflin Associates")
    headers = ["email", "name", "dept", "role", "currency", "created"]
    for header in headers:
        table.add_column(header, style="green")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Show information about users or dept."""
    result = core.read(**query)

    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))

    table = Table(title="Dunder Mifflin Report")
    if not result:
        table.add_column("Result", style="green")
        table.add_row("Nothing value")

    else:
        for key in result[0]:
            table.add_column(key.title().replace("_", " "), style="green")

        for person in result:
            table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Add points to the user or dept."""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def remove(ctx, value, **query):
    """Remove points from user or dept."""
    core.add(-value, **query)
    ctx.invoke(show, **query)
