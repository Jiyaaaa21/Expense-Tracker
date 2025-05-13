import datetime
import os

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
        with open(self.filename, "a" , encoding="utf-8") as file:
            for expense in self.expenses:
                file.write(str(expense) + "\n")
            self.expenses.clear()
            print("All expenses saved to file.")

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
    
    def show_total_summary(self):
        if not os.path.exists(self.filename):
            print("No expense found.")
            return
        
        total = 0.0
        category_summary= {}

        with open(self.filename, "r", encoding = "utf-8") as file:
            for line in file:
                try:
                    parts = line.strip().split("|")
                    amount_str = parts[1].strip().replace("₹", "")
                    amount = float(amount_str)
                    category = parts[2].strip()

                    total +=amount
                    if category in category_summary:
                        category_summary[category] += amount
                    else:
                        category_summary[category] = amount
                except Exception as e:
                    print(f"Skipping a line due to error:{e}")

        print("\n=== Total Expense Summary ===")
        print(f"Total Spent: ₹{total:.2f}\n")
        print("Spending by Category:")
        for category, amount in category_summary.items():
            print(f"  {category}: ₹{amount:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Save Expenses to File")
        print("3. View Saved Expenses")
        print("4. Total summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category: ")
                description = input("Enter description: ")
                expense = Expense(amount, category, description)
                tracker.add_expense(expense)
            except ValueError:
                print("Invalid input. Amount must be a number.")
        elif choice == "2":
            tracker.save_expenses()
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
             tracker.show_total_summary()
        elif choice == "5":
            print("Goodbye!")

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 

    

    











   

