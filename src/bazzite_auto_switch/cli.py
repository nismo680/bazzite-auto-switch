from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="bazzite-auto-switch",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "list",
        help="List detected GPUs and connectors.",
    )

    args = parser.parse_args()

    if args.command == "list":
        return cmd_list()

    return 1


def cmd_list() -> int:
    print("Not implemented yet.")
    return 0
