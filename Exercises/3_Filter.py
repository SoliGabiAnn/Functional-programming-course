# Hint: https://github.com/SoliGabiAnn/Functional-programming-course/wiki/5.-Filter#why-use-it

transactions = [
    {"id": 1, "amount": "15.50", "status": "valid"},
    {"id": 2, "amount": "0.00", "status": "invalid"},  
    {"id": 3, "amount": "100.75", "status": "valid"},  
    {"id": 4, "amount": "50.25", "status": "invalid"},  
]

# Step 1: Filter valid transactions (status="valid")
valid_transactions = filter(______, transactions) 

# Step 2: Extract and convert amounts to floats
amounts = map(______, valid_transactions) 

# Step 3: Apply 10% tax
taxed_amounts = map(______, amounts) 

# Step 4: Format as currency strings ("X zł")
formatted_amounts = map(______, taxed_amounts) 

# Convert to list and print
print(list(formatted_amounts))

'''
Expected Output:

['$17.05', '$110.83']
'''
