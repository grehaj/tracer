"""
    This module provides ...
"""

import paramiko


def ssh_run_command(host, username, password, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print("Output:\n", stdout.read().decode())
        print("Errors:\n", stderr.read().decode())
    finally:
        ssh.close()