# api-uptime-monitoring-tool

A small Python CLI that reads a JSON list of URLs, performs HTTP GET checks with a 10 second timeout, and prints per-target status and latency as JSON.

## Key features

- Reads targets from a JSON file
- Reports HTTP status codes and latency in milliseconds
- Returns structured JSON suitable for piping into other tooling
- Falls back to an error object when a request fails

## Project structure

- `monitor.py` — CLI entrypoint that performs the checks
- `requirements.txt` — Dependency file (currently empty because the script uses the standard library only)

## Requirements

- Python 3.9+
- Outbound network access to the target URLs

## Setup

```bash
git clone https://github.com/biprajit007/api-uptime-monitoring-tool.git
cd api-uptime-monitoring-tool
```

## Usage

### targets.json

```bash
["https://example.com", "https://httpbin.org/status/200"]
```

### Run the monitor

```bash
python3 monitor.py targets.json
```

## Sample output

```text
[
  {
    "url": "https://example.com",
    "status": 200,
    "latency_ms": 143.21
  }
]
```

## Notes

- The script performs one pass only; it is not a daemon or scheduler.
- It does not retry failed requests or persist results.

## Limitations / next improvements

- No concurrency or retry logic
- No authentication, headers, or method selection
- JSON input must be a simple array of URL strings
