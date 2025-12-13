def polacz_i_przetworz(lista1: list, lista2: list) -> list:
    polaczona = lista1 + lista2  # 1. łączenie list
    bez_duplikatow = list(set(polaczona))  # 2. usuwanie duplikatów
    wynik = [x**3 for x in bez_duplikatow]  # 3. każdy element do potęgi 3
    return wynik


a = [1, 2, 3]
b = [2, 3, 4]

print(polacz_i_przetworz(a, b))
