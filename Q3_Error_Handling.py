from io import StringIO


class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord("Expected 3 fields")

    reg, date, status = parts

    if status not in ("P", "A"):
        raise InvalidRecord("Invalid status")

    return reg, date, status


def summarise(data):
    present = 0
    absent = 0
    errors = []

    with StringIO(data) as file:
        for line_no, line in enumerate(file, 1):
            try:
                reg, date, status = parse_line(line)
                if status == "P":
                    present += 1
                else:
                    absent += 1
            except InvalidRecord as error:
                errors.append((line_no, str(error)))

    print("File processing completed")
    print("Processing finished")
    return present, absent, errors


data = """192311001,2026-10-08,P
192311002,2026-10-08,A
192311003,2026-10-08
192311004,2026-10-08,L
"""

print(summarise(data))