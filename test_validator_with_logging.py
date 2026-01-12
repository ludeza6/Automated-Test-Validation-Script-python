import logging

# Configure logging to file
logging.basicConfig(
    filename="test_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Measurement:
    def __init__(self, name, value, min_limit, max_limit, unit):
        self.name = name
        self.value = value
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.unit = unit

        self.passed = self.min_limit <= self.value <= self.max_limit

        status = "PASS" if self.passed else "FAIL"
        logging.info(
            f"{self.name}: {self.value}{self.unit} "
            f"(Limits: {self.min_limit}-{self.max_limit}{self.unit}) -> {status}"
        )
