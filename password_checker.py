password = input('Enter Password: ')

results = {}

if len(password) > 8:
    results["length"] = True
else:
    results["length"] = False

contains_digit = False

for i in password:
    if i.isdigit():
        contains_digit = True
        break
    
results["digit"] = contains_digit

contains_uppercase_char = False

for i in password:
    if i.isupper():
        contains_uppercase_char = True
        break
    
results["uppercase"] = contains_uppercase_char

print(results, results.keys(), results.values())

if all(results.values()):
    print("Strong Password")
else:
    print("Weak Password")