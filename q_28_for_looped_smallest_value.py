print(f"Which of the following numbers represents the smallest value? 3, 0.3, 0.33, 0.333")

values = [9, 0.9, 0.99, 0.999]
smallest = values[0]

for value in values:
    if value < smallest:
        smallest = value

print(f"The smallest value is: {smallest}")