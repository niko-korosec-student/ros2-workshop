sadje = ['jabolko', 'banana', 'češnja']

print("Izpis sadja s for zanko:")
for sadez in sadje:
    print(sadez)

print("\nUporaba range() za izpis števil od 0 do 4:")
for i in range(5):
    print(i)

print("\nUporaba enumerate() za indeks in vrednost:")
for indeks, sadez in enumerate(sadje):
    print(f"Na indeksu {indeks} je sadež: {sadez}")


"""
Razlaga:

    Prvi for gre skozi vsak element v seznamu sadje in izpiše ime sadeža.

    Drugi for uporablja range(5), ki generira števila od 0 do 4 in jih izpiše.

    Tretji for uporablja enumerate(), da hkrati dobi indeks elementa in njegovo vrednost ter ju lepo izpiše.
"""