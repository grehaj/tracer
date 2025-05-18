"""
    This module provides ...
"""

import paramiko
import socket
import time

from ssh.ssh_credentials import SSHCredentials

class RemoteCommandError(Exception):
    def __init__(self, command, stderr):
        self.command = command
        self.stderr = stderr
        message = f"Command '{command}' failed with reason: {stderr}"
        super().__init__(message)

def ssh_run_command(ssh_credentials, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=ssh_credentials.host,
                    username=ssh_credentials.username,
                    password=ssh_credentials.password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        error_msg = str(stderr.read().decode())
        if len(error_msg) > 0:
            raise RemoteCommandError(cmd, error_msg)
        return str(stdout.read().decode()).strip()
    except socket.timeout:
        raise RemoteCommandError(cmd, "Connection timed out.")
    except socket.gaierror:
        raise RemoteCommandError(cmd, "Hostname could not be resolved.")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        raise RemoteCommandError(cmd, f"Unable to connect to port 22 on the host: {e}")
    except paramiko.ssh_exception.AuthenticationException:
        raise RemoteCommandError(cmd, "Authentication failed.")
    except paramiko.ssh_exception.SSHException as e:
        raise RemoteCommandError(cmd, f"SSH negotiation failed: {e}")
    except Exception as e:
        raise RemoteCommandError(cmd, f"General error: {e}")
    finally:
        ssh.close()

def ssh_run_jumped_command(jump_host_ssh_credentials, target_host_ssh_credentials, cmd):
    jump_client = paramiko.SSHClient()
    jump_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        jump_client.connect(hostname=jump_host_ssh_credentials.host,
                            username=jump_host_ssh_credentials.username,
                            password=jump_host_ssh_credentials.password)

        jump_transport = jump_client.get_transport()
        dest_addr = (target_host_ssh_credentials.host, 22)
        local_addr = ('', 0)
        channel = jump_transport.open_channel("direct-tcpip", dest_addr, local_addr)
        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(
            hostname=target_host_ssh_credentials.host,
            username=target_host_ssh_credentials.username,
            password=target_host_ssh_credentials.password,
            sock=channel
        )
        stdin, stdout, stderr = target_client.exec_command(cmd)
        error_msg = str(stderr.read().decode())
        if len(error_msg) > 0:
            raise RemoteCommandError(cmd, error_msg)
        return str(stdout.read().decode()).strip()
    except socket.timeout:
        raise RemoteCommandError(cmd, "Connection timed out.")
    except socket.gaierror:
        raise RemoteCommandError(cmd, "Hostname could not be resolved.")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        raise RemoteCommandError(cmd, f"Unable to connect to port 22 on the host: {e}")
    except paramiko.ssh_exception.AuthenticationException:
        raise RemoteCommandError(cmd, "Authentication failed.")
    except paramiko.ssh_exception.SSHException as e:
        raise RemoteCommandError(cmd, f"SSH negotiation failed: {e}")
    except Exception as e:
        raise RemoteCommandError(cmd, f"General error: {e}")
    finally:
        target_client.close()
        jump_client.close()

def send_command(shell, cmd, wait=1):
    shell.send(cmd + '\n')
    time.sleep(wait)
    output = shell.recv(10000).decode()
    return output

def ssh_run_jumped_command_in_config_mode(jump_host_ssh_credentials, target_host_ssh_credentials, cmd):
    jump_client = paramiko.SSHClient()
    jump_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        jump_client.connect(hostname=jump_host_ssh_credentials.host,
                            username=jump_host_ssh_credentials.username,
                            password=jump_host_ssh_credentials.password)

        jump_transport = jump_client.get_transport()
        dest_addr = (target_host_ssh_credentials.host, 22)
        local_addr = ('', 0)
        channel = jump_transport.open_channel("direct-tcpip", dest_addr, local_addr)
        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(
            hostname=target_host_ssh_credentials.host,
            username=target_host_ssh_credentials.username,
            password=target_host_ssh_credentials.password,
            sock=channel
        )

        shell = target_client.invoke_shell()
        time.sleep(1)
        shell.recv(1000)
        print(send_command(shell, 'config'))
        output = send_command(shell, cmd)

        return str(output).strip()
    except socket.timeout:
        raise RemoteCommandError(cmd, "Connection timed out.")
    except socket.gaierror:
        raise RemoteCommandError(cmd, "Hostname could not be resolved.")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        raise RemoteCommandError(cmd, f"Unable to connect to port 22 on the host: {e}")
    except paramiko.ssh_exception.AuthenticationException:
        raise RemoteCommandError(cmd, "Authentication failed.")
    except paramiko.ssh_exception.SSHException as e:
        raise RemoteCommandError(cmd, f"SSH negotiation failed: {e}")
    except Exception as e:
        raise RemoteCommandError(cmd, f"General error: {e}")
    finally:
        target_client.close()
        jump_client.close()