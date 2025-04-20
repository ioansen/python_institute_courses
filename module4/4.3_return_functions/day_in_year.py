def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    
    months_days = [31, "x", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month != 2:
        return months_days[month-1]
    
    if is_year_leap(year):
        return 29
    
    return 28


def day_of_year(year, month, day):
    days = 0

    for m in range(1, month):
        days += days_in_month(year, m)

    return days + day


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

print()



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

print()


    
    
print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 1, 1))
print(day_of_year(2000, 2, 1))
print(day_of_year(2000, 1, 31))