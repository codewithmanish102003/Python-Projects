import calendar 

month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

cal = calendar.month(year, month)
print(cal)