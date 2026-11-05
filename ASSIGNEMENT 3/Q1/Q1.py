
import random
import time


# Generate 365 rainfall readings
readings = []

for i in range(365):
    readings.append(random.randint(0, 100))


# Weekly rainfall totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    total = sum(readings[i:i + 7])
    weekly_totals.append(total)

print("Weekly totals:", weekly_totals)


# Maximum and minimum rainfall
if len(readings) > 0:
    maximum = max(readings)
    minimum = min(readings)

    print("Maximum rainfall:", maximum)
    print("Maximum position:", readings.index(maximum) + 1)

    print("Minimum rainfall:", minimum)
    print("Minimum position:", readings.index(minimum) + 1)


# Naive moving average
def naive_average(data):
    averages = []

    if len(data) < 7:
        return averages

    for i in range(len(data) - 6):
        total = sum(data[i:i + 7])
        averages.append(total / 7)

    return averages


# Running sum moving average
def running_average(data):
    averages = []

    if len(data) < 7:
        return averages

    total = sum(data[:7])
    averages.append(total / 7)

    for i in range(7, len(data)):
        total = total + data[i]
        total = total - data[i - 7]

        averages.append(total / 7)

    return averages


naive = naive_average(readings)
running = running_average(readings)

print("Naive moving average:", naive[:10])
print("Running moving average:", running[:10])


# Dry days
dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("Dry days:", dry_days)


# Slicing examples
print("Readings 7 to 14:", readings[7:14])
print("Last 7 readings:", readings[-7:])
print("Every seventh reading:", readings[::7])


# Experimental investigation
sizes = [365, 36500, 365000]

print("\nExecution time comparison")

for size in sizes:

    data = []

    for i in range(size):
        data.append(random.randint(0, 100))

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("\nReadings:", size)
    print("Naive time:", naive_time)
    print("Running sum time:", running_time)


# Edge cases
print("\nEmpty list:", running_average([]))
print("Short list:", running_average([2, 4, 6, 8]))
