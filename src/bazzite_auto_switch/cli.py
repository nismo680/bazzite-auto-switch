from __future__ import annotations

import argparse

import bazzite_auto_switch.commands.disable as disable
import bazzite_auto_switch.commands.enable as enable
import bazzite_auto_switch.commands.list as list_command
import bazzite_auto_switch.commands.setup_displays as setup_displays
import bazzite_auto_switch.commands.setup_settings as setup_settings
import bazzite_auto_switch.commands.show_config as show_config
import bazzite_auto_switch.commands.status as status
import bazzite_auto_switch.daemon as daemon


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
        "settings",
        help="Configure settings.",
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

    subparsers.add_parser(
        "install",
        help="Install the systemd user service.",
    )

    subparsers.add_parser(
        "uninstall",
        help="Remove the systemd user service.",
    )

    args = parser.parse_args()

    if args.command == "list":
        return list_command.run()

    if args.command == "setup":
        if args.setup_command is None:
            setup_parser.print_help()
            return 0

        if args.setup_command == "displays":
            return setup_displays.run()

        if args.setup_command == "settings":
            return setup_settings.run()

    if args.command == "show":
        if args.show_command is None:
            show_parser.print_help()
            return 0

        if args.show_command == "config":
            return show_config.run()

    if args.command == "status":
        return status.run()

    if args.command == "enable":
        return enable.run()

    if args.command == "disable":
        return disable.run()

    if args.command == "daemon":
        return daemon.run()

    if args.command == "install":
        raise NotImplementedError

    if args.command == "uninstall":
        raise NotImplementedError

    return 1
