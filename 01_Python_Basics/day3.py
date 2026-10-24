# Day 3: Lists (Collection of Data)

# 1. Defining a list of client project budgets in USD
budgets =[100.0, 230.0, 40.0, 70.0, 10.0]

# Printing The whole List and its length
print("Client Project Budgets: ",budgets)
print("Total Projects:",len(budgets))

# 2. Aceesing items from the list using index
print("First item:", budgets[0])
print("Last item:", budgets[-1])

# 3. Adding a New project budget to the list Dynamically ( append method always adds at the end)
budgets.append(2234.0)
print("Updated Project Budgets: ", budgets)

# 4. Adding a New project budget to the list Dynamically ( insert method can add at any position)
# Forr adding at index 0
budgets.insert(0, 999.0)

# For adding at index 2
budgets.insert(2, 500.0)

# 5. Automating with for loops (processing each budget in the list)
print("\n___processing Budget Calculations___")
for single_budget in budgets:
    tax= single_budget*0.10
    final_amount= single_budget+tax  
    print(f"Orignal: ${single_budget}| Tax: ${tax} | Total: Final Amount ${final_amount}")

    # TEST
    approved_projects= []
    for budget in budgets:
        if(budget >=50):
            approved_projects.append(budget)
    print(approved_projects)