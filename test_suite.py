import csv
from test_validator_with_logging import Measurement

def run_test_suite(csv_file):
    measurements = []

    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            measurement = Measurement(
                name=row["name"],
                value=float(row["value"]),
                min_limit=float(row["min_limit"]),
                max_limit=float(row["max_limit"]),
                unit=row["unit"]
            )
            measurements.append(measurement)

    passed = sum(1 for m in measurements if m.passed)
    failed = len(measurements) - passed

    print(f"Test Summary: {passed} PASSED, {failed} FAILED")

if __name__ == "__main__":
    run_test_suite("measurements.csv")
