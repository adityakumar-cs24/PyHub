products = eval(input().replace("products = ",""))
unique_products = []
for product in products:
    if product not in unique_products:
        unique_products.append(product)
unique_products = tuple(unique_products)
print(unique_products)