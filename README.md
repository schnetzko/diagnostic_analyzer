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

There will pytest based test. Currently there is only one Python module
within tests/integration folder to generate a sample log file + 2 backup files.
   ```bash
   python tests/integration/generate_diagnostic_log_file.py
   ```

   ```text
   [2026-06-16 20:20:05.860] : any other event log
   [2026-06-16 20:20:05.860] : any other event log
   [2026-06-16 20:20:05.861] : any other event log
   [2026-06-16 20:20:05.861] : any other event log
   [2026-06-16 20:20:05.862] : any other event log
   #PE[2026-06-16 20:20:05.862] : END DEVICE_TEST
   #PE[2026-06-16 20:20:05.863] : END DEVICE_TEST
   [2026-06-16 20:20:05.864] : any other event log
   [2026-06-16 20:20:05.865] : any other event log
   [2026-06-16 20:20:05.865] : any other event log
   [2026-06-16 20:20:05.866] : any other event log
   #PE[2026-06-16 20:20:05.866] : BEGIN REMOVAL
   [2026-06-16 20:20:05.867] : any other event log
   [2026-06-16 20:20:05.867] : any other event log
   [2026-06-16 20:20:05.868] : any other event log
   [2026-06-16 20:20:05.869] : any other event log
   ```