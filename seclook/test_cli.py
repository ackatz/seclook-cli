import pytest
from click.testing import CliRunner
from seclook.cli import main


def test_list_services():
    runner = CliRunner()
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0
    assert "Available services:" in result.output


def test_missing_service_and_value():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code != 0
    assert "Error: Missing service argument." in result.output


def test_shodan_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["shodan"])
    assert result.exit_code != 0
    assert "Error: Missing value argument for service 'shodan'." in result.output


def test_virustotal_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["virustotal"])
    assert result.exit_code != 0
    assert "Error: Missing value argument for service 'virustotal'." in result.output


def test_emailrep_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["emailrep"])
    assert result.exit_code != 0
    assert "Error: Missing value argument for service 'emailrep'." in result.output


def test_abuseipdb_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["abuseipdb"])
    assert result.exit_code != 0
    assert "Error: Missing value argument for service 'abuseipdb'." in result.output


def test_unknown_service():
    runner = CliRunner()
    result = runner.invoke(main, ["unknown", "value"])
    assert result.exit_code != 0
    assert "is not available in seclook" in result.output


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
    result = runner.invoke(main, ["emailrep", "andrew@akatz.org"])
    assert result.exit_code == 0


def test_abuseipdb_valid_value():
    runner = CliRunner()
    result = runner.invoke(main, ["abuseipdb", "1.1.1.1"])
    assert result.exit_code == 0
