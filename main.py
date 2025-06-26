"""Probando trabajo conjunto"""
mensaje = "Esto es una prueba"
print(mensaje)

for e in mensaje:
    print(e)

print()
i = 0
for e in mensaje.replace(" ", ""):
    i += 1
    print(e.rjust(i))



