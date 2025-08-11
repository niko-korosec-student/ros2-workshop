def pozdrav(ime):
    return f"Živjo, {ime}!"

def vsota(a, b):
    return a + b

# Klic funkcij
print(pozdrav("Niko"))
rezultat = vsota(5, 7)
print(f"Vsota 5 in 7 je: {rezultat}")


"""
Razlaga:

    Funkcije definiramo z def in ime funkcije.

    V oklepajih so parametri (lahko jih ni).

    return pošlje vrednost nazaj tja, kjer smo funkcijo poklicali.

    Funkcije so super za organizacijo kode, ponovno uporabo in razbijanje problema na manjše dele.
"""