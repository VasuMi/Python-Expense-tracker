print('''============================
        Welcome to the Expense Tracker
         ============================''')

#list of all expenses(list of dictionaries)
expensesList=[]

while True:
    print('''========MENU========
             1. Add Expense
             2. View Expenses
             3. View Total Expenses
             4. Exit''')
             
choice= input("Enter your choice (1-4): ")

#ADD EXPENSE
if choice == 1:
    date=input("Enter the date")
    category=input("Enter the category (food, travel, shopping, any other u want to enter)")
    description=input("any other detail u want to add")
    amount=float(input("Enter the amount spent:"))

    expense={
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    }
    expensesList.append(expense)
    print("Expense added successfully!\n Done bro.")

#VIEW EXPENSES
elif choice == 2:
    if(len(expensesList))==0:
        print("No expenses recorded yet.")
    else:
        print("====YourExpenses====")
        count=1
        for i in expensesList:
            print(f"expense no. {count} ->{i['date']} | {i['category']} | {i['description']} | {i['amount']}")
            count+=1

#VIEW TOTAL EXPENSES
elif choice == 3:
    total=0
    for i in expensesList:
        total+=i['amount']
    print(f"Total Expenses: {total}")

#EXIT
elif choice == 4:
    print("Exiting the Expense Tracker. Thankyou!")
    
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
