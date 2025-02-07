day = input()

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print((6 - week.index(day)) % 6)
