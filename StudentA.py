# Defining the variables 
name = input("What is yout name? ")
Monthly_Income = int(input(f"Hello {name} i'm your finance tracker, enter your monthly income: "))
print(f"You earn {Monthly_Income} ZMW every month")

Total_expenses = int(input("Enter the total expenses you spent: "))

# A savings goal for the end of 12 months
Savings_Goal = Monthly_Income - Total_expenses
print(f"You have {Savings_Goal} ZMW as your account balance")
print("Sufficient balance to save" if Savings_Goal >0 else "Insufficient balance to  save")

# Monthly income & extra income are assigned 1 as a default value, we will insert for the user their own in the print adding income(monthly income value, extra income value). eg print(adding_income(900, 400)) 1 assigned won't affect the add

def adding_income(Monthly_Income=1, extra_income=1):
  new_income = Monthly_Income + extra_income
  return new_income


print(adding_income())

def adding_expenses(Total_expenses=1, extra_expenses=1):
  new_expenses= Total_expenses + extra_expenses
  return new_expenses


print(adding_expenses())






