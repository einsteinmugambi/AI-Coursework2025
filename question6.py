values = []  

for i in range(5):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

average = sum(values) / len(values)

print(f"The average of the values is {average}")
