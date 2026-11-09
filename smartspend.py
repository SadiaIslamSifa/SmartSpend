print("====Welcome to Samrt Spend====")

name = input("Enter your name:")
budget =int (input(" Enter your monthly budget$:"))
print("Hello", name)
print("Your monthly budget is $", budget)



expense = input("Enter your expense category:")
categories = {
  "Food" :['Lunch', 'dinner','Breakfast'],
  "Transport":['Bus','Uber'],
  "Grocery": ['Milk and eggs', 'Meat', 'Vegetables'],
  "Shopping": ['Clothes', 'Shoes'],
  "Rent": ['House_rent', 'Water_bill']
}

if expense in categories:
    print ("you selected", expense)
else:
    print("Invalid Choice")
expenses = []

while True:
 expense = input("Enter expense category: ").strip().title()
 if expense not in categories:
        print("Invalid category. Try again.")
        continue
 buy = input("What is that?:")
 spend= float(input("How much did you spend?:"))

 new_expenses= {"category": expense,
               "item": buy,
               "amount": spend
         }
           
 expenses.append(new_expenses)
 again = input("Add another  expense? yes/no:").strip().lower()
 if again == "no":
    break
print (expenses)


total_spent = 0

for item in expenses:
    total_spent += item["amount"]

remaining_budget = budget - total_spent

print("Total spent: $", total_spent)
print("Remaining budget: $", remaining_budget)
if remaining_budget < 0:
    print("Warning! You exceeded your monthly budget!")
else:
    print("You are within your budget!")

print("===== Spending Summary =====")

category_totals = {}

for item in expenses:
    category = item["category"]
    amount = item["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount

for category, amount in category_totals.items():
    print(category, ": $", amount)

print("Total spent: $", total_spent)
print("Remaining budget: $", remaining_budget)