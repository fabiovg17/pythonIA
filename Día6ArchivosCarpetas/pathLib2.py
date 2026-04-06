from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas/prueba.txt')
print(carpeta.read_text())
# no se necesita abrir el archivo con open() para leer su contenido, se puede hacer directamente con el método read_text() del objeto Path.

print(carpeta.name)  # para obtener el nombre del archivo
print(carpeta.parent)  # para obtener el directorio padre del archivo
print(carpeta.suffix)  # para obtener la extensión del archivo
print(carpeta.stem)  # para obtener el nombre del archivo sin la extensión

if carpeta.exists():  # para verificar si el archivo existe
    print(f"El archivo {carpeta.stem} existe")
else:    
    print(f"El archivo {carpeta.stem} no existe")  

ruta_windows = PureWindowsPath('/Users/fabiovalverde/Documents/Aprendizaje/IA Python/Proyectos/Día6ArchivosCarpetas/prueba.txt')
print(ruta_windows)  # para mostrar la ruta en formato Windows