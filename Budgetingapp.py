""" Name: Ali Shamsi
Project for HTNE
Prototype budgeting device"""

choice = 0
fifty = 0.0
thirty = 0.0
twenty = 0.0

choice = input("Hello, what would you like to do?\n1. Record income\n2. Record expense\n")

if choice == "1":
    income = input("Please type your income: ")
    income = float(income)
    
    fifty += income*0.5
    thirty += income*0.3
    twenty += income*0.2
    
    print("You now have:" fifty "$ in savings, " thirty "$ in [], and " twenty "$ in []. Good Job!")

elif choice == "2":
    pass