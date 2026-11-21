def calculate_stats(records):
    total = len(records)

    present = sum(1 for r in records if r[1] == "P")

    return present / total * 100 if total else 0