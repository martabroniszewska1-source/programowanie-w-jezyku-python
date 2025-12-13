class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Adres: {self.address} | Powierzchnia: {self.area} m^2 | "
            f"Pokoje: {self.rooms} | Cena: {self.price} PLN"
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"--- DOM ---"
            f"\nAdres: {self.address}"
            f"\nPowierzchnia: {self.area} m^2, Pokoje: {self.rooms}"
            f"\nCena: {self.price} PLN"
            f"\nRozmiar działki (plot): {self.plot} m^2"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"--- MIESZKANIE ---"
            f"\nAdres: {self.address}"
            f"\nPowierzchnia: {self.area} m^2, Pokoje: {self.rooms}"
            f"\nCena: {self.price} PLN"
            f"\nPiętro (floor): {self.floor}"
        )


# TWÓRZENIE INSTANCJI
dom_jednorodzinny = House(
    area=150, rooms=5, price=750000, address="ul. Dębowa 5, 30-001 Kraków", plot=800
)

mieszkanie_w_bloku = Flat(
    area=65,
    rooms=3,
    price=420000,
    address="al. Niepodległości 12/A, 50-100 Wrocław",
    floor=3,
)

# WYŚWIETLANIE WYNIKÓW
print("### WYŚWIETLANIE NIERUCHOMOŚCI ###")
print(dom_jednorodzinny)
print("\n" + "=" * 30 + "\n")
print(mieszkanie_w_bloku)
