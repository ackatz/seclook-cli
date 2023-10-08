from click.testing import CliRunner
from seclook.cli import main


def test_missing_service_and_value():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code != 0
    assert "Error: Missing service argument." in result.output
