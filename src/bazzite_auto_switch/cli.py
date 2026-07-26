from __future__ import annotations

import argparse

import bazzite_auto_switch.commands.list as list_command
import bazzite_auto_switch.commands.setup_displays as setup_displays
import bazzite_auto_switch.commands.setup_mode as setup_mode
import bazzite_auto_switch.commands.show_config as show_config


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

    setup_parser = subparsers.add_parser(
        "setup",
        help="Setup configuration.",
    )

    setup_subparsers = setup_parser.add_subparsers(
        dest="setup_command",
    )

    setup_subparsers.add_parser(
        "displays",
        help="Configure displays.",
    )

    setup_subparsers.add_parser(
        "mode",
        help="Configure mode priority.",
    )

    show_parser = subparsers.add_parser(
        "show",
        help="Show information.",
    )

    show_subparsers = show_parser.add_subparsers(
        dest="show_command",
    )

    show_subparsers.add_parser(
        "config",
        help="Show configuration.",
    )

    # Parser
    args = parser.parse_args()

    # Dispatch
    if args.command == "list":
        return list_command.run()

    if args.command == "setup":
        if args.setup_command is None:
            setup_parser.print_help()
            return 0

        if args.setup_command == "displays":
            return setup_displays.run()

        if args.setup_command == "mode":
            return setup_mode.run()

    if args.command == "show":
        if args.show_command is None:
            show_parser.print_help()
            return 0

        if args.show_command == "config":
            return show_config.run()

    return 1
