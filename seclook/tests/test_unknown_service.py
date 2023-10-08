from click.testing import CliRunner
from seclook.cli import main


def test_unknown_service():
    runner = CliRunner()
    result = runner.invoke(main, ["unknown", "value"])
    assert result.exit_code != 0
    assert "is not available in seclook" in result.output
