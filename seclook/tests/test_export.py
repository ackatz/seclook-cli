from click.testing import CliRunner
from seclook.cli import main


def test_export():
    runner = CliRunner()
    result = runner.invoke(main, ["threatfox", "1.1.1.1", "--export"])
    assert "Results exported to" in result.output
