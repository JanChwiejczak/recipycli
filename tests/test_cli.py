import pytest
from click.testing import CliRunner
from recipy import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_search_without_valid_filename_raises_error(runner):
    result = runner.invoke(cli.search)
    assert result.exception
    assert result.exit_code == 2
    assert 'Error' in result.output.strip()


def test_search_with_only_filename(runner):
    result = runner.invoke(cli.search, ['README.md'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Searching...'


def test_main_correctly_passes_debug(runner):
    result = runner.invoke(cli.main,
                           ['--debug', 'search', 'README.md'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'Debug info...' in result.output
