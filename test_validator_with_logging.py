import csv
import logging

# Configure logging
logging.basicConfig(
    filename="test_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_measurements(csv_file):
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            voltage = float(row["voltage"])
            current = float(row["current"])

            if 4.5 <= voltage <= 5.5 and current <= 2.0:
                status = "PASS"
            else:
                status = "FAIL"

            message = f"Voltage={voltage}V, Current={current}A -> {status}"
            print(message)
            logging.info(message)

if __name__ == "__main__":
    validate_measurements("measurements.csv")
