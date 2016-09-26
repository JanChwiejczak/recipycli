import click
from recipy.cli import pass_config


@click.command('search', short_help='Search for file in runs.')
@click.option('--exact', '-e', is_flag=True,
              help='Match based exactly on FILENAME.')
@click.option('--id', '-i', is_flag=True,
              help='Match based on a fragment of run id.')
@click.option('--filepath', '-f', is_flag=True,
              help='Match all files from the same directory as FILENAME.')
@click.option('--all', '-a', is_flag=True, help='Return all results.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.argument('filename', required=True)
@pass_config
def cmd(config, exact, id, filepath, all, json, filename):
    """Search for FILENAME or part of it in all ReciPy runs, you can also
    use regular expressions. By default it only returns the most recent result."""
    if config.debug:
        click.echo('Debug info...')
    click.echo('Searching...')
