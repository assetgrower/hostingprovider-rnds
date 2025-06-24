# Reverse DNS PTR Signature Regexes

This project maintains a collection of reverse DNS (PTR) signature regular expressions
for various hosting providers and services. It enables matching PTR records to known
providers using PCRE-compatible patterns.

## Files

- `match_providers.py`: Script to match hostnames in a hosts log against regexes in `providers.csv`, showing which hosts match which provider and which hosts don't match any.
- `providers.csv`: The primary dataset of approved provider PTR signatures with columns:
  - `Provider`: Friendly name of the hosting provider or service.
  - `PTR`: Example real-world PTR record.
  - `Provider Domain`: Base domain suffix for reverse DNS (e.g., `amazonaws.com`).
  - `PTR PCRE Regex`: PCRE regex pattern to validate matching PTR records.
  - `Verification URL`: Reference URL for how to configure or verify reverse DNS.

