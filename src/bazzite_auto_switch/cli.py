from __future__ import annotations

import argparse

import bazzite_auto_switch.commands.list as list_command
import bazzite_auto_switch.commands.setup_displays as setup_displays
import bazzite_auto_switch.commands.setup_mode as setup_mode


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

    setup_parser = subparsers.add_parser(
        "setup",
        help="Setup configuration.",
    )

    setup_subparsers = setup_parser.add_subparsers(
        dest="setup_command",
        required=True,
    )

    setup_subparsers.add_parser(
        "mode",
        help="Configure mode priority.",
    )

    setup_subparsers.add_parser(
        "displays",
        help="Configure displays.",
    )

    if args.command == "list":
        return list_command.run()

    if args.command == "setup":
        if args.setup_command == "mode":
            return setup_mode.run()

        if args.setup_command == "displays":
            return setup_displays.run()

    return 1
