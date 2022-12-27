# calculator app
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main():
    print("Welcome to the calculator app")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        exit()
    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1:
            print("Result: ", add(a,b))
        elif choice == 2:
            print("Result: ", subtract(a,b))
        elif choice == 3:
            print("Result: ", multiply(a,b))
        elif choice == 4:
            print("Result: ", divide(a,b))
        else:
            print("Invalid choice")
main()
#



