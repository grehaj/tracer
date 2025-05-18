"""
    Module for parsing cmd arguments
"""

import argparse

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host_name", required=True, help="Name of the host")
    parser.add_argument("--crash", required=True, help="Name of the host")
    parser.add_argument(
        "--ids",
        nargs='+',
        type=int,
        help="A list of numbers",
        required=True
    )

    return parser