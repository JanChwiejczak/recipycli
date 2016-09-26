import os
import sys
import click


class CliConfig(object):
    """Passes configuration between commands."""
    def __init__(self):
        self.debug = False

pass_config = click.make_pass_decorator(CliConfig, ensure=True)
cmd_folder = os.path.dirname(__file__)


class CLI(click.MultiCommand):
    """Implements MultiCommand click class methods to find other
    commands in the cmd_folder. Command files must be in
    format cmd_COMMANDNAME.py"""

    def list_commands(self, ctx):
        cmd = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                cmd.append(filename[4:-3])
        cmd.sort()
        return cmd

    def get_command(self, ctx, cmd_name):
        try:
            if sys.version_info[0] == 2:
                cmd_name = cmd_name.encode('ascii', 'replace')
            mod = __import__('recipy.cmd_' + cmd_name, fromlist=['cmd'])
        except ImportError:
            return
        return mod.cmd


@click.command(cls=CLI)
@click.version_option(version='0.1.0')
@click.option('--debug', is_flag=True,
              help='Show debug info while running command.')
@pass_config
def main(config, debug):
    """Frictionless provenance tracking in Python.
    For more info type: recipy COMMAND --help"""
    config.debug = debug
    if config.debug:
        click.echo('Debug info...')
