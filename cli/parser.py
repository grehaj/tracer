"""
    Module for parsing cmd arguments.
"""

import argparse


def get_cli_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--host_name",
        required=True,
        help="Name of the host on which logs will be collected."
    )

    parser.add_argument(
        "--user_name",
        required=True,
        help="User name used to ssh the remote host."
    )

    parser.add_argument(
        "--password",
        required=True,
        help="Password used to ssh the remote host."
    )

    parser.add_argument(
        "--interface",
        required=True,
        help="Interface to collect logs from."
    )

    parser.add_argument(
        "--local_log_dir",
        required=True,
        help="Location where logs will be copied after hitting the error."
    )

    parser.add_argument(
        "--remote_log_dir",
        required=True,
        help="Location where logs will be temporary stored on the remote host."
    )

    parser.add_argument(
        "--monitored_file",
        required=True,
        help="A file where monitored_log will be searched."
    )

    parser.add_argument(
        "--monitored_log",
        required=True,
        help="A string literal which will be searched in the monitored_log."
    )

    return parser.parse_args()
