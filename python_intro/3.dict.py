oseba = {
    "ime": "Niko",          # Ustvarimo slovar z začetnimi podatki o osebi
    "starost": 25,
    "poklic": "inženir"
}

print("Podatki o osebi:", oseba)  # Izpišemo celoten slovar

oseba["lokacija"] = "Maribor"    # Dodamo nov ključ 'lokacija' z vrednostjo 'Maribor'
print("Po dodajanju lokacije:", oseba)

oseba["starost"] = 26            # Posodobimo vrednost ključa 'starost' na 26
print("Po posodobitvi starosti:", oseba)

del oseba["poklic"]              # Odstranimo ključ 'poklic' iz slovarja
print("Po odstranitvi poklica:", oseba)

for ključ, vrednost in oseba.items():  # Zanka, ki gre skozi vse ključe in vrednosti
    print(f"{ključ}: {vrednost}")       # Izpišemo posamezen ključ in pripadajočo vrednost


"""
Dictionary (slovar) v Pythonu je podatkovna struktura, ki shranjuje podatke v obliki parov ključ-vrednost. Ključ je unikaten identifikator, ki je lahko npr. niz (string), vrednost pa je lahko katerakoli Pythonova vrednost.
Razlaga primera:

    oseba = { ... }
    Ustvarili smo slovar z informacijami o osebi. Ključi so "ime", "starost" in "poklic", vrednosti pa "Niko", 25 in "inženir".

    print("Podatki o osebi:", oseba)
    Izpišemo celoten slovar.

    oseba["lokacija"] = "Maribor"
    Dodajamo nov ključ "lokacija" s pripadajočo vrednostjo "Maribor".

    oseba["starost"] = 26
    Posodobimo vrednost ključa "starost" na 26.

    del oseba["poklic"]
    Odstranimo ključ "poklic" in njegovo vrednost iz slovarja.

    for ključ, vrednost in oseba.items():
    Zanko, ki gre skozi vse pare ključ-vrednost in jih izpiše. Metoda .items() vrne vse ključe in vrednosti v slovarju.

Zakaj uporabljati slovarje?

    Omogočajo hiter dostop do vrednosti preko ključev (ne glede na položaj).

    So zelo fleksibilni za shranjevanje strukturiranih podatkov.

    Pogosto uporabljeni za konfiguracije, parametre, baze podatkov v pomnilniku itd.
"""