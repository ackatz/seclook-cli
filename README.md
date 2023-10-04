[![Tests](https://github.com/ackatz/seclook/actions/workflows/ci.yml/badge.svg)](https://github.com/ackatz/seclook/actions/workflows/ci.yml)
[![Release](https://github.com/ackatz/seclook/actions/workflows/cd.yml/badge.svg)](https://github.com/ackatz/seclook/actions/workflows/cd.yml)

# seclook

`seclook` is a security lookup CLI tool that allows you to query various security services on the fly. It is essentially a wrapper over the `requests` library that removes the need to manually search within Web UIs or write your own requests in Postman or cURL to query these services.

You can look up information using commands like `seclook [service] [value]`, where the service can be `virustotal`, `shodan`, `emailrep`, and so on. The value is the information you're querying for and varies by service.

## Installation

1. `pip install seclook`
2. Copy [config.ini.sample](https://github.com/ackatz/seclook/blob/main/config.ini.sample) from this directory and place it in `~/.seclook/config.ini`
3. Open `~/.seclook/config.ini` and add in your own API keys for the services you want to use. 

> Some services (e.g., GreyNoise, ThreatFox) _don't require API keys_, but may be rate-limited more quickly without one or have other limitations.

## Usage

Basic usage of `seclook` is as follows:

```bash
seclook [service] [value]
```

For example, to look up IP 1.1.1.1 on VirusTotal, you'd run:

```bash
seclook virustotal 1.1.1.1
```

You can pipe the output to `jq` or `fx` for further processing:

```bash
seclook virustotal 1.1.1.1 | jq
```

You can `grep` the output for known keys to get specific information:

```bash
seclook virustotal 1.1.1.1 | grep malicious
``` 

## Options

`--export` – Use this flag to export the results to a JSON file on your Desktop.

## Supported services

- [x] [VirusTotal](https://virustotal.com/)
- [x] [Shodan](https://www.shodan.io/)
- [x] [Emailrep](https://emailrep.io/)
- [x] [AbuseIPDB](https://www.abuseipdb.com/)
- [x] [GreyNoise](https://www.greynoise.io/)
- [x] [ThreatFox](https://threatfox.abuse.ch/)

You can also view supported services by passing `list` as the service name:

```bash 
seclook list
```

## Upgrading

To upgrade seclook to the latest version:

```bash
pip install --upgrade seclook
```

## Contributing

If you'd like to contribute to seclook, please feel free to fork the repository, create a feature branch, and then submit a Pull Request.

## License

MIT License

## Contact

[andrew@akatz.org](mailto:andrew@akatz.org)



