"""
    Module for parsing cmd arguments.
"""

import argparse

from dataclasses import dataclass
from typing import Optional


@dataclass
class CmdArguments:
    host_name: str
    log_type: str
    mode: Optional[str] = None
    on_failure: Optional[str] = None


def get_cmd_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host_name",
        required=True,
        help="Name of the host"
    )
    parser.add_argument(
        "--type",
        required=True,
        nargs="+",
        choices=["d", "n", "o"],
        help="Type of logs: ['d', 'n', 'o']",
    )
    parser.add_argument(
        "--mode",
        required=False,
        choices=["pre_failure", "post_failure"],
        help="Log collection mode: ['pre_failure', 'post_failure']",
    )
    parser.add_argument(
        "--on_failure",
        required=False,
        choices=["stop", "continue"],
        help="Action after failure: ['stop', 'continue']",
    )
    args = parser.parse_args()

    return CmdArguments(
        args.host_name,
        args.type,
        args.mode,
        args.on_failure
    )