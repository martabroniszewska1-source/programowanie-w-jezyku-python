import requests
import argparse
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


def parse_arguments():
    parser = argparse.ArgumentParser(description="Pobiera dane o browarach z Open Brewery DB API.")

    parser.add_argument(
        '--city',
        type=str,
        default=None,
        help='Ogranicza pobierane browary do podanego miasta. Przykład: --city=San_Diego'
    )

    return parser.parse_args()


def get_breweries_from_api(per_page: int = 20, city: Optional[str] = None) -> list:
    try:
        params = {"per_page": per_page}

        if city:
            city_api_format = city.replace(' ', '_').replace('-', '_')
            params["by_city"] = city_api_format
            print(f"Pobieranie {per_page} browarów dla miasta: {city}...")
        else:
            print(f"Pobieranie {per_page} losowych browarów...")

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
    args = parse_arguments()
    city_filter = args.city

    breweries_data = get_breweries_from_api(per_page=20, city=city_filter)

    if not breweries_data:
        print("Nie udało się pobrać danych z API lub nie znaleziono browarów dla podanych kryteriów.")
        return

    breweries_objects = brewery_factory(breweries_data)

    print(f"\nPomyślnie utworzono {len(breweries_objects)} obiektów Brewery.")
    print("--- POBRANE BROWARY ---")

    for brewery in breweries_objects:
        print(brewery)


if __name__ == "__main__":
    main()