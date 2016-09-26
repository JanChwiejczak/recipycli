import pytest
from click.testing import CliRunner
from recipy import cmd_gui


@pytest.fixture
def runner():
    return CliRunner()


def test_search_with_only_filename(runner):
    result = runner.invoke(cmd_gui.cmd)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Starting GUI...'
