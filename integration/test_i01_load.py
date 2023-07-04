import pytest
from click.testing import CliRunner

from dundie.cli import load, main
from dundie.utils.log import get_logger
from tests.constants import PEOPLE_FILE

cmd = CliRunner()
log = get_logger()


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """test command load"""
    out = cmd.invoke(load, [PEOPLE_FILE])
    assert "Dunder Mifflin Associates" in out.output
    assert out.exit_code == 0


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "run", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    out = cmd.invoke(main, [wrong_command, PEOPLE_FILE])
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
