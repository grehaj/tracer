"""
    This module provides ...
"""

from ssh.ssh_command import ssh_run_bg_command, ssh_run_fg_command

class Collector:
    def __init__(self, traced_host, interface, remote_log_dir):
        self.traced_host = traced_host
        self.interface=interface
        self.remote_log_dir=remote_log_dir
        self.tcp_dump_pid = None

    def start(self):
        tcpdump_cmd = (
            f"sudo tcpdump -i {self.interface} -C 10 -W 5 -w {self.remote_log_dir}/trace.pcap -Z client"
            f">> /tmp/tcpdump.log 2>&1"
        )
        self.tcp_dump_pid = ssh_run_bg_command(host=self.traced_host, command=tcpdump_cmd)

        print(f"tcpdump started on remote host with PID: {self.tcp_dump_pid}")


    def stop(self):
        kill_cmd = (
            f"sudo kill {self.tcp_dump_pid} >> /tmp/tcpdump.log"
        )

        result = ssh_run_fg_command(host=self.traced_host, command=kill_cmd)

        print(f"tcpdump with PID: {self.tcp_dump_pid} stopped.")

    def on_error(self):
        self.stop()
        # TODO copy files to local directory

    def is_started(self):
        output = ssh_run_fg_command(host=self.traced_host, command="pgrep -fl tcpdump")

        return len(output) > 0
