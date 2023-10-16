from click.testing import CliRunner
from seclook.cli import main


def test_threatfox_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["threatfox"])
    assert result.exit_code != 0
    assert "Missing value argument for 'threatfox'." in result.output


def test_yaraify_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["yaraify"])
    assert result.exit_code != 0
    assert "Missing value argument for 'yaraify'." in result.output


def test_pulsedive_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["pulsedive"])
    assert result.exit_code != 0
    assert "Missing value argument for 'pulsedive'." in result.output


def test_shodan_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["shodan"])
    assert result.exit_code != 0
    assert "Missing value argument for 'shodan'." in result.output


def test_virustotal_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["virustotal"])
    assert result.exit_code != 0
    assert "Missing value argument for 'virustotal'." in result.output


def test_emailrep_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["emailrep"])
    assert result.exit_code != 0
    assert "Missing value argument for 'emailrep'." in result.output


def test_abuseipdb_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["abuseipdb"])
    assert result.exit_code != 0
    assert "Missing value argument for 'abuseipdb'." in result.output


def test_greynoise_missing_value():
    runner = CliRunner()
    result = runner.invoke(main, ["greynoise"])
    assert result.exit_code != 0
    assert "Missing value argument for 'greynoise'." in result.output
