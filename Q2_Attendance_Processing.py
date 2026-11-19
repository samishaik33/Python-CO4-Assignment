from io import StringIO

data = """192311001,2026-10-08,P
192311002,2026-10-08,A
192311003,2026-10-08
192311004,2026-10-08,L
"""


def process_attendance():
    students = {}
    errors = []

    with StringIO(data) as file:
        for line_no, line in enumerate(file, 1):
            try:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    raise ValueError("Invalid fields")
                reg, date, status = parts
                if status not in ("P", "A"):
                    raise ValueError("Invalid status")

                if reg not in students:
                    students[reg] = {"P": 0, "A": 0}

                students[reg][status] += 1

            except ValueError as error:
                errors.append(f"Line {line_no}: {error}")

    report = StringIO()
    report.write("ATTENDANCE REPORT\n")
    for reg, count in students.items():
        total = count["P"] + count["A"]
        percentage = count["P"] / total * 100
        report.write(f"{reg}: {percentage:.2f}%\n")
        if percentage < 75:
            report.write("Below 75%\n")

    print("Attendance processing completed")
    print("Students:", len(students))
    print("Damaged records:", len(errors))
    print(report.getvalue())

    print("ERROR LOG:")
    for error in errors:
        print(error)


process_attendance()
