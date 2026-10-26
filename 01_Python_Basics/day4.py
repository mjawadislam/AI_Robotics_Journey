# Day 4. String Cleaning And Manipulation For Data Pipelines

#1. Handling Messy text inputs
raw_client_name = "    jawad khan      "
raw_budget_string = " $2,450"

# Stripping Extra whitespaces from ends
clean_name = raw_client_name.strip()

# Case Formatting Lower,Upper, Title
formatted_name = clean_name.title()
# Cleaning Unwanted Symbols For Numeric Extraction
clean_budget= raw_budget_string.strip().replace("$","").replace(",","")
numeric_budget= float(clean_budget)

print("Orignal Name:", repr(raw_client_name))
print("Clean Name:", clean_name)
print("Formatted Name(Title):", formatted_name)
print("Extracted Budget:", numeric_budget)

# 2. Splitting and Joining Data Records
raw_tags = "python,automation,data,robotics"

# String ko commas se tod kar List banana
skills_list = raw_tags.split(",")
print("\nParsed Skills List:", skills_list)

# List ke items ko kisi naye symbol ke sath wapas jorna
clean_tags_display = " | ".join(skills_list)
print("Formatted Tag String:", clean_tags_display)

# 3. Python Dictionaries (Structured Data Records)
client_project = {
    "client_name": " Jawad Khan",
    "budget": 3450.0,
    "skills_required": ["python", "automation"],
    "is_approved": True
}
# Accessing values through keys
print("\nClient project Name:", client_project["client_name"])
print("\nClient Project Budget:", client_project["budget"])

# Dynamic Update(adding or updating new key)
client_project["status"] = "In Progress"
client_project["budget"] = 921.0

print("\n Updated Project Records:")
print(client_project)

# 4. List of Dictionaries (Multiple Database Records)
projects = [
    {"client": "Jawad Khan", "budget": 921.0},
    {"client": "Tech Corp", "budget": 45.0},
    {"client": "Global Logistics", "budget": 350.0}
]

# Loop chalakar har project ka data read karna
print("\n--- Project Overview ---")
for proj in projects:
    print(f"Client: {proj['client']} | Budget: ${proj['budget']}")


    raw_leads = [
    {"name": "   ali khan   ", "raw_budget": " $1,200 "},
    {"name": "sara ahmed  ", "raw_budget": " $450 "},
    {"name": "  usman tariq ", "raw_budget": " $2,500 "}
]
clean_leads = []
for lead in raw_leads:
    clean_name=lead["name"].strip()
    cleaned_name=clean_name.title()

    clean_budget= lead["raw_budget"].strip().replace("$","").replace(",","")
    numeric_budget= float(clean_budget)
    clean_leads.append({"name": cleaned_name, "budget": numeric_budget})
print("\nFinal Cleaned Leads:")
print(clean_leads)