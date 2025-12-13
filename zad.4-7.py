import requests
from typing import List, Optional

API_URL = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:
    def __init__(
            self,
            name: str,
            brewery_type: str,
            city: str,
            state: str,
            country: str,
            phone: Optional[str],
            website_url: Optional[str]
    ):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        phone_info = f"Telefon: {self.phone}" if self.phone else "Telefon: Brak"
        website_info = f"Strona: {self.website_url}" if self.website_url else "Strona: Brak"

        return (
            f"--- BROWAR: {self.name.upper()} ---\n"
            f"  Typ: {self.brewery_type.capitalize()}\n"
            f"  Lokalizacja: {self.city}, {self.state}, {self.country}\n"
            f"  {phone_info}\n"
            f"  {website_info}\n"
        )


def get_breweries_from_api(per_page: int = 20) -> list:
    try:
        params = {"per_page": per_page}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas łączenia z API: {e}")
        return []


def brewery_factory(breweries_data: list) -> List[Brewery]:
    brewery_objects = []
    for data in breweries_data:
        brewery = Brewery(
            name=data.get('name', 'Brak Nazwy'),
            brewery_type=data.get('brewery_type', 'Nieznany'),
            city=data.get('city', 'Nieznane Miasto'),
            state=data.get('state', 'Nieznany Stan'),
            country=data.get('country', 'Nieznany Kraj'),
            phone=data.get('phone'),
            website_url=data.get('website_url')
        )
        brewery_objects.append(brewery)

    return brewery_objects


def main():
    breweries_data = get_breweries_from_api(per_page=20)

    if not breweries_data:
        print("Nie udało się pobrać danych z API. Zakończenie skryptu.")
        return

    breweries_objects = brewery_factory(breweries_data)

    print(f"\nPomyślnie utworzono {len(breweries_objects)} obiektów Brewery.\n")
    print("--- POBRANE BROWARY ---")

    for brewery in breweries_objects:
        print(brewery)


if __name__ == "__main__":
    main()