import json , math
from datetime import datetime

def add_expense(name,amount, category,date):
    item = {
    "name" : name,
    "amount": amount,
    "category": category,
    "date": date
}
    expenses.append(item)

def get_expenses():
    if not expenses:
         print("No expenses yet")
    else:
        for index, expense in enumerate(expenses, start=1):
            # print(f"Expense: {name} , Amount : {amount}")
            print(f"{index}. {expense}")
def edit_expenses():
    if not expenses:
          print("No expenses yet")
    else:
        get_expenses()
        try:
            index = int(input("Enter expense number to edit: "))
        except ValueError:
            print("Please enter a valid number")
            return
        if 1 <= index <= len(expenses):
            expense = expenses[index - 1]
        else:
             print("Invalid expense number")
             return
            
        print("What do you want to change?")
        print("1. Name\n2. Amount\n3. Category\n4. Date")
            
        choice = input("Enter choice: ")
        if choice == "1":
            expense["name"] = input("Enter new name: ")

        elif choice == "2":
          
            expense["amount"] = ask_amount()
        elif choice == "3":
            expense["category"] = input("Enter new category: ")

        elif choice == "4":
            expense["date"] = ask_date()
        else:
            print("Enter choice between 1 and 4")
            return
        
        print("Expenses updated ")
        return True


def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total amount : {total}")
def delete_expense():
    if not expenses:
        print("No expenses")
    else:
        get_expenses()
        try:
            index = int(input("Enter the index number: "))
        except ValueError:
            print("Please enter a number")
            return
        if 1<=index <= len(expenses):
            expenses.pop(index-1)
            print("Expense deleted")
            return True
        else:
            print("invalid index number")
def save_expenses():
    with open("expenses.json","w") as f:
        json.dump(expenses,f,indent=2)
def load_expenses():
        try:
                with open("expenses.json", "r") as f:
                    data =  json.load(f)
                    return data if isinstance(data,list) else []
        except (FileNotFoundError, json.JSONDecodeError):
                 return []
def ask_amount():
    while True:
                try:
                    amount = float(input("Enter the amount: "))
    
                except ValueError:
                    print("Please enter only values")
                    continue
                if not math.isfinite(amount):
                    print("Amount must be finite number")
                    continue
                if amount<=0:
                    print("Enter amount more than 0")
                    continue
                return amount
def ask_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date = input(prompt).strip()
        try:
           datetime.strptime(date,"%Y-%m-%d")
        except ValueError:
             print("Invalid date. Use YYYY-MM-DD, for example 2026-11-05")
             continue
        return date

expenses = load_expenses()

while True:
    print("1. Add Expense \n2. Show Expenses \n3. Total Expenses \n4. Edit Expenses \n5. Delete Expenses \n6. Quit")
    choice = input("Choose Task:").strip()
    if choice not in ["1","2","3","4","5","6"]:
        print("Enter value between 1 and 6: ")
        continue
    if choice == "1":
        name =  input("Enter the Expense_name: ")
        amount = ask_amount()
        category = input("Enter the Category: ")
        date = ask_date()
        add_expense(name,amount,category,date)
        save_expenses()
    elif choice == "2":
        get_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        if edit_expenses():
            save_expenses()
    elif choice == "5":
        if delete_expense():
            save_expenses()
    elif choice == "6":
        break

