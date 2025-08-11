# Primer: Enostavna "konzola" za računanje plače z bonusom
print("Salary Calculator")
# Vprašamo uporabnika za osnovno plačo (integer ali float)
base_salary = float(input("Vnesi osnovno plačo v evrih: "))

# Vprašamo za bonus (v %)
bonus_percent = float(input("Vnesi bonus v odstotkih: "))

# Izračunamo bonus kot decimalno vrednost
bonus = base_salary * (bonus_percent / 100)

# Izračunamo skupno plačo
total_salary = base_salary + bonus

# Izpišemo rezultate
print("Osnovna plača je:", base_salary)
print("Bonus je:", bonus)
print("Skupna plača je:", total_salary)

# Uporaba type() za prikaz tipov spremenljivk
print("Tip osnovne plače je:", type(base_salary))
print("Tip bonusa je:", type(bonus))
print("Tip skupne plače je:", type(total_salary))

"""
Zakaj ta primer?

    Uporablja osnovne tipe: float, str (iz input()), int (lahko bi tudi)

    Pokazuje konverzijo tipov (input() vrne str, zato float() za pretvorbo)

    Izračuni s spremenljivkami

    Izpis rezultatov z print()

    Uporaba type() za razumevanje tipov

    Interakcija z uporabnikom preko input()

Kako to predstaviti?

    Najprej pojasni, da so spremenljivke kot “posode” za različne vrste podatkov.

    Povej, da Python sam “ve” tip, ampak za nekatere stvari je potrebno pretvoriti (npr. input() vrne niz).

    Razloži tipe, ki jih uporabljamo tukaj: float, str, int in zakaj.

    Predvajaj kodo, da študentje vidijo, kako je program interaktiven.

    Pokaži, kako type() pomaga razumeti, kaj imajo spremenljivke za tip.

    Povej, da bomo naslednje lekcije gradili na teh osnovah in dodali bolj zapletene strukture.


"""