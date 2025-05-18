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

    def has_critical_error(self):
        return self.error_type == ErrorType.CRITICAL

    def has_error(self):
        return self.error_type == ErrorType.ERROR

    def has_warning(self):
        return self.error_type == ErrorType.WARNING

class Auditor:
    def __init__(self, credentials, crash, ids):
        self.credentials = credentials
        self.crash=crash
        self.ids = ids

    def run_audit(self):
        result = ssh_run_command(ssh_credentials=self.credentials, cmd='grep -i -a -A 1 crash var/log/crash.log').strip()
        if self.crash in result:
            print("Crash detected.")
            for i in range(self.ids[0], self.ids[1] + 1):
                if str(i) in result:
                    print(f"Desired crash detected for id: {i}.")
                    return ErrorData(error_type=ErrorType.CRITICAL)
            print(f"Crash found but for other id: {result}.")
            return ErrorData(error_type=ErrorType.ERROR)
        else:
            print("Other crash found.")
            return ErrorData(error_type=ErrorType.WARNING)

        print("No crash so far.")
        return ErrorData(error_type=ErrorType.INFO)

