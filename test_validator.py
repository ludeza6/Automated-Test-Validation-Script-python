import csv
import sys
import logging
import argparse
from datetime import datetime

# Logging is the industry standard for tracking errors
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Measurement:
    """Represents a single hardware test with validation logic."""
    def __init__(self, name, measured, min_val, max_val, unit):
        self.name = name
        self.measured = float(measured)
        self.min_val = float(min_val)
        self.max_val = float(max_val)
        self.unit = unit
        self.passed, self.margin = self._validate()

    def _validate(self):
        passed = self.min_val <= self.measured <= self.max_val
        # Calculate 'Margin' - how close the value was to failing
        margin = min(self.measured - self.min_val, self.max_val - self.measured)
        return passed, round(margin, 4)

    def to_dict(self):
        return {
            "name": self.name, "measured": self.measured, "unit": self.unit,
            "range": f"{self.min_val}-{self.max_val}",
            "status": "PASS" if self.passed else "FAIL", "margin": self.margin
        }

class ReportGenerator:
    """Generates visual reports for stakeholders."""
    @staticmethod
    def print_console(results):
        print(f"\n{'TEST NAME':<20} | {'STATUS':<6} | {'VALUE':<10} | {'MARGIN'}")
        print("-" * 55)
        for r in results:
            print(f"{r['name']:<20} | {r['status']:<6} | {r['measured']}{r['unit']:<4} | {r['margin']:+.2f}")

class TestValidatorApp:
    def __init__(self, input_file):
        self.input_file = input_file
        self.measurements = []

    def run(self):
        try:
            with open(self.input_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.measurements.append(Measurement(
                        row['test_name'], row['measured_value'], 
                        row['expected_min'], row['expected_max'], row['unit']
                    ))
            results = [m.to_dict() for m in self.measurements]
            ReportGenerator.print_console(results)
        except Exception as e:
            logging.error(f"Failed to process data: {e}")

if __name__ == "__main__":
    app = TestValidatorApp("measurements.csv")
    app.run()
