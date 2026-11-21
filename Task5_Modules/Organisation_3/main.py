from reader import read_attendance
from report import create_report

records = read_attendance()

create_report(records)