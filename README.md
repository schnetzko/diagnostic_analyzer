# Diagnostic Analyzer
Analyze diagnostic log files of an automated test equipment system (ATE).

   ```text
   diagnostic_analyzer/src/diagnostic_analyzer$ python main.py --help
   usage: main.py [-h] [-file_path FILE_PATH]
   
   CLI tool to analyze diagnostic log file of an automated test equipment system (ATE).

   options:
   -h, --help            show this help message and exit
   -file_path FILE_PATH  path/to/diagnostic.log
   ```
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

There will pytest based tests. Currently there is a Python module
at tests/integration to generate sample log file and backup files.
The generated sample log file and backup files will be used for tests.
   ```bash
   python tests/integration/diagnostic_log_file_generator.py
   ```
Example:
   ```text
   [2026-06-18 16:20:16.194] : ribbonweed intertongue coeditor spitefullest
   [2026-06-18 16:20:16.990] : conformingly lang solace debased
   #PE[2026-06-18 16:20:16.991] : END INSERTION
   [2026-06-18 16:20:17.582] : extensional leavened scummier
   [2026-06-18 16:20:18.169] : nonadjustive misgiving tarantulous
   [2026-06-18 16:20:18.756] : stimulator nants pathoformic
   #PE[2026-06-18 16:20:18.757] : BEGIN DEVICE_TEST
   #PE[2026-06-18 20:20:18.758] : BEGIN DEVICE_TEST.SUBTEST "check connection"
   [2026-06-18 16:20:19.567] : lym tropicalise glack dyeable
   [2026-06-18 16:20:20.357] : spongoid chegre hemology marylandian
   [2026-06-18 16:20:21.159] : exacuate polytonic pretastes laitance
   [2026-06-18 16:20:22.034] : sprangle pod antignostic skittle
   [2026-06-18 16:20:22.863] : crashed gatch immure euhemerised
   #PE[2026-06-18 16:20:22.865] : END DEVICE_TEST.SUBTEST
   #PE[2026-06-18 16:20:22.865] : BEGIN DEVICE_TEST.SUBTEST "measure leakage current"
   [2026-06-18 16:20:23.508] : cogeneration predisability rocky
   [2026-06-18 16:20:24.144] : braggle aeroplane miffier
   [2026-06-18 16:20:24.738] : oversold klva usherdom
   #PE[2026-06-18 16:20:24.739] : END DEVICE_TEST.SUBTEST
   #PE[2026-06-18 16:20:24.739] : END DEVICE_TEST
   [2026-06-18 16:20:25.152] : unslurred hypoazoturia
   [2026-06-18 16:20:25.543] : hyperexcitability winetree
   [2026-06-18 16:20:26.003] : pedule lioncel
   [2026-06-18 16:20:26.399] : necrotic supraseptal
   [2026-06-18 16:20:26.802] : calcitrant ombrometer
   #PE[2026-06-18 16:20:26.803] : BEGIN REMOVAL
   [2026-06-18 16:20:27.593] : expressivity overstatement cryptologist fadge
   #PE[2026-06-18 16:20:27.594] : END REMOVAL
   ```