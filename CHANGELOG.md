# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0-dev] - 2026-06-17

> ⚠️ This release is **not production-ready**. It is a development snapshot intended for prototyping and demonstration purposes only. It may lack proper error handling, security measures, and other production considerations.

### Added

#### Diagnostic log file generator for testing
- Introduced [`diagnostic_log_file_generator.py`](tests/integration/diagnostic_log_file_generator.py) to generate diagnostic log file and backup files as a basis for implementing the analyzer. Sample diagnostic log files are added to repo. The number of non-PE (Profiling Event) log entries is generated randomly, and these entries contain random English words.
#### python package structure
- Introduced basic structure to build wheel file, to execute tests and to define dependencies.
#### CLI tool
- introduce CLI as entry point to use this tool
