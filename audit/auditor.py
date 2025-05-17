"""
    This module provides ...
"""

from enum import Enum
from ssh.ssh_command import ssh_run_command

class ErrorType(Enum):
    """
    Enum representing severity levels for logging or error reporting.
    """
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class ErrorData:
    def __init__(self, error_type: ErrorType):
        self.error_type = error_type

    def has_error(self):
        return self.error_type == ErrorType.CRITICAL

class Auditor:
    def __init__(self, credentials):
        self.credentials = credentials

    def run_audit(self):
        ssh_run_command(host=self.credentials.host, username=self.credentials.username,
                        password=self.credentials.password,
                        cmd='echo "Running audit on $HOSTNAME"')
        return ErrorData(error_type=ErrorType.CRITICAL)

