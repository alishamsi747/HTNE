""" Name: Ali Shamsi
Project for HTNE
Prototype budgeting device"""

choice = 0
fifty = 0.0
thirty = 0.0
twenty = 0.0

choice = input("Hello, what would you like to do?\n1. Record income\n2. Record expense\n3. View Balances\n")

if choice == "1":
    income = input("Please type your income: ")
    income = float(income)
    
    fifty += income*0.5
    thirty += income*0.3
    twenty += income*0.2
    
    print("You now have:" + str(fifty) + "$ in savings, " + str(thirty) + "$ in essential spending, and " + str(twenty) + "$ in leisure spending. Good Job!")

elif choice == "2":
    amount = input("How much did you spend?: ")
    amount = float(amount)
    
    category = input("What category does this item fall into?\n1. Essential items\n2. Leisure spending")
    
    if category == "1":
        thirty-=amount
        print("You now have " + str(thirty) + "$ remaining for essential spending")
    elif category == "2":
        twenty -= amount
        print("You now have " + str(twenty) + "$ remaining for leisure spending")

elif choice == "3":
    print("You balances are: " + str(fifty) + "$ in savings" + str(thirty) + "$ in essential spending, and " + str(twenty) + "$ in leisure spending. Good Job!")