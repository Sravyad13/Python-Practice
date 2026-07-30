
def withdraw(balance,amount):
    if amount >balance:
        raise ValueError("Insufficient funds!")
    return balance-amount
try:
    withdraw(100,500)
except ValueError as e:
    print("Transaction Failed",e)            