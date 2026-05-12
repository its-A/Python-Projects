'''---Example 1: Mean ---'''
visitors = [120, 150, 135, 142, 160, 122, 130]

mean_visitors = sum(visitors) / len(visitors)

print(f"Mean Visitors: {mean_visitors}")

'''---Example 2: Median ---'''
data = [75, 80, 72, 150, 85, 90, 78]

data.sort()

n = len(data)

if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2

print(f"Median: {median}")


'''---Example 3: Range (Spread of Data) ---'''
temperatures = [18, 21, 19, 25, 17, 23, 20]

data_range = max(temperatures) - min(temperatures)

print(f"Temperatures: {temperatures}")
print(f"Range: {data_range}")


'''---Example 4: Standard Deviation ---'''
import math

data = [20.5, 21.2, 20.8, 22.1, 19.9, 20.1, 21.5]

n = len(data)
mean = sum(data) / n

squared_diffs = []

for value in data:
    squared_diffs.append((value - mean) ** 2)

variance = sum(squared_diffs) / (n - 1)
std_dev = math.sqrt(variance)

print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")


'''---Example 5: Using statistics.stdev() for Standard Deviation ---'''
import statistics

# Student A: Highly consistent scores
student_a = [70, 80, 80, 80, 90]
# Student B: More spread out scores
student_b = [70, 71, 80, 89, 90]

# Calculating Standard Deviation
stdev_a = statistics.stdev(student_a)
stdev_b = statistics.stdev(student_b)

print(f"Student A Standard Deviation: {stdev_a:.2f}")
print(f"Student B Standard Deviation: {stdev_b:.2f}")

'''---Example 6: The Mode (Most Frequent Value) ---'''
orders = ["A", "B", "A", "C", "A", "B"]

frequency = {}

for item in orders:
    frequency[item] = frequency.get(item, 0) + 1

# Find the most frequent value
mode = max(frequency, key=frequency.get)

print(f"Orders: {orders}")
print(f"Mode: {mode}")