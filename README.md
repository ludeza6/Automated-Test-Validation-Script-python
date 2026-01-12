# Hardware Test Automation & Validation Utility

A Python-based utility designed to automate the validation of system measurements against predefined thresholds. The suite reads test data from a CSV, evaluates pass/fail criteria, and generates a timestamped execution log.

Features

Automated Validation: Compares numerical measurements against minimum and maximum bounds.



Persistent Logging: Generates detailed execution reports including timestamps, measured values, and status.


Data-Driven Design: Uses CSV input files for easy test case management.

File Structure
test_suite.py: The main entry point that orchestrates the data loading and testing process.

test_validator_with_logging.py: Contains the core logic for measurement evaluation and logging configuration.


measurements.csv: The input data file containing test parameters (names, values, limits, and units).


test_report.log: The output file generated after running tests, documenting every result.

Usage

Prepare your data: Edit measurements.csv to include the values you wish to test.

Run the suite: Execute the main script via terminal:

Bash

python test_suite.py
Check results:

Review the console output for a high-level summary (e.g., Test Summary: 3 PASSED, 1 FAILED).

Open test_report.log for a detailed breakdown of each measurement.

Example Log Output
The system generates logs in the following format:

Plaintext

2026-01-12 12:41:22,812 - INFO - Voltage Rail 1: 5.1V (Limits: 4.8-5.2V) -> PASS
2026-01-12 12:41:22,812 - INFO - Voltage Rail 2: 4.5V (Limits: 4.8-5.2V) -> FAIL
2026-01-12 12:41:22,812 - INFO - Current Draw: 1.9A (Limits: 1.5-2.2A) -> PASS
2026-01-12 12:41:22,812 - INFO - Clock Frequency: 99.8MHz (Limits: 98.0-102.0MHz) -> PASS
Would you like me to add a section on how to extend the Measurement class to support more complex validation logic?
