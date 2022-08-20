numbers = input("Enter all of your numbers.")
numbers.split(" ")
print(numbers)
def addition1(numbers):
    for i in numbers:
        sum1 = 0
        sum1 += float(i)
    return sum1

def subtraction1(numbers):
    for i in numbers:
        sub = 0
        sub -= float(i)
    return sub

def multiplication1(numbers):
    for i in numbers:
        multiple = 0
        multiple *= float(i)
    return multiple

def division1(numbers):
    for i in numbers:
        divident = 0
        divident /= float(i)
    return divident

while True:
    quit1 = input("Do you want to quit?").lower()
    if quit1 == "yes":
        break
    elif quit1 == "no":
        operation = input("Which operation do you want to use? Multiplication, Division, Addition ot Subtracrion?").lower()
        if operation == "addition":
            print(addition1(numbers))
        elif operation == "subtracition":
            print(subtraction1(numbers))
        elif operation == "multiplication":
            print(multiplication1(numbers))
        elif operation == "division":
            print(division1(numbers))
        else:
            print("incorrect format")
    else:
        print("incorrect format")