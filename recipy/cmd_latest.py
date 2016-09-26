import click
from recipy.cli import pass_config


@click.command('latest', short_help='Show latest run.')
@click.option('--diff', '-d', is_flag=True, help='Show diff.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
def cmd(diff, json):
    """Show latest ReciPy run."""
    click.echo('Latest Run...')
