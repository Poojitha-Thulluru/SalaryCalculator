hours_worked = []

try:
    try :
        for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            hours = int(input(f"Enter the number of hours worked on {day}: "))
            hours_worked.append(hours)
    except ValueError:
        print("Invalid Input... Please Enter Only Integers")
    base_salary = 100  # Base hourly rate
    extra_hours_rate = 15  # Extra rate for hours above 8 in a day
    bonus_sunday = 0.5  # Bonus for working on Sunday (50%)
    bonus_saturday = 0.25  # Bonus for working on Saturday (25%)
    weekly_salary = sum(hours_worked) * base_salary
    for i in range(1, 6):  # Monday to Friday
        if hours_worked[i] > 8:
            weekly_salary += (hours_worked[i] - 8) * extra_hours_rate

    weekly_salary += (hours_worked[0] * base_salary * bonus_sunday) if hours_worked[0] else 0
    weekly_salary += (hours_worked[6] * base_salary * bonus_saturday) if hours_worked[6] else 0
    if sum(hours_worked) > 40:
        overtime_hours = sum(hours_worked) - 40
        weekly_salary += overtime_hours * 25

    print(int(weekly_salary))

except ValueError as e:
    print(e)