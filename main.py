import datetime
import csv

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.date} | ₹{self.amount} | {self.category} | {self.description}"

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully")

    def save_expenses(self):
        with open(self.filename, "a") as file:
            for expense in self.expenses:
                file.write(str(expense) + "\n")
            self.expenses.clear()
            print("All expenses saved to file.")

if __name__ == "__main__":
    tracker = ExpenseTracker()  # Create an instance of the tracker

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add New Expense")
        print("2. Save Expenses to File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: ₹"))
            category = input("Enter category: ")
            description = input("Enter description: ")

            expense = Expense(amount, category, description)  # create Expense
            tracker.add_expense(expense)  # add to tracker

        elif choice == "2":
            tracker.save_expenses()

        elif choice == "3":
            tracker.view_expenses()
            break
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
    
    def view_expenses(self):
        if not os.path.exists(self.filename):
            print("No expenses found.")
            return

        with open(self.filename, "r") as file:
            print("\nSaved Expenses:")
            print("-" * 50)
            for line in file:
                 print(line.strip())
            print("-" * 50) 









   

