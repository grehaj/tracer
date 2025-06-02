"""
    This module provides ...
"""

from enum import Enum
from abc import ABC, abstractmethod

from ssh.ssh_command import ssh_run_fg_command

class ErrorType(Enum):
    """
    Enum representing severity levels for logging or error reporting.
    """
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class ErrorData:
    def __init__(self, error_type: ErrorType):
        self.error_type = error_type

    def has_error(self):
        return self.error_type == ErrorType.ERROR

    def has_warning(self):
        return self.error_type == ErrorType.WARNING

class Auditor(ABC):
    @abstractmethod
    def run_audit(self):
        pass

class LogAuditor(Auditor):
    def __init__(self, monitored_host, monitored_file, monitored_log):
        self.monitored_host = monitored_host
        self.monitored_file = monitored_file
        self.monitored_log = monitored_log

    def run_audit(self):
        result = ssh_run_fg_command(
            host=self.monitored_host,
            command=f'grep -i -a -A 1 {self.monitored_log} {self.monitored_file}'
        ).strip()
        if len(result) > 0:
            return ErrorData(error_type=ErrorType.ERROR)

        print("No crash so far.")
        return ErrorData(error_type=ErrorType.INFO)

