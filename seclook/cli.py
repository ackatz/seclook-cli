#!/usr/bin/env python3
import click
from seclook.lookups import (\
    quick_lookup,
    shodan_lookup,
    virustotal_lookup,
    emailrep_lookup,
    abuseipdb_lookup,
    greynoise_lookup,
    threatfox_lookup,
    pulsedive_lookup,
    yaraify_lookup,
)
import json
import os

@click.command()
@click.argument("service", required=False)
@click.argument("value", required=False)
@click.option("--export", is_flag=True, help="Export JSON to current working directory.")
def main(service, value, export):
    """Perform lookups from various security services
    - Use `seclook [service] [value]` to perform a lookup.
    - Use `seclook list` to see a list of available services.
    """
    services = [
        "list",  # Keep at top, so services.pop(0) always removes it
        "quick",
        "shodan",
        "virustotal",
        "emailrep",
        "abuseipdb",
        "greynoise",
        "threatfox",
        "pulsedive",
        "yaraify"
    ]
    if not service:
        raise click.UsageError("Missing service argument.")
    if service.lower() not in services:
        raise click.UsageError(f"'{service}' is not available in seclook.")
    if service.lower() == "list":
        services.pop(0)  # Remove 'list' from the list
        click.echo("Available services:")
        for service in services:
            click.echo("- " + service.capitalize())
        click.echo("Run 'seclook [service] [value]' to perform a lookup.")
        return
    if not value:
        raise click.UsageError(f"Missing value argument for '{service}'.")
    if service.lower() == "quick":
        result = quick_lookup.search(value)
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
    elif service.lower() == "pulsedive":
        result = pulsedive_lookup.search(value)
    elif service.lower() == "yaraify":
        result = yaraify_lookup.search(value)

    if export:
        # Use current working directory for exports
        cwd = os.getcwd()
        filename = os.path.join(cwd, f"seclook_{service}_{value}.json")
        with open(filename, "w") as outfile:
            json.dump(result, outfile, indent=2)
        click.echo(f"Results exported to {filename}")
    else:
        click.echo(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()