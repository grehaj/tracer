Title: Tracer
|----------------------------------------------------------------------------------------------------------|
Problem: Program running on the remote host crashes from time to time. We need to monitor its work
and collect tcp dump from the moment of failure to allow further troubleshooting.
|----------------------------------------------------------------------------------------------------------|
Description:
- An app that allows user to start tcp dump on the remote host from the interface provided by the user.
- It constantly monitors log file selected.
- When an expected error happens copies logs from the remote host to a local directory selected.
|----------------------------------------------------------------------------------------------------------|
