[![Tests](https://github.com/ackatz/seclook/actions/workflows/ci.yml/badge.svg)](https://github.com/ackatz/seclook/actions/workflows/ci.yml)
[![Release](https://github.com/ackatz/seclook/actions/workflows/cd.yml/badge.svg)](https://github.com/ackatz/seclook/actions/workflows/cd.yml)
[![Downloads](https://static.pepy.tech/badge/seclook)](https://pepy.tech/project/seclook)

# seclook

`seclook` is a security lookup CLI tool that allows you to query various security services on the fly. It is essentially a wrapper over the `requests` library that removes the need to manually search within Web UIs or write your own requests in Postman or cURL to query these services.

You can look up information using commands like `seclook [service] [value]`, where the service can be `virustotal`, `shodan`, `emailrep`, and so on. The value is the information you're querying for and varies by service.

## Installation

1. `pip install seclook`
2. Copy [config.ini.sample](https://github.com/ackatz/seclook/blob/main/config.ini.sample) from this directory and place it in `~/.seclook/config.ini`
3. Open `~/.seclook/config.ini` and add in your own API keys for the services you want to use. 

> Some services (e.g., GreyNoise, ThreatFox) _don't require API keys_, but may be rate-limited more quickly without one or have other limitations. Others (e.g., YARAify) do not need an API key at all and will not be referenced in the config file.

## Usage

Basic usage of `seclook` is as follows:

```bash
seclook [service] [value]
```

For example, to look up IP 1.1.1.1 on AbuseIPDB, you'd run:

```bash
seclook abuseipdb 1.1.1.1
```

You can send the JSON response to OpenAI GPT-4 for summarization:

```bash
seclook virustotal 44d88612fea8a8f36de82e1278abb02f --gpt4
```

You can pipe the output to `fx` or `jq` for further processing:

```bash
seclook emailrep andrew@akatz.org | fx
```

You can `grep` the output for known keys to get specific information:

```bash
seclook virustotal 44d88612fea8a8f36de82e1278abb02f | grep malicious
```

## Options

`--export` – Use this flag to export the results to a JSON file on your Desktop.  
`--gpt4` – Use this flag to summarize the JSON response from a service in GPT4.

## Supported services

- [x] [VirusTotal](https://virustotal.com/)
- [x] [Shodan](https://www.shodan.io/)
- [x] [Emailrep](https://emailrep.io/)
- [x] [AbuseIPDB](https://www.abuseipdb.com/)
- [x] [GreyNoise](https://www.greynoise.io/)
- [x] [ThreatFox](https://threatfox.abuse.ch/)
- [x] [Pulsedive](https://pulsedive.com/)
- [x] [Yaraify](https://yaraify.abuse.ch/)

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



