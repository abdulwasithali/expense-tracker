from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()

    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1': manager.add_expense()
        elif choice == '2': manager.view_expenses()
        elif choice == '3': manager.delete_expense()
        elif choice == '4': manager.monthly_summary()
        elif choice == '5': manager.category_summary()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
