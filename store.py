import products


class Store:
    def __init__(self, products): # 'products' ist das Argument, das übergeben wird
        # Hier wird die Instanzvariable definiert:
        self.products = products

    def add_product(self, product):
        """Fügt ein Produkt zum Store hinzu."""
        self.products.append(product)

    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        # Hier greifst du auf self.products zu:
        for prod in self.products:
            total += prod.get_quantity()
        return total

    def get_all_products(self):
        """Gibt eine Liste aller aktiven Produkte zurück."""
        return [prod for prod in self.products if prod.is_active()]

    def order(self, shopping_list) -> float:
        """
        Verarbeitet eine Bestellung (Liste von Tupeln: (Produkt, Menge)).
        Gibt den Gesamtpreis zurück.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            # Wir nutzen die buy-Methode der Product-Klasse
            # Diese kümmert sich bereits um Bestandsprüfung und Preiskalkulation
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Fehler bei Bestellung von {product.name}: {e}")
                raise e  # Wir werfen den Fehler weiter, damit der User weiß, dass die Order scheiterte

        return total_price


def main():
    # Setup der Produkte
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Store Instanz erstellen
    best_buy = Store(product_list)

    # Aktive Produkte holen
    store_products = best_buy.get_all_products()

    # Tests aus der Aufgabenstellung
    print(f"Gesamtmenge im Lager: {best_buy.get_total_quantity()}")

    try:
        # Bestellt 1x MacBook und 2x Bose Earbuds
        order_cost = best_buy.order([(store_products[0], 1), (store_products[1], 2)])
        print(f"Bestellkosten: {order_cost} Euro.")
    except Exception as e:
        print(f"Bestellung konnte nicht abgeschlossen werden: {e}")


if __name__ == "__main__":
    main()