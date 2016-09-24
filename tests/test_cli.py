import pytest
from click.testing import CliRunner
from recipy import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'Hello, world.'


def test_cli_with_option(runner):
    result = runner.invoke(cli.main, ['--count=2'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'Hello, world.\nHello, world.'


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['Jan'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, Jan.'
