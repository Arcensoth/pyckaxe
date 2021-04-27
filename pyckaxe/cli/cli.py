import click

from pyckaxe import __version__
from pyckaxe.cli.utils import asyncify
from pyckaxe.utils import LOG_LEVELS, setup_logging
from pyckaxe.utils.logging.preview import preview_async_logging, preview_logging

# NOTE We need to support asyncio ourselves.
# See: https://github.com/pallets/click/issues/85
# Thankfully this is pretty easy to support. If one of our commands requires async
# somewhere down the line, we can just wrap it with the utility decorator provided in
# that GitHub issue.


__all__ = ("run",)


PROG_NAME = "pyckaxe"


@click.group()
@click.version_option(__version__, "-v", "--version")
@click.option(
    "-l",
    "--log",
    type=click.Choice(LOG_LEVELS, case_sensitive=False),
    default=LOG_LEVELS[2],
    help="The level of verbosity to log at.",
)
@click.option(
    "-ll",
    "--detailed-logs/--no-detailed-logs",
    default=False,
    help="Whether to use the detailed logging format.",
)
def cli(log: str, detailed_logs: bool):
    setup_logging(level=log.upper(), detailed=detailed_logs)


@cli.group("test", help="Contains sub-commands for various tests.")
def cli_test():
    pass


@cli_test.command("log", help="Preview logging output for each level.")
def cli_test_log():
    preview_logging()


@cli_test.command("async", help="Test async commands using random timers.")
@asyncify
async def cli_test_async():
    await preview_async_logging()


def run():
    cli(prog_name=PROG_NAME)
