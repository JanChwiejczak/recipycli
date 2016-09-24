import click

from . import __version__ as VERSION


@click.command()
@click.version_option(version=VERSION)
@click.option('--count', default=1, type=int, help='How many times to greet')
@click.argument('name', default='world', required=False)
def main(name, count):
    """Test layout for recipy cli."""
    for x in range(count):
        click.echo('Hello, {}.'.format(name))
