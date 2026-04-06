from pathlib import Path
# Path es una clase que representa una ruta de archivo o directorio en el sistema de archivos. 
# Permite manipular rutas de manera más intuitiva y ofrece una interfaz orientada a objetos 
# para trabajar con archivos y directorios.
base = Path.home()  # para obtener el directorio home del usuario
print(base)  # para mostrar el directorio home del usuario
documentos = base / 'Documents'  # para unir el directorio home con la carpeta Documents
print(documentos)  # para mostrar la ruta de la carpeta Documents
proyecto = documentos / 'Aprendizaje' / 'IA Python' / 'Proyectos' / 'Día6ArchivosCarpetas'  # para unir la ruta de la carpeta Documents con la ruta del proyecto
print(proyecto)  # para mostrar la ruta del proyecto
guia = Path("Barcelona", "Sagrada Familia.txt")
print(guia)  # para mostrar la ruta de la guía turística  

guia2 = Path(base, "Barcelona", "Sagrada Familia.txt")
print(guia2)  # para mostrar la ruta de la guía turística utilizando el directorio home del usuario como base

#crear una ruta más larga utilizando Path() dentro de Path() para mayor claridad
guia2 = Path(base, "Europa", "España", Path("Barcelona", "Sagrada Familia.txt"))
print(guia2)  # para mostrar la ruta de la guía turística utilizando el directorio home del usuario como base y uniendo varias partes de la ruta con Path() dentro de Path() para mayor claridad

guia3 = guia2.with_name("Parque Güell.txt")  # para cambiar el nombre del archivo en la ruta utilizando with_name()
print(guia3)  # para mostrar la nueva ruta con el nombre del archivo cambiado

guia4 = guia2.with_suffix(".pdf")  # para cambiar la extensión del archivo en la ruta utilizando with_suffix()
print(guia4)  # para mostrar la nueva ruta con la extensión del archivo cambiada
print(guia2.parent)  # para mostrar el directorio padre de la ruta utilizando parent

print(guia2.stem)  # para mostrar el nombre del archivo sin la extensión
print(guia2.suffix)  # para mostrar la extensión del archivo
print(guia2.exists())  # para verificar si la ruta existe en el sistema de archivos

print(guia2.parent.parent)  # para mostrar el directorio abuelo de la ruta utilizando parent.parent


guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("**/*.txt"):  # para buscar todos los archivos con extensión .txt 
    #en la ruta y sus subdirectorios utilizando glob()
    print(txt)  # para mostrar la ruta de cada archivo encontrado

for txt in Path(guia2).rglob("*.txt"):  # para buscar todos los archivos con extensión .txt
    # en la ruta y sus subdirectorios utilizando rglob()
    print(txt)  # para mostrar la ruta de cada archivo encontrado

# guia = Path(Path.home()) #Este código busca en todo el directorio home del usuario, 
# lo cual puede ser muy lento y generar una gran cantidad de resultados. 
# Es recomendable especificar una ruta más concreta para evitar esto.

for txt in Path(guia).rglob("*.txt"):  # para buscar todos los archivos con extensión .txt
    # en la ruta y sus subdirectorios utilizando rglob()
    print(txt)  # para mostrar la ruta de cada archivo encontrado

print("----------relative-------------------")  # para separar los resultados de las búsquedas
guia6 = Path( "Europa", "España", "Barcelona", "Sagrada Familia.txt")
en_europa = guia6.is_relative_to(Path("Europa"))  # para verificar si la ruta es relativa a "Europa" utilizando is_relative_to()
print(en_europa)  # para mostrar el resultado de la verificación
en_europa = guia6.relative_to(Path("Europa"))  # para verificar si la ruta es relativa a "Europa" utilizando is_relative_to()
print(en_europa)  # para mostrar el resultado de la verificación
en_espana = guia6.is_relative_to(Path("Europa", "España"))  # para verificar si la ruta es relativa a "España" utilizando is_relative_to()
print(en_espana)  # para mostrar el resultado de la verificación
en_barcelona = guia6.is_relative_to("Barcelona")  # para verificar si la ruta es relativa a "Barcelona" utilizando is_relative_to()
print(en_barcelona)  # para mostrar el resultado de la verificación
