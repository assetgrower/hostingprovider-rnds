#!/usr/bin/env python3
"""
Script to match hostnames in hosts.log against regexes in providers.csv,
showing which hosts match which provider and which hosts don't match any.
"""

import re
import csv
import argparse
import sys


def load_providers(csv_file):
    providers = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pattern = row.get('PTR PCRE Regex')
            if not pattern:
                continue
            try:
                regex = re.compile(pattern)
            except re.error as e:
                print(f"Invalid regex for provider {row.get('Provider')}: {e}", file=sys.stderr)
                continue
            providers.append((row.get('Provider'), regex))
    return providers


def load_hosts(hosts_file):
    with open(hosts_file) as f:
        return [line.strip() for line in f if line.strip()]


def main():
    parser = argparse.ArgumentParser(
        description="Match hostnames against provider regexes"
    )
    parser.add_argument(
        'csv', nargs='?', default='providers.csv',
        help="Path to providers CSV file"
    )
    parser.add_argument(
        'hosts', nargs='?', default='hosts.log',
        help="Path to hosts log file"
    )
    args = parser.parse_args()

    providers = load_providers(args.csv)
    hosts = load_hosts(args.hosts)

    matched = {}
    unmatched = []

    for host in hosts:
        found = False
        for provider, regex in providers:
            if regex.match(host):
                matched.setdefault(provider, []).append(host)
                found = True
                break
        if not found:
            unmatched.append(host)

    # Print matches
    print("Matches:")
    for provider, hs in matched.items():
        for h in hs:
            print(f"{h} => {provider}")
    # Print unmatched
    if unmatched:
        print("\nUnmatched:")
        for h in unmatched:
            print(h)


if __name__ == '__main__':
