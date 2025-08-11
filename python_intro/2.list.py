# Ustvarimo seznam z imeni študentov
students = ["Ana", "Bine", "Cilka"]

# Izpišemo začetni seznam
print("Začetni seznam študentov:", students)

# Dodamo novega študenta na konec seznama
students.append("David")
print("Po dodajanju Davida:", students)

# Vstavimo novega študenta na drugo mesto (indeks 1)
students.insert(1, "Eva")
print("Po vstavljanju Eve na indeks 1:", students)

# Odstranimo študenta z imenom 'Bine'
students.remove("Bine")
print("Po odstranitvi Bine:", students)

# Preverimo koliko študentov je na seznamu
print("Število študentov:", len(students))

# Dostopamo do prvega študenta v seznamu (indeks 0)
print("Prvi študent na seznamu:", students[0])

# Sprehodimo se po seznamu in pozdravimo vsak študent
for student in students:
    print(f"Živjo, {student}!")


"""
Razlaga

    students = ["Ana", "Bine", "Cilka"]
    To ustvari list (seznam) imen. Seznami so urejeni in lahko vsebujejo poljubne elemente (tukaj nize).

    print(...)
    Izpiše trenutno stanje seznama ali neko sporočilo.

    students.append("David")
    Funkcija append() doda element na konec seznama.

    students.insert(1, "Eva")
    Funkcija insert() vstavi element na določen indeks (tukaj na indeks 1, torej drugo mesto).

    students.remove("Bine")
    Odstrani prvi pojav elementa s tem imenom iz seznama.

    len(students)
    Vrne dolžino (število elementov) seznama.

    students[0]
    Dostop do elementa z indeksom 0 (prvi element v seznamu).

    for student in students:
    Zanka, ki gre po vseh elementih seznama in jih postopoma dodeli spremenljivki student.

    print(f"Živjo, {student}!")
    Izpis pozdrava za vsakega študenta posebej z uporabo f-stringov za lepšo interpolacijo.
"""