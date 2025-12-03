def pomnoz_liczby(lista_liczb):
    wynik=[]
    for liczba in lista_liczb:
        wynik.append(liczba*2)

    return wynik

print(pomnoz_liczby([1, 2, 3, 4, 5]))