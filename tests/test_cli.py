import pytest
from click.testing import CliRunner
from recipy import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_main_correctly_passes_config(runner):
    result = runner.invoke(cli.main,
                           ['--debug', 'latest'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'Debug info...' in result.output
