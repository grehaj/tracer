"""
    This module provides ...
"""

import os
import sys

from ssh.ssh_credentials import SSHCredentials

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        print(f"Error: Missing environment variable: {name}")
        sys.exit(1)
    return value

audit_host = get_env_var("AUDIT_HOSTNAME")
audit_username = get_env_var("AUDIT_USERNAME")
audit_password = get_env_var("AUDIT_PASSWORD")
trace_host = get_env_var("TRACE_HOSTNAME")
trace_username = get_env_var("TRACE_USERNAME")
trace_password = get_env_var("TRACE_PASSWORD")

class ConfigManager:
    def __init__(self, host_name):
        self.auditor_host_credentials = SSHCredentials(host=audit_host, username=audit_username, password=audit_password)
        self.trace_host_credentials = SSHCredentials(host=trace_host, username=trace_username, password=trace_password)

    def get_auditor_host_credentials(self):
        return self.auditor_host_credentials

    def get_trace_host_credentials(self):
        return self.trace_host_credentials
