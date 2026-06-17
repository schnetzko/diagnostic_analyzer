# Diagnostic Analyzer
Analyze diagnostic log files of an automated test equipment system (ATE).

## Tech stack

- Python 3.12+

## Setup

1. Install `uv` if you don't already have it:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Initialize the uv environment and install dependencies:
   ```bash
   uv sync
   ```

## Tests

There will pytest based tests. Currently there is one Python module
at tests/integration to generate sample log file + 2 backup files.
The generated sample log file + backup files will be used for tests.
   ```bash
   python tests/integration/generate_diagnostic_log_file.py
   ```

   ```text
   [2026-06-17 08:14:36.175] : any other event log
   #PE[2026-06-17 08:14:36.176] : END REMOVAL
   [2026-06-17 08:14:36.176] : any other event log
   [2026-06-17 08:14:36.177] : any other event log
   #PE[2026-06-17 08:14:36.177] : BEGIN INSERTION "Device #6"
   [2026-06-17 08:14:36.178] : any other event log
   [2026-06-17 08:14:36.179] : any other event log
   [2026-06-17 08:14:36.179] : any other event log
   [2026-06-17 08:14:36.179] : any other event log
   [2026-06-17 08:14:36.180] : any other event log
   #PE[2026-06-17 08:14:36.180] : END INSERTION
   [2026-06-17 08:14:36.181] : any other event log
   [2026-06-17 08:14:36.181] : any other event log
   [2026-06-17 08:14:36.182] : any other event log
   [2026-06-17 08:14:36.182] : any other event log
   #PE[2026-06-17 08:14:36.183] : BEGIN DEVICE_TEST
   #PE[2026-06-17 08:14:36.183] : BEGIN DEVICE_TEST.SUBTEST "check connection"
   [2026-06-17 08:14:36.183] : any other event log
   #PE[2026-06-17 08:14:36.184] : END DEVICE_TEST
   [2026-06-17 08:14:36.184] : any other event log
   [2026-06-17 08:14:36.184] : any other event log
   [2026-06-17 08:14:36.185] : any other event log
   ```