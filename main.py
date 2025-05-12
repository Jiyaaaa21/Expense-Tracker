import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # This line saves the current date and timew in a clean, readable format

    def __str__(self):  # this make it easy to print the expense in presentable format
        return f"{self.date} | ₹{self.amount} | {self.category} | {self.description}" 
    

