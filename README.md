# Hardware Test Automation & Validation Utility

## Overview
This project is an automated data validation tool designed for hardware engineering and manufacturing environments. It processes raw sensor or test equipment data (via CSV) and performs automated pass/fail analysis against predefined engineering specifications.

By automating the validation process, this tool reduces human error in data interpretation and provides immediate feedback on hardware performance margins.

## Key Features
* **Object-Oriented Design**: Built using modular classes (`Measurement`, `Validator`, `ReportGenerator`) for easy scalability.
* **Automated Validation**: Compares measured values against `min` and `max` tolerances to determine status.
* **Margin Analysis**: Calculates the "Engineering Margin"—quantifying how close a test was to the failure threshold.
* **Professional Reporting**: Generates clean, scannable console reports and professional HTML summaries for stakeholders.
* **Robust Error Handling**: Includes logging and validation to handle malformed data or missing files.
* **Unit Tested**: Features a comprehensive test suite to ensure validation logic accuracy before deployment.

## Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/hardware-validation-tool.git](https://github.com/your-username/hardware-validation-tool.git)
   cd hardware-validation-tool
   
Usage
The tool accepts a CSV file containing test data. The CSV must follow this header format: test_name,measured_value,expected_min,expected_max,unit

Running the Validator
Run the script from your terminal:

Bash

python test_validator.py measurements.csv --html
Running Unit Tests
To verify the integrity of the validation logic:

Bash

python test_suite.py
📋 Data Format Example
The input CSV (measurements.csv) should look like this: | test_name | measured_value | expected_min | expected_max | unit | | :--- | :--- | :--- | :--- | :--- | | Output Voltage | 5.05 | 4.8 | 5.2 | V | | Signal Frequency | 980 | 990 | 1010 | Hz | | Current Draw | 85 | 0 | 100 | mA |

Why I Built This
This project demonstrates the intersection of Software Engineering and Hardware Reliability. It addresses the common industry need to transform raw manufacturing data into actionable insights, showing proficiency in Python, data processing, and quality assurance workflows.
