print(f"Which of the following numbers represents the smallest value? 3, 0.3, 0.33, 0.333")

values = [.4, 0.44, 0.444, 0.4444]
largest = values[0]

for value in values:
    if value > largest:
        largest = value

print(f"The largest value is: {largest}")