import products
import store


def start(best_buy):
    """Startet die interaktive Benutzeroberfläche für den Store."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # Alle aktiven Produkte anzeigen
            all_products = best_buy.get_all_products()
            print("------")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

        elif choice == "2":
            # Gesamte Menge im Store anzeigen
            total = best_buy.get_total_quantity()
            print(f"Total amount in store: {total}")

        elif choice == "3":
            all_products = best_buy.get_all_products()
            shopping_list = []

            # Liste NUR HIER einmal anzeigen
            print("Available products:")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")

            print("When you want to finish your order, leave the product number empty.")

            while True:
                prod_idx = input("Which product # do you want? ")
                if prod_idx == "":
                    break

                amount = input("Amount? ")

                try:
                    idx = int(prod_idx) - 1
                    qty = int(amount)

                    if 0 <= idx < len(all_products):
                        shopping_list.append((all_products[idx], qty))
                        print("Added to cart!")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Error: Please enter valid numbers.")

            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"********\nOrder made! Total cost: {total_price}\n********")
                except Exception as e:
                    print(f"Error during order: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    # UI starten
    start(best_buy)