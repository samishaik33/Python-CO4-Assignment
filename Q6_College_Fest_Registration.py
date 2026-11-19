from io import StringIO


class InvalidRegistration(Exception):
    pass


data = """S101,Arun,CSE
S102,Bala,ECE
S103,Divya,IT
S101,Arun,CSE
S104,,EEE
S105,Kiran
"""


def validate(record):
    parts = record.strip().split(",")

    if len(parts) != 3:
        raise InvalidRegistration("Invalid fields")

    reg, name, dept = parts

    if not reg or not name or not dept:
        raise InvalidRegistration("Empty field")

    return reg, name, dept


def read_registrations():
    registrations = []
    seen = set()
    errors = []

    with StringIO(data) as file:
        for line_no, line in enumerate(file, 1):
            try:
                reg, name, dept = validate(line)

                if reg in seen:
                    raise InvalidRegistration("Duplicate registration")

                seen.add(reg)
                registrations.append((reg, name, dept))

            except InvalidRegistration as error:
                errors.append(f"Line {line_no}: {error}")

    return registrations, errors


def create_report(registrations):
    report = StringIO()
    report.write("COLLEGE FEST REGISTRATION REPORT\n")
    for reg, name, dept in registrations:
        report.write(f"{reg} - {name} - {dept}\n")
    report.write(f"\nTotal Registrations: {len(registrations)}")
    return report.getvalue()


def main():
    registrations, errors = read_registrations()

    print("COLLEGE FEST REGISTRATION")
    print("-------------------------")
    print("Total valid registrations:", len(registrations))
    print("Rejected records:", len(errors))

    print("\nREGISTRATION REPORT")
    print(create_report(registrations))

    print("\nERROR LOG")
    if errors:
        for error in errors:
            print(error)
    else:
        print("No errors")


main()