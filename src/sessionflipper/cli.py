from __future__ import annotations

import argparse

import sessionflipper.commands.config as config
import sessionflipper.commands.disable as disable
import sessionflipper.commands.displays as displays
import sessionflipper.commands.enable as enable
import sessionflipper.commands.list as list_command
import sessionflipper.commands.settings as settings
import sessionflipper.commands.status as status
import sessionflipper.daemon as daemon


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="sessionflipper",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Show detailed debug output.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    subparsers.add_parser(
        "list",
        help="List detected GPUs and connectors.",
    )

    subparsers.add_parser(
        "displays",
        help="Configure displays.",
    )

    subparsers.add_parser(
        "settings",
        help="Configure settings.",
    )

    subparsers.add_parser(
        "config",
        help="Show configuration.",
    )

    subparsers.add_parser(
        "status",
        help="Show current status.",
    )

    subparsers.add_parser(
        "enable",
        help="Enable automatic switching.",
    )

    subparsers.add_parser(
        "disable",
        help="Disable automatic switching.",
    )

    subparsers.add_parser(
        "daemon",
        help="Run display event daemon.",
    )

    args = parser.parse_args()

    if args.command is None:
        return daemon.run(
            debug=args.debug,
            run_once=True,
        )

    if args.command == "list":
        return list_command.run()

    if args.command == "displays":
        return displays.run()

    if args.command == "settings":
        return settings.run()

    if args.command == "config":
        return config.run()

    if args.command == "status":
        return status.run()

    if args.command == "enable":
        return enable.run()

    if args.command == "disable":
        return disable.run()

    if args.command == "daemon":
        return daemon.run(
            debug=args.debug,
        )

    return 1
