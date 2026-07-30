cart_amount = 1200

if cart_amount >= 1000:
    discount = 20
elif cart_amount >= 500:
    discount = 10
else:
    discount = 0

discount_amount = cart_amount * discount / 100
final_amount = cart_amount - discount_amount

print("Original amount:", cart_amount)
print("Discount:", discount, "%")
print("Final amount:", final_amount)