#!/usr/bin/python3

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))
# universary time "toUTC"
print(datetime.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {} second".format(datetime.offsetFromUtc()))
print("Day in month: {}".format(now.daysInMonth()))
print("Day in year: {}".format(now.daysInYear()))

# days to 'now'
xmas1 = QDate(2018, 7, 12)
xmas2 = QDate(2019, 7, 12)

to_days = xmas1.daysTo(now)
days_left = now.daysTo(xmas2)

print("days to now:",to_days)
print("days left: ",days_left)

#add or subtract day

print("Adding 12 days: ", datetime.addDays(12).toString(Qt.ISODate))
print("Subtract 25 days: ", datetime.addDays(-25).toString(Qt.ISODate))

print("Adding 50 seconds: ", datetime.addSecs(50).toString(Qt.ISODate))
print("Adding 3 months: ", datetime.addMonths(3).toString(Qt.ISODate))
print("Adding 12 yeasr: ", datetime.addYears(12).toString(Qt.ISODate))
