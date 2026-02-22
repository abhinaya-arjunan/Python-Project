import csv
import os
import datetime

FILE_NAME = "expenses.csv"
expenses = []


# ---------------- LOAD DATA ----------------
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)


# ---------------- SAVE DATA ----------------
def save_expenses():
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["date", "amount", "category", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


# ---------------- ADD EXPENSE ----------------
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount! Please enter a number.\n")
        return

    category = input("Enter category (Food/Travel/etc): ").strip()
    note = input("Enter note: ").strip()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!\n")


# ---------------- VIEW EXPENSES ----------------
def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n---------------- Expense List ----------------")
    print("{:<5} {:<20} {:<10} {:<15} {:<20}".format(
        "ID", "Date", "Amount", "Category", "Note"))

    for i, exp in enumerate(expenses, start=1):
        print("{:<5} {:<20} ₹{:<9} {:<15} {:<20}".format(
            i, exp["date"], exp["amount"], exp["category"], exp["note"]))
    print()


# ---------------- DELETE EXPENSE ----------------
def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter ID to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses()
            print(f"Deleted expense: ₹{deleted['amount']} ({deleted['category']})\n")
        else:
            print("Invalid ID.\n")
    except ValueError:
        print("Invalid input.\n")


# ---------------- TOTAL EXPENSE ----------------
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total:.2f}\n")


# ---------------- CATEGORY-WISE TOTAL ----------------
def category_summary():
    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    print("\n------ Category-wise Summary ------")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")
    print()


# ---------------- MAIN MENU ----------------
def main():
    load_expenses()

    while True:
        print("========== ADVANCED EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expense")
        print("5. Category-wise Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
