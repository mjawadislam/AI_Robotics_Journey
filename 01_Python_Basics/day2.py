# Day2: Data Types and Type Casting

# 1. Four Core Data Types
user_name= "Jawad" #str (string)
user_age= 20 #int (integer)
hourly_rate= 20.5 #float (decimal)
is_enrolled= True #bool (boolean)

# Printing values with their types
print(type(user_name))
print(type(user_age))
print(type(hourly_rate))
print(type(is_enrolled))

#2. Type Casting Example
str_num="50"
converted_num= float(str_num)
print(converted_num)

# Total Calculation
Total= converted_num + user_age
print("Total Sum: ", Total)

# 3. User Input & Dynamic Type Casting
client_budget=float(input("Enter client budget in USD: "))
tax_amount= client_budget * 0.10
final_total= client_budget + tax_amount
print(f"Original: ${client_budget} | Tax (10%): ${tax_amount} | Final Total: ${final_total}")

# 4. Conditional Logic Client-Filter System
project_budget= float(input("Enter project budget in USD: "))
if project_budget >=100:
    print("Project is Good")
elif project_budget >=30:
    print("Project is Average")
else:
    print("Project is Poor")
