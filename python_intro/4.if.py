starost = 20

if starost < 18:
    print("Oseba je mladoletna.")
elif 18 <= starost < 65:
    print("Oseba je odrasla.")
else:
    print("Oseba je upokojenec.")

"""
Razlaga:

    if stavek preveri prvi pogoj (starost < 18). Če je ta pogoj resničen, se izvede koda znotraj te veje, ostali pogoji se preskočijo.

    Če prvi pogoj ni izpolnjen, program preide na elif (kar pomeni "else if") in preveri naslednji pogoj (18 <= starost < 65). Če je ta resničen, se izvede koda tukaj.

    Če nobeden od zgornjih pogojev ni resničen, se izvede else del, ki pokrije vse preostale možnosti.

    S tem lahko elegantno pokriješ več različnih primerov s prilagodljivimi pogojnimi izrazi.

Zakaj je to pomembno?

    If-elif-else nam omogoča odločanje v programu — ključna logika, ki robotu ali sistemu pove, kako naj se odzove v različnih situacijah.

    V ROS2 na primer lahko preverjamo stanje robota in se na podlagi tega odločamo, katero dejanje naj izvede.

    Brez pogojev ni dinamičnega in pametnega obnašanja programov.
"""