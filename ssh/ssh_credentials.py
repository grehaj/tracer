"""
    This module provides ...
"""

from dataclasses import dataclass

@dataclass
class SSHCredentials:
    user_name: str
    password: str

@dataclass
class SSHHost:
    host_name: str
    credentials: SSHCredentials