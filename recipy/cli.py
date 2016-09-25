import click

from . import __version__ as VERSION


class CliConfig(object):
    """Passes configuration between commands."""
    def __init__(self):
        self.debug = False

pass_config = click.make_pass_decorator(CliConfig, ensure=True)


@click.group()
# TODO: perhaps hardcode version if this is the only place
@click.version_option(version=VERSION)
@click.option('--debug', is_flag=True,
              help='Show debug info while running command.')
@pass_config
def main(config, debug):
    """Frictionless provenance tracking in Python.
    For more info type: recipy COMMAND --help"""
    config.debug = debug


@main.command()
@click.option('--fuzzy', '-f', is_flag=True,
              help='Match based on a part of file name.')
@click.option('--id', '-i', is_flag=True,
              help='Match based on a fragment of run id.')
@click.option('--filepath', '-p', is_flag=True,
              help='Match all files from the same directory as FILENAME.')
@click.option('--all', '-a', is_flag=True, help='Return all results.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.argument('filename', type=click.Path(exists=True), required=True)
@pass_config
def search(config, fuzzy, id, filepath, all, json, filename):
    """Search for exact FILENAME in run outputs.
    By default it only returns the most recent result."""
    if config.debug:
        click.echo('Debug info...')
    click.echo('Searching...')
