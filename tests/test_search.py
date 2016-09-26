import pytest
from click.testing import CliRunner
from recipy import cmd_search


@pytest.fixture
def runner():
    return CliRunner()


def test_search_without_valid_filename_raises_error(runner):
    result = runner.invoke(cmd_search.cmd)
    assert result.exception
    assert result.exit_code == 2
    assert 'Error' in result.output.strip()


def test_search_with_only_filename(runner):
    result = runner.invoke(cmd_search.cmd, ['README.md'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Searching...'
