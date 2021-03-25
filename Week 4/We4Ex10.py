salary = int(input("Enter your current salary: "))
if salary >= 500:
    print(f"Your final salary is {salary}€")
elif salary < 500:
    work_time = int(input("For how long have you been working with us? "))
    if work_time >= 10:
        salary += salary * 0.2
    elif work_time < 10:
        salary += salary * 0.05
    print(f"Since you've been working with us for {work_time} years, your salary is {salary}€")