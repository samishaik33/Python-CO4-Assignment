from stats import calculate_stats


def create_report(records):

    print("ATTENDANCE REPORT")

    for reg, status in records:
        print(reg, status)

    print("Percentage:", calculate_stats(records))