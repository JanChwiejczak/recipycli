import click
from recipy.cli import pass_config


@click.command('gui', short_help='Launch GUI in default browser.')
@click.option('--no-browser', is_flag=True,
              help="Start GUI app, but don't open a browser.")
@pass_config
def cmd(config, no_browser):
    """Start ReciPy GUI in default browser."""
    click.echo('Starting GUI...')
