


# Importa el módulo `io`
import io

# Abre el archivo en modo de lectura
with io.open("chords.txt", "r") as f:

    # Lee el contenido del archivo
    content = f.read()

# Imprime el contenido del archivo


lineas=content.split("\n")




palabras = content.split(" ")
print(palabras)

Palabras_pares = " ".join(palabras[::2])

print(Palabras_pares)