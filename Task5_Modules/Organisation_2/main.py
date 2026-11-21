import attendance

records = attendance.read_attendance()

print("ATTENDANCE REPORT")

for reg, status in records:
    print(reg, status)

print("Percentage:", attendance.calculate_stats(records))