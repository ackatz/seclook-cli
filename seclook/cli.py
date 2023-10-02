#!/usr/bin/env python3

import click
from seclook.lookups import shodan_lookup, virustotal_lookup
from seclook.lookups import emailrep_lookup
import json
import os


@click.command()
@click.argument("service")
@click.argument("value")
@click.option(
    "--export", is_flag=True, help="Export results to a JSON file on the desktop"
)
def main(service, value, export):
    """Perform lookups from various security services"""

    result = None

    if service.lower() == "shodan":
        result = shodan_lookup.search(value)
    elif service.lower() == "virustotal":
        result = virustotal_lookup.search(value)
    elif service.lower() == "emailrep":
        result = emailrep_lookup.search(value)
    else:
        click.echo("Unknown service")
        return

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
