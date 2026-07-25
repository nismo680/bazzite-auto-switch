import argparse

from .version import __version__


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bazzite-auto-switch",
        description="Automatic session switching for Bazzite.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.parse_args()

    print("Bazzite Auto Switch")
