import click

from . import __version__ as VERSION


class CliConfig(object):
    """Passes cli configuration between commands."""
    def __init__(self, debug):
        self.debug = debug

pass_config = click.make_pass_decorator(CliConfig)


@click.group()
@click.version_option(version=VERSION)  # TODO: perhaps hardcode version if this is the only place
@click.option('--debug', is_flag=True,
              help='Show debug info while running command.')
def main(debug):
    """Frictionless provenance tracking in Python."""
    pass


@main.command()
@click.option('--fuzzy', '-f', is_flag=True,
              help='Match based on a part of file name.')
@click.option('--id', '-i', is_flag=True,
              help='Match based on a fragment of run id.')
@click.option('--filepath', '-p', is_flag=True,
              help='Match all files from the same directory as FILENAME.')
@click.option('--all', '-a', is_flag=True, help='Return all results.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.argument('filename', type=str, required=True)
def search(fuzzy, id, filepath, all, json, filename):
    """Search for exact FILENAME in run outputs.
    By default it only returns the most recent result."""
    click.echo('Searching...')
