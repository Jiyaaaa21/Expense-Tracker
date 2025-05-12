import datetime
import csv

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date & time in a readable format

    def __str__(self):
        return f"{self.date} | ₹{self.amount} | {self.category} | {self.description}"

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully")

    def save_expenses(self):
        # Open the CSV file in append mode, creating a new file if it doesn't exist
        with open(self.filename, mode="a", newline='') as file:
            writer = csv.writer(file)
            # Write a header if the file is empty
            if file.tell() == 0:
                writer.writerow(["Date", "Amount", "Category", "Description"])
            for expense in self.expenses:
                writer.writerow([expense.date, expense.amount, expense.category, expense.description])
            self.expenses.clear()  # Clear the list after saving
            print("All expenses saved to file.")

if __name__ == "__main__":
    tracker = ExpenseTracker()  # create an instance of tracker
    while True:
        print("\n==== Expense tracker ===")
        print("1. Add New Expense")
        print("2. Save Expenses to file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            amount = float(input("Enter amount: ₹"))
            category = input("Enter category (e.g., Food, Travel): ")
            description = input("Enter description (optional): ")
            expense = Expense(amount, category, description)
            tracker.add_expense(expense)

        elif choice == "2":
            tracker.save_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.") 





   

