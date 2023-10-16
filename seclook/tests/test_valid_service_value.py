from click.testing import CliRunner
from seclook.cli import main


def test_threatfox_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["threatfox", "1.1.1.1"])
    assert result.exit_code == 0


def test_yaraify_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["yaraify", "asdf"])
    assert result.exit_code == 0


def test_pulsedive_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["pulsedive", "1.1.1.1"])
    assert result.exit_code == 0


def test_shodan_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["shodan", "1.1.1.1"])
    assert result.exit_code == 0


def test_virustotal_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["virustotal", "1.1.1.1"])
    assert result.exit_code == 0


def test_emailrep_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["emailrep", "example@example.org"])
    assert result.exit_code == 0


def test_abuseipdb_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["abuseipdb", "1.1.1.1"])
    assert result.exit_code == 0


def test_greynoise_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["greynoise", "1.1.1.1"])
    assert result.exit_code == 0
