# seclook

`seclook` is a security lookup CLI tool that allows you to query various security services on the fly. You can look up information using commands like `seclook [service] [value]`, where service can be `virustotal`, `shodan`, `emailrep` etc., and value is the information you're querying for.

## Installation

1. `pip install seclook`
2. Copy `config.ini.sample` to `~/.seclook/config.ini`.
3. Edit `~/.seclook/config.ini` with your own API keys.

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
- [ ] [AlienVault OTX](https://otx.alienvault.com/) (Planned)
- [ ] [AbuseIPDB](https://www.abuseipdb.com/) (Planned)
- [ ] [GreyNoise](https://www.greynoise.io/) (Planned)

## Contributing

If you'd like to contribute to seclook, please feel free to fork the repository, create a feature branch, and then submit a Pull Request.

## License

MIT License

## Contact

[andrew@akatz.org](mailto:andrew@akatz.org)



