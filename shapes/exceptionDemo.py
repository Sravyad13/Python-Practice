
age=int(input("Enter a age"))

try:
    print(100/age)
    res =int("abc")
except (ValueError,ZeroDivisionError) as e:
      print("Error Details",e)
else:
    print("Else block1")
finally:
    print("Done Processing")    