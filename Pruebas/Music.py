


# Importa el módulo `io`
import io

# Abre el archivo en modo de lectura
with io.open("chords.txt", "r") as f:

    # Lee el contenido del archivo
    content = f.read()

# Imprime el contenido del archivo
print(content)
