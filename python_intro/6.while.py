print("Primer while zanke:")
i = 0
while i < 5:
    print(f"while: Število je {i}")
    i += 1

print("\nPrimer simulacije do-while zanke:")
j = 0
while True:
    print(f"do-while: Število je {j}")
    j += 1
    if not (j < 5):
        break

"""
razlaga:

    Prvi del: while zanka preveri pogoj pred izvajanjem in izpiše števila od 0 do 4.

    Drugi del: simulacija do-while zanke vedno izvede telo vsaj enkrat, nato preveri pogoj in ponovi, dokler je pogoj izpolnjen.
"""