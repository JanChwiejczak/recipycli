import pytest
from click.testing import CliRunner
from recipy import cmd_annotate


@pytest.fixture
def runner():
    return CliRunner()


def test_tag_with_no_arguments_annotates_last_run(runner):
    result = runner.invoke(cmd_annotate.cmd)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Added Note...'
