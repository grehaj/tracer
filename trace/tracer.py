"""
    This module provides ...
"""

from ssh.ssh_command import ssh_run_command

class Tracer:
    def __init__(self, credentials):
        self.credentials = credentials

    def start(self):
        ssh_run_command(host=self.credentials.host, username=self.credentials.username, password=self.credentials.password,
                        cmd='echo "Starting traces on $HOSTNAME"')

    def stop(self):
        ssh_run_command(host=self.credentials.host, username=self.credentials.username,
                        password=self.credentials.password,
                        cmd='echo "Stopping traces on $HOSTNAME"')
