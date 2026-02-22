import math
import datetime

history = []

# ---------------- OPERATIONS ----------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    return math.sqrt(a)


# ---------------- SAVE HISTORY ----------------
def save_history():
    with open("calculator_history.txt", "a") as file:
        for record in history:
            file.write(record + "\n")
    print("History saved successfully!\n")


# ---------------- SHOW HISTORY ----------------
def show_history():
    if not history:
        print("No calculations yet.\n")
        return
    print("\n------ Calculation History ------")
    for record in history:
        print(record)
    print()


# ---------------- MAIN PROGRAM ----------------
def main():
    while True:
        print("\n========== ADVANCED CALCULATOR ==========")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Show History")
        print("9. Save History to File")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '10':
                print("Exiting calculator. Thank you! 👋")
                break

            elif choice in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"

                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"

                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"

                elif choice == '4':
                    result = divide(num1, num2)
                    operation = f"{num1} / {num2} = {result}"

                elif choice == '5':
                    result = power(num1, num2)
                    operation = f"{num1} ^ {num2} = {result}"

                elif choice == '6':
                    result = modulus(num1, num2)
                    operation = f"{num1} % {num2} = {result}"

                print("Result:", result)
                history.append(f"{datetime.datetime.now()} | {operation}")

            elif choice == '7':
                num = float(input("Enter number: "))
                result = square_root(num)
                operation = f"√{num} = {result}"
                print("Result:", result)
                history.append(f"{datetime.datetime.now()} | {operation}")

            elif choice == '8':
                show_history()

            elif choice == '9':
                save_history()

            else:
                print("Invalid choice! Please select valid option.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except ZeroDivisionError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
