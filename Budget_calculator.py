def budget_calculator():
    print("Budget Calculator")
    print("-------------------")

    # get monthly income
    income = float(input("Enter your monthly income: "))
    expenses = {}

    print("\nEnter your expenses. Type 'Done' when finished.")

    while True:
        category = input("Enter name: ")
        if category == "Done":
            break
        amount = float(input(f"Amount for {category}: "))
        expenses[category] = amount

    total_expenses = sum(expenses.values())
    balance = income-total_expenses

    print("\nsummary")
    print("----------")
    print(f"Total Income: {income}")
    print("Total Expenses: {0}".format(total_expenses))
    print("Balance left: {0}".format(balance))

    print("\nBreakdown:")
    for cat, amt in expenses.items():
        print(f"{cat}: {amt}")


budget_calculator()
