#!/usr/bin/env python3

import click
from seclook.lookups import (
    shodan_lookup,
    virustotal_lookup,
    emailrep_lookup,
    abuseipdb_lookup,
    greynoise_lookup,
    threatfox_lookup,
)
import json
import os


@click.command()
@click.argument("service", required=False)
@click.argument("value", required=False)
@click.option("--export", is_flag=True, help="Export JSON to Desktop")
def main(service, value, export):
    """Perform lookups from various security services

    - Use `seclook [service] [value]` to perform a lookup.

    - Use `seclook list` to see a list of available services.
    """

    if not service:
        raise click.UsageError("Missing service argument.")

    # If service doesn't exist, print an error message
    if service.lower() not in [
        "list",
        "shodan",
        "virustotal",
        "emailrep",
        "abuseipdb",
        "greynoise",
        "threatfox",
    ]:
        raise click.UsageError(f"'{service}'a is not available in seclook.")

    # Special service name to list available services
    if service.lower() == "list":
        services = [
            "- Shodan",
            "- VirusTotal",
            "- Emailrep",
            "- AbuseIPDB",
            "- GreyNoise",
            "- ThreatFox",
        ]
        click.echo("Available services:")
        for service in services:
            click.echo(service)
        click.echo("Run 'seclook [service] [value]' to perform a lookup.")
        return

    # If value is not provided for a service lookup, print an error message
    if not value:
        raise click.UsageError(f"Missing value argument for '{service}'.")

    if service.lower() == "shodan":
        result = shodan_lookup.search(value)
    elif service.lower() == "virustotal":
        result = virustotal_lookup.search(value)
    elif service.lower() == "emailrep":
        result = emailrep_lookup.search(value)
    elif service.lower() == "abuseipdb":
        result = abuseipdb_lookup.search(value)
    elif service.lower() == "greynoise":
        result = greynoise_lookup.search(value)
    elif service.lower() == "threatfox":
        result = threatfox_lookup.search(value)
    else:
        raise click.UsageError("Unknown service.")

    # If export flag is set, save to a JSON file on the desktop
    if export:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        filename = os.path.join(desktop, f"seclook_{service}_{value}.json")

        with open(filename, "w") as outfile:
            json.dump(result, outfile, indent=4)

        click.echo(f"Results exported to {filename}")
        return

    # Pretty print the result
    pretty_result = json.dumps(result, indent=4)
    click.echo(pretty_result)


if __name__ == "__main__":
    main()
