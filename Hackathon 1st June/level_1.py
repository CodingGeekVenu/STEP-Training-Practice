m = int(input())

catalogue = {}
cart = {}

for _ in range(m):
    prod_id, price = input().split()
    catalogue[prod_id] = int(price)

k = int(input())

for _ in range(k):
    prod_id, quantity = input().split()
    quantity = int(quantity)

    if prod_id in cart:
        cart[prod_id] += quantity
    else:
        cart[prod_id] = quantity

total = 0

for prod_id in cart:
    price = catalogue[prod_id]
    quantity = cart[prod_id]        
    total += price * quantity

print(total)