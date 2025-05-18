product_name,price,availability = map(str,input().split())
if product_name > 50:
    print("Product name is greater than 50.")
elif float(price) < 0:
    print("Price is less than 0.")
elif availability not in ["True", "False"]:
    print("Availability should be either 'True' or 'False'.")
else:
    print(f"Product Name: {product_name}")
    print(f"Price: {float(price):.2f}")
    print(f"In Stock: {availability}")