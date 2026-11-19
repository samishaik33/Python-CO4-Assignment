from io import StringIO
from decimal import Decimal, InvalidOperation

data = """192311001, Arun, 1250.50
192311002, Bala, 1400.00
192311003, Divya, 1200.75
192311004, Ravi, invalid
"""


def process_bills():
    total = Decimal("0.00")
    report = []
    rejected = []

    with StringIO(data) as file:
        for line_no, line in enumerate(file, 1):
            try:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    raise ValueError("Invalid number of fields")

                reg_no, name, amount = parts
                bill = Decimal(amount)

                if not bill.is_finite() or bill < 0:
                    raise ValueError("Invalid amount")

                total += bill
                report.append((name, bill))
            except (ValueError, InvalidOperation) as error:
                rejected.append(
                    f"Line {line_no}: {line.strip()} [{error}]"
                )

    print("MESS BILL REPORT")
    print("----------------")
    for name, bill in report:
        print(f"{name}: {bill:.2f}")
    print("----------------")
    print("Total Bill:", f"{total:.2f}")

    print("\nRejected Records:")
    if rejected:
        for item in rejected:
            print(item)
    else:
        print("No rejected records")


process_bills()