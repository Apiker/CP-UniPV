seconds = eval(input("Number of seconds: "))

minutes = seconds/60
hours = minutes/60
days = hours/24
months = days/30
years = months/12

print("Given 30-day months in a year, there are")
print("Minutes in", seconds, "seconds:", minutes)
print("Hours in", minutes, "minutes:", hours)
print("Days in", hours, "hours:", days)
print("Months in", days, "days:", months)
print("Years in", months, "months:", years)