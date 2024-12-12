price=float(input("Please type in a price:"))

Dinars=price.__floor__()

Centimes=int((price-Dinars)*100)
print(f"Dinars:{Dinars}")
print(f"Centimes:{Centimes}")
