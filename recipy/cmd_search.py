import click
from recipy.cli import pass_config


@click.command('search', short_help='Find run with this file.')
@click.option('--hash', '-h', is_flag=True,
              help='Match using hash value of FILENAME. Will find original run even if the name of a file has changed.')
@click.option('--all', '-a', is_flag=True, help='Return all runs.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.option('--inputs', is_flag=True, help='Restrict search to run inputs only.')
@click.option('--outputs', is_flag=True, help='Restrict search to run outputs only.')
@click.argument('filename', required=True)
@pass_config
def cmd(config, hash, all, json, inputs, outputs, filename):
    """Search for FILENAME among all inputs and outputs recorded by ReciPy.
    By default, it returns partial matches and most recent run. You can
    use regular expressions in FILENAME.

    \b
    For example: recipy search -a --outputs newplot
    Will look through outputs of all runs and try to find a file containing
    newplot in its name.
    """
    click.echo('Searching...')
