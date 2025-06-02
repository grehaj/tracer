"""
    This module provides ...
"""

import socket
import paramiko


class RemoteCommandError(Exception):
    def __init__(self, command, stderr):
        self.command = command
        self.stderr = stderr
        message = f"Command '{command}' failed with reason: {stderr}"
        super().__init__(message)

def ssh_run_fg_command(host, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host.host_name,
                    username=host.credentials.user_name,
                    password=host.credentials.password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        return str(output).strip()
    except socket.timeout:
        raise RemoteCommandError(command, "Connection timed out.")
    except socket.gaierror:
        raise RemoteCommandError(command, "Hostname could not be resolved.")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        raise RemoteCommandError(command, f"Unable to connect to port 22 on the host: {e}")
    except paramiko.ssh_exception.AuthenticationException:
        raise RemoteCommandError(command, "Authentication failed.")
    except paramiko.ssh_exception.SSHException as e:
        raise RemoteCommandError(command, f"SSH negotiation failed: {e}")
    except Exception as e:
        raise RemoteCommandError(command, f"General error: {e}")
    finally:
        ssh.close()

def ssh_run_bg_command(host, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host.host_name,
                    username=host.credentials.user_name,
                    password=host.credentials.password)
        bg_command = f"{command} & echo $!"
        stdin, stdout, stderr = ssh.exec_command(bg_command)
        pid = stdout.read().decode().strip()

        return str(pid)
    except socket.timeout:
        raise RemoteCommandError(command, "Connection timed out.")
    except socket.gaierror:
        raise RemoteCommandError(command, "Hostname could not be resolved.")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        raise RemoteCommandError(command, f"Unable to connect to port 22 on the host: {e}")
    except paramiko.ssh_exception.AuthenticationException:
        raise RemoteCommandError(command, "Authentication failed.")
    except paramiko.ssh_exception.SSHException as e:
        raise RemoteCommandError(command, f"SSH negotiation failed: {e}")
    except Exception as e:
        raise RemoteCommandError(command, f"General error: {e}")
    finally:
        ssh.close()