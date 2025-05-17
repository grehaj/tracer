import time

from audit.auditor import Auditor
from cli.parser import create_parser
from config.config_manager import ConfigManager
from trace.tracer import Tracer

if __name__ == "__main__":
    cli_parser = create_parser()
    args = cli_parser.parse_args()
    config_manager = ConfigManager(host_name=args.host_name)
    auditor = Auditor(credentials=config_manager.get_auditor_host_credentials())
    tracer = Tracer(credentials = config_manager.get_trace_host_credentials())

    tracer.start()
    while True:
        error_data = auditor.run_audit()
        if error_data.has_error():
            tracer.stop()
            print("Issue detected")
            break
        else:
            print("No issue detected")
            time.sleep(5)