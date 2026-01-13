class Product:
    def __init__(self, name, price, quantity):
        # Validierung der Eingabewerte
        if not name:
            raise ValueError("Der Name darf nicht leer sein")
        if price < 0:
            raise ValueError("Der Preis darf nicht negative sein")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negative sein")

        # Instanzvariable initialisieren
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Hier hatten wir vorhin 'activity' zu 'active' korrigiert

    def get_quantity(self) -> int:
        """Gibt die aktuelle Menge zurück"""
        return self.quantity

    def set_quantity(self, quantity):
        """Aktualisiert die Menge und deaktiviert das Produkt, falls 0 erreicht ist"""
        if quantity < 0:
            raise ValueError("Menge kann nicht negative sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Prüft, ob das Produkt aktiv ist."""
        return self.active

    def activate(self):
        """Aktiviere das Produkt"""
        self.active = True

    def deactivate(self):
        """Deaktiviere das Produkt"""
        self.active = False

    def show(self):
        """Gibt die Produktinformationen auf der Konsole aus."""
        print(f"{self.name}, price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Kauft eine Menge des Produkts und gibt den Gesamtpreis zurück."""
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss grösser als Null sein")

        if quantity > self.quantity:
            raise ValueError("Nicht genügend Bestand auf Lager!")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return float(total_price)