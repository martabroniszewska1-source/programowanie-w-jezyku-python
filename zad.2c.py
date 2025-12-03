def wyswietl_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(1, 11))

wyswietl_parzyste(liczby)
