def wyswietl_co_drugi(lista_liczb):
    for element in lista_liczb[::2]:
        print(element)


liczby = list(range(21, 30))

wyswietl_co_drugi(liczby)
