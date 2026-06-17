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

There will pytest based tests. Currently there is a Python module
at tests/integration to generate sample log file and backup files.
The generated sample log file and backup files will be used for tests.
   ```bash
   python tests/integration/generate_diagnostic_log_file.py
   ```
Example:
   ```text
   [2026-06-17 14:41:29.835] : impartivity herbaceous effet chased
   [2026-06-17 14:41:30.700] : literalness superconstitutionally bumfs souteneur
   [2026-06-17 14:41:31.694] : majlis imbodiment brassicaceous decurrences
   [2026-06-17 14:41:32.754] : mammillaplasty quieting unpresumptuousness polyactinia
   #PE[2026-06-17 14:41:32.755] : END REMOVAL
   [2026-06-17 14:41:33.441] : aerosphere lozengewise canescence
   #PE[2026-06-17 14:41:33.443] : BEGIN INSERTION "Device #8"
   [2026-06-17 14:41:34.182] : bioassaying emanent taiwan
   [2026-06-17 14:41:34.835] : crotchets wisest preservability
   #PE[2026-06-17 14:41:34.836] : END INSERTION
   [2026-06-17 14:41:35.539] : arcella growan fibrocrystalline
   #PE[2026-06-17 14:41:35.541] : BEGIN DEVICE_TEST
   #PE[2026-06-17 14:41:35.542] : BEGIN DEVICE_TEST.SUBTEST "check connection"
   [2026-06-17 14:41:36.225] : transgresses butyrone bedismal
   [2026-06-17 14:41:36.879] : nonautomotive macroanalyst connexionalism
   [2026-06-17 14:41:37.550] : elasmobranchian goldylocks dopy
   [2026-06-17 14:41:38.116] : boobyalla rubberneck antitruster
   #PE[2026-06-17 14:41:38.117] : END DEVICE_TEST
   [2026-06-17 14:41:38.735] : maternalness buvette grosser
   [2026-06-17 14:41:39.330] : cataractwise viscidity rehinges
   #PE[2026-06-17 14:41:39.331] : BEGIN DEVICE_TEST.SUBTEST "measure leakage current"
   [2026-06-17 14:41:39.720] : nongenetically octoechos
   [2026-06-17 14:41:40.104] : football phacoscope
   [2026-06-17 14:41:40.518] : scallopers disthroned
   [2026-06-17 14:41:40.953] : fogman tecon
   [2026-06-17 14:41:41.350] : rooming forgemen
   ```