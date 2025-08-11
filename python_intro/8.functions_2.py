def pozdrav(ime, priimek=""):
    if priimek:
        return f"Živjo, {ime} {priimek}!"
    return f"Živjo, {ime}!"

def vsota(*stevilke):
    total = 0
    for stevilo in stevilke:
        total += stevilo
    return total

def podatki_o_osebi(ime, starost, **lastnosti):
    info = f"Oseba {ime}, star {starost} let.\n"
    for kljuc, vrednost in lastnosti.items():
        info += f"- {kljuc}: {vrednost}\n"
    return info

def fib(n):
    """Rekurzivna funkcija za n-ti Fibonacci člen."""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Uporaba funkcij
print(pozdrav("Niko", "Korošec"))
print(pozdrav("Ana"))

print("Vsota:", vsota(1, 3, 5, 7, 9))

print(podatki_o_osebi("Marko", 30, poklic="inženir", mesto="Ljubljana", hobi="kolesarjenje"))

print("10. Fibonacci člen je:", fib(10))


"""
Razlaga:

    Funkcije so koščki kode, ki jih lahko večkrat uporabimo z različnimi vhodnimi podatki (argumenti).

    Parametri lahko imajo privzete vrednosti, kar pomeni, da jih ni treba vedno podati.

    Z *args lahko funkcija sprejme poljubno število nepodpisanih argumentov (npr. več števil, ki jih seštejemo).

    Z **kwargs lahko funkcija sprejme poljubno število argumentov kot ključ-vrednost pare (npr. dodatne podatke o osebi).

    Rekurzija pomeni, da se funkcija kliče sama – uporabna je pri reševanju problemov, ki jih lahko razdelimo na manjše enake dele (npr. izračun Fibonacci števila).

    Funkcije nam pomagajo, da je koda bolj urejena, pregledna in ponovno uporabna.
"""