"""Think Python 2 - exercise 1.2"""

# seconds is 42 minutes 42 seconds
m = 42
s = 42
s = s + m*60
print(s)

# miles in 10 km
km = 10
miles = km * 0.62137
print(miles)

# average pace and speed
m = s / 60
pace = m / miles
seconds = (pace*60) % 60
h = s / 3600
v = km / h
print('Pace:', str(int(pace)) + ":" + str(int(seconds)), 'minutes/mile  |   Avg speed:', v, 'km/h')
