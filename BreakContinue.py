print("Demonstrating break and continue:")

for i in range(1, 11):
    if i == 5:
        continue  # Skip printing 5
    if i == 9:
        break     # Stop the loop when i is 9
    print(i)
