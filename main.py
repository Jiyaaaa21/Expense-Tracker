import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # This line saves the current date and timew in a clean, readable format

    def __str__(self):  # this make it easy to print the expense in presentable format
        return f"{self.date} | ₹{self.amount} | {self.category} | {self.description}" 
    
    import os
    import datetime

class ExpenseTracker:
     def __init__(self, filename="expenses.txt"):
            self.filename = filename
            self.expense = []
     def add_expense(self, expense):
          self.expense.append(expense)
          print("Expense added successfully")
     def save_expenses(self):
          with open(self.filename,"a") as file:
               for expense in self.expenses:
                    file.write(str(expense) + "\n") # write one line per expense
                    self.expenses.clear()  # Clear the list after saving
                    print("All expenses saved to file.")

                    



   

