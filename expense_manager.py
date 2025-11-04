import csv
from datetime import datetime
import pandas as pd
import os

class ExpenseManager:
    def __init__(self):
        self.file_path = "data/expenses.csv"
        os.makedirs("data", exist_ok=True)
        
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Category", "Description", "Amount"])

    def add_expense(self):
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter category (Food/Travel/Shopping/etc): ")
        description = input("Enter description: ")
        amount = input("Enter amount: ")

        with open(self.file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, category, description, amount])
        print("✅ Expense added!")

    def view_expenses(self):
        df = pd.read_csv(self.file_path)
        print("\n---- All Expenses ----")
        print(df)

    def delete_expense(self):
        df = pd.read_csv(self.file_path)
        print(df)
        index = int(input("Enter index to delete: "))
        df = df.drop(index)
        df.to_csv(self.file_path, index=False)
        print("🗑️ Expense deleted!")

    def monthly_summary(self):
        df = pd.read_csv(self.file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.strftime('%B')
        print("\n---- Monthly Summary ----")
        print(df.groupby('Month')['Amount'].sum())

    def category_summary(self):
        df = pd.read_csv(self.file_path)
        print("\n---- Category Summary ----")
        print(df.groupby('Category')['Amount'].sum())
