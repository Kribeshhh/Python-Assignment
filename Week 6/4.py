class ShoppingCart:
    def __init__(self):
        self.items = []

    def total_price(self):
        total = 0

        for item in self.items:
            total += item["price"]

        return total


cart = ShoppingCart()

for i in range(5):
    print(f"\nEnter Item {i+1}")
    name = input("Item Name: ")
    price = float(input("Price: "))

    cart.items.append({
        "name": name,
        "price": price
    })

print("\nTotal Price:", cart.total_price())