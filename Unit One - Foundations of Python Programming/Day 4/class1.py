Drink = float(input("What is the cost of your drink?: "))
Appetizer = float(input("What is the cost of your appetizer?: "))
Entree = float(input("What is the cost of your entree?: "))
Desert = float(input("What is the cost of your dessert?: "))
Bill = Drink + Appetizer + Entree + Desert
Tip = float(input("How much would you like to tip?: "))
BWT = Bill*Tip/100 + Bill
Total = BWT*0.13 + BWT

print(f"Your total will be ${Total}")




