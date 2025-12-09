def czy_zawiera(lista: list, liczba: int) -> bool:
    return liczba in lista

mojalista = [3, 5, 7, 10]
wynik = czy_zawiera(mojalista, 5)

print(wynik)
