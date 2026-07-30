age = 22

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "Teenager"
elif age >= 20 and age <= 59:
    category = "Adult"
else:
    category = "Senior citizen"

print("Age category:", category)