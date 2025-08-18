numDay = int(input("Enter the number of days: "))

total = 0
for i in range(1, numDay+1):
    nextDay = int(input(f"Enter day {i}'s high temperature: "))
    total += nextDay

avg = total / numDay
print(f"Average temperature is {avg}")



