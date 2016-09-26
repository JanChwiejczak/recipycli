import pytest
from click.testing import CliRunner
from recipy import cmd_latest


@pytest.fixture
def runner():
    return CliRunner()


def test_latest_returns_last_run(runner):
    result = runner.invoke(cmd_latest.cmd)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Latest Run...'
