import click
from recipy.cli import pass_config


@click.command('search', short_help='Find run with this file.')
@click.option('--exact', '-e', is_flag=True,
              help='Match FILENAME exactly.')
@click.option('--id', '-i', is_flag=True,
              help='Match based on a fragment of run id.')
@click.option('--filepath', '-f', is_flag=True,
              help='Match all files from the same directory as FILENAME.')
@click.option('--all', '-a', is_flag=True, help='Return all runs.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.option('--inputs', is_flag=True, help='Restrict search to run inputs only.')
@click.option('--outputs', is_flag=True, help='Restrict search to run outputs only.')
@click.argument('filename', required=True)
@pass_config
def cmd(config, exact, id, filepath, all, json, filename, inputs, outputs):
    """Search for FILENAME among all inputs and outputs recorded by ReciPy.
    By default, it returns partial matches and most recent run. You can
    use regular expressions in FILENAME.

    \b
    For example: recipy search -a --outputs newplot
    Will look through outputs of all runs and try to find a file containing
    newplot in its name.
    """
    click.echo('Searching...')
