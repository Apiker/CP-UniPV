years = eval(input("Number of years: "))

mnt = years * 12
dys = mnt * 30
hrs = dys * 24
min = hrs * 60
scn = min * 60

print("Given 30-day months in a year, there are")
print("Months in", years, "years:", mnt)
print("Days in", mnt, "months:", dys)
print("Hours in", dys, "days:", hrs)
print("Minutes in", hrs, "hours:", min)
print("Seconds in", min, "minutes:", scn)

