import click
from recipy.cli import pass_config


@click.command('search', short_help='Find run with this file.')
@click.option('--exact', '-e', is_flag=True,
              help='Match FILENAME exactly.')
@click.option('--id', '-i', is_flag=True,
              help='Match based on a fragment of run id.')
@click.option('--filepath', '-f', is_flag=True,
              help='Match all files from the same directory as FILENAME.')
@click.option('--all', '-a', is_flag=True, help='Return all results.')
@click.option('--json', '-j', is_flag=True, help='Return results as JSON.')
@click.option('--inputs', is_flag=True, help='Restrict search to run inputs only.')
@click.option('--outputs', is_flag=True, help='Restrict search to run outputs only.')
@click.argument('filename', required=True)
@pass_config
def cmd(config, exact, id, filepath, all, json, filename, inputs, outputs):
    """Search for FILENAME or part of it in outputs and inputs of all runs
    recorded by ReciPy. You can use regular expressions in FILENAME.
    By default it only returns the most recent result.

    \b
    For example: recipy search -a --outputs new_plot
    Will find all runs which outputs had a file containing
    new_plot in its name.
    """
    click.echo('Searching...')
