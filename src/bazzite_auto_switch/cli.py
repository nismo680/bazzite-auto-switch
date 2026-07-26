from __future__ import annotations

import argparse

import bazzite_auto_switch.commands.list as list_command
import bazzite_auto_switch.commands.setup as setup_command


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

    subparsers.add_parser(
        "setup",
        help="Configure displays.",
    )

    args = parser.parse_args()

    if args.command == "list":
        return list_command.run()

    if args.command == "setup":
        return setup_command.run()

    return 1
