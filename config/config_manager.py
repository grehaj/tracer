"""
    This module provides ...
"""

import os
import sys
from dataclasses import dataclass

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        print(f"Error: Missing environment variable: {name}")
        sys.exit(1)
    return value

host = get_env_var("HOSTNAME")
username = get_env_var("USERNAME")
password = get_env_var("PASSWORD")

@dataclass
class SSHCredentials:
    host: str
    username: str
    password: str

class ConfigManager:
    def __init__(self, host_name):
        self.auditor_host_credentials = SSHCredentials(host=host, username=username, password=password)
        self.trace_host_credentials = SSHCredentials(host=host, username=username, password=password)

    def get_auditor_host_credentials(self):
        return self.auditor_host_credentials

    def get_trace_host_credentials(self):
        return self.trace_host_credentials
