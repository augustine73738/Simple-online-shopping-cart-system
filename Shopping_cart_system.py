cart = []

def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart.append({"item": item, "price": price})
    print("Item added to cart")

def view_cart():
    if not cart:
        print("Cart is empty")
    else:
        total = 0
        for item in cart:
            print(item["item"], "- Price:", item["price"])
            total += item["price"]
        print("Total cost:", total)

def main():
    while True:
        print("1. Add Item")
        print("2. View Cart")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
