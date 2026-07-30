logged_in = False
user_role = "admin"

if logged_in:
    if user_role == "admin":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Login required")