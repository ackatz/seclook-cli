from click.testing import CliRunner
from seclook.cli import main


def test_list():
    runner = CliRunner()
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0
    assert "Available services:" in result.output
