
try:
    file =open("data.txt","r")
        print("File is found")
    try:    
        value = int(file.read())
        print(value)
    except ValueError:
        print("Value error")    
except FileNotFoundError:
    print("File not found")
