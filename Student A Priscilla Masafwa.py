# Defining the variables 
name = input("What is yout name? ")
monthly_income = int(input(f"Hello {name} i'm your finance tracker, enter your monthly income: "))
print(f"You earn {monthly_income} ZMW every month")

total_expenses = int(input("Enter the total expenses you spent: "))

# A savings goal for the end of 12 months
Savings_Goal = monthly_income - total_expenses
print(f"You have {Savings_Goal} ZMW as your account balance")
print("Sufficient balance to save" if Savings_Goal >0 else "Insufficient balance to  save")

# The Functions
def adding_income(monthly_Income, extra_income):
  new_income = monthly_Income + extra_income
  return new_income


first_amount = int(input("Enter your monthly income earned:"))
second_amount = int(input("Enter your extra income earned:"))

print(adding_income(first_amount, second_amount))

def adding_expenses(total_expenses, extra_expenses):
  new_expenses= total_expenses + extra_expenses
  return new_expenses


first_value = int(input("Enter your total expenses spent:"))
second_value = int(input("Enter your extra expenses spent:"))

print(adding_expenses(first_value, second_value))





