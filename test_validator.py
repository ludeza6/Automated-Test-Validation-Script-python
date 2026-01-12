import csv

def load_measurements(filename):
    measurements = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            measurements.append({
                "test_name": row["test_name"],
                "measured": float(row["measured_value"]),
                "min": float(row["expected_min"]),
                "max": float(row["expected_max"]),
                "unit": row["unit"]
            })
    return measurements

def validate_measurements(measurements):
    results = []
    for test in measurements:
        passed = test["min"] <= test["measured"] <= test["max"]
        results.append({
            "test_name": test["test_name"],
            "measured": test["measured"],
            "range": f'{test["min"]}-{test["max"]}',
            "unit": test["unit"],
            "status": "PASS" if passed else "FAIL"
        })
    return results

def print_report(results):
    print("TEST VALIDATION REPORT")
    print("-" * 40)
    for r in results:
        print(
            f'{r["test_name"]}: {r["measured"]}{r["unit"]} '
            f'(Expected {r["range"]}) -> {r["status"]}'
        )

def main():
    measurements = load_measurements("measurements.csv")
    results = validate_measurements(measurements)
    print_report(results)

if __name__ == "__main__":
    main()
