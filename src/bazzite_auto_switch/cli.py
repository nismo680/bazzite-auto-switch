from __future__ import annotations

import argparse

import bazzite_auto_switch.commands.list as list_command


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
        return list_command.run()

    return 1
