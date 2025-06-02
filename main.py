import time

from trace.auditor import LogAuditor
from trace.collector import Collector
from cli.parser import get_cli_arguments
from ssh.ssh_credentials import SSHCredentials, SSHHost


if __name__ == "__main__":

    args = get_cli_arguments()

    ssh_host = SSHHost(
        host_name = args.host_name,
        credentials = SSHCredentials(
            user_name=args.user_name,
            password=args.password,
        )
    )

    auditor = LogAuditor(
        monitored_host=ssh_host,
        monitored_file=args.monitored_file,
        monitored_log=args.monitored_log,
    )

    collector = Collector(
        traced_host=ssh_host,
        interface=args.interface,
        remote_log_dir=args.remote_log_dir
    )


    while True:
        try:
            if not collector.is_started():
                collector.start()
            error_data = auditor.run_audit()
            if error_data.has_error():
                collector.on_error()
                print("Issue detected.", flush=True)
                break
            else:
                print("No issue detected.", flush=True)
            time.sleep(10)
        except Exception as ex:
            print(f"Issue detected {ex}. Wait for recovery.")
            time.sleep(60)