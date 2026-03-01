# Expense Tracker Project

expensesList = []
print("Welcome to Expense Tracker")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your choice = "))

    if (choice == 1):
        date = input("Enter the date = ")
        category = input("Enter the Category (Food, Travel, Makeup, Books) = ")
        description = input("Enter Short description = ")
        amount = float(input("Enter the Amount = "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n Expenses is added succesfully")
    
    elif(choice == 2):
        if(len(expensesList)==0):
            print("No Expenses Added.")
        else:
            print("=== This is your expense ===")
            count = 1
            for eachExpenses in expensesList:
                print(f"Expense Number {count} -> {eachExpenses["date"]}, {eachExpenses["category"]}, {eachExpenses["description"]}, {eachExpenses["amount"]} ")
                count = count+1

    elif(choice == 3):
        total = 0
        for eachExpenses in expensesList:
            total = total + eachExpenses["amount"]

        print("\n TOTAL EXPENSES = ", total)

    elif(choice == 4):
        print("Thank You")
        break

    else:
        print("Invalid choice. Try again.")