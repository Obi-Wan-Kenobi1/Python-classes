numbers = input("Enter all of your numbers.")
numbers = numbers.split(" ")

print(numbers)

def addition1(numbers):
    sum1 = 0
    for i in numbers:
        sum1 += float(i)
    return sum1

def subtraction1(numbers):
    sub = float(numbers[0])
    for i in numbers[1:]:
        sub -= float(i)
    return sub

def multiplication1(numbers):
    print(numbers)
    multiple = 1
    for i in numbers:
        multiple *= float(i)
    return multiple

def division1(numbers):
    divident = float(numbers[0])
    for i in numbers[1:]:
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
        elif operation == "subtraction":
            print(subtraction1(numbers))
        elif operation == "multiplication":
            print(multiplication1(numbers))
        elif operation == "division":
            print(division1(numbers))
        else:
            print("incorrect format")
    else:
        print("incorrect format")