def day_name(day_number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 0 <= day_number <= 6:
        return days[day_number]
    else:
        return "Invalid day number"
print(day_name(0))
print(day_name(1))
print(day_name(2))
print(day_name(3))
print(day_name(4))
print(day_name(5))
print(day_name(6))
