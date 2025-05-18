"""
    This module provides ...
"""

from ssh.ssh_command import ssh_run_jumped_command

class Tracer:
    def __init__(self, jump_host_ssh_credentials, target_host_ssh_credentials):
        self.jump_host_ssh_credentials = jump_host_ssh_credentials
        self.target_host_ssh_credentials = target_host_ssh_credentials

    def start(self):
        result = ssh_run_jumped_command(jump_host_ssh_credentials=self.jump_host_ssh_credentials,
                                        target_host_ssh_credentials=self.target_host_ssh_credentials,
                                        cmd='echo "Starting traces on $HOSTNAME"').strip()
        print(result)

    def stop(self):
        result = ssh_run_jumped_command(jump_host_ssh_credentials=self.jump_host_ssh_credentials,
                                        target_host_ssh_credentials=self.target_host_ssh_credentials,
                                        cmd='echo "Stopping traces on $HOSTNAME"').strip()
        print(result)
