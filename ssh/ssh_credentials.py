"""
    This module provides ...
"""

from dataclasses import dataclass

@dataclass
class SSHCredentials:
    host: str
    username: str
    password: str