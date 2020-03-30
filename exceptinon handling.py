try:
    age = int(input("age"))
    salary = int(input("salary"))
    Risk = salary / age
    print (" salary is ", salary)
    print(age)
    print("risk is ",Risk)
except ValueError :
    print("The value cannot be taken")
except ZeroDivisionError:
    print(" Age cannot be zero ")