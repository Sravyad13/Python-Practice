from datetime import datetime
now=datetime.now()
print("Current time",now)
print("Current year",now.year)
print("Formatted",now.strftime("%d-%m-%Y"))
