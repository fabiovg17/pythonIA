'''
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar 
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar 
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de 
estas opciones que tenemos aquí: 
1.  La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que 
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido. 
2.  En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que 
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va 
a crear ese archivo en el lugar correcto.  
3.  La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar 
una carpeta nueva con ese nombre. 
4.  La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va 
a eliminar 
5.  La opción 5, le va a preguntar qué categoría quiere eliminar 
6.  Finalmente, la opción 6 simplemente va a finalizar la ejecución del código. 
Este programa tiene algunas cuestiones importantes a considerar: 
  Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le 
va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se 
va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo 
el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se 
cumpla la condición de que la elección del usuario sea 6 
  Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la 
pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con 
system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero. 
  Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio 
vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con 
los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los 
métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo. 
Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los 
métodos, pero recuerda que también es importante que a medida que avanzamos vayas 
aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del 
programador en el mundo en que vivimos. 
  Utiliza  muchas  funciones,  todas  las  que  creas  necesario.  Las  funciones  ayudan  a 
compartir, mentalizar el código y hacerlo mucho más dinámico, ordenado, repetible y 
más fácil de mantener. 
  Recuerda comenzar con un diagrama de flujos o un gráfico hecho a mano que te permita 
visualizar con más facilidad el árbol de decisiones que necesitas ejecutar en tu código. 
Sin eso te vas a enredar más rápido de lo que crees y se te va a complicar bastante.  
  Y, por último, no te frustres si no logras hacerlo o completarlo. Si logras hacer una parte, 
un par de funciones, algunas cosas sí y otras no, está muy bien. Siempre estamos 
aprendiendo y parte de aprender es no saber. 
''' 

from pathlib import Path

base = Path.home()  # para obtener el directorio home del usuario
print(base)  # para mostrar el directorio home del usuario

ruta = Path(base, "Recetas")  # para unir el directorio home con la carpeta Recetas
print(ruta)

def contar_recetas(ruta):
    categorias = [categoria for categoria in ruta.iterdir() if categoria.is_dir()]  # para obtener las categorías de recetas en la carpeta Recetas utilizando iterdir() y is_dir()
    total_recetas = sum(len(list(categoria.glob("*.txt"))) for categoria in categorias)  # para contar el total de recetas en todas las categorías utilizando glob() para buscar archivos con extensión .txt
    return total_recetas

def mostrar_menu():
    print("Bienvenido al programa de recetas")
    print(f"El directorio de recetas se encuentra en: {ruta}")
    total_recetas = contar_recetas(ruta)
    print(f"Hay un total de {total_recetas} recetas en la carpeta Recetas")
    print("Por favor, elige una opción:")
    print("1. Leer una receta")
    print("2. Crear una nueva receta")
    print("3. Crear una nueva categoría")
    print("4. Eliminar una receta")
    print("5. Eliminar una categoría")
    print("6. Salir")   

mostrar_menu()

def leer_receta():
    categoria = input("¿Qué categoría quieres elegir? (carnes, ensaladas, etc.) ")
    opciones_recetas = [receta.stem for receta in (ruta / categoria).glob("*.txt")]
    if not opciones_recetas:
        print("No hay recetas disponibles en esta categoría.")
        return
    print("Recetas disponibles:")
    for i, opcion in enumerate(opciones_recetas, 1):
        print(f"{i}. {opcion}")
    while True:
        try:
            seleccion = int(input("Selecciona el número de la receta que quieres leer: "))
            if 1 <= seleccion <= len(opciones_recetas):
                receta = opciones_recetas[seleccion - 1]
                break
            else:
                print("Por favor, selecciona un número válido.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
    opciones_recetas = [receta.stem for receta in (ruta / categoria).glob("*.txt")]  # para obtener las opciones de recetas disponibles en la categoría utilizando glob() para buscar archivos con extensión .txt y stem para obtener el nombre de la receta sin la extensión
    if receta not in opciones_recetas:  # para verificar si la receta elegida por el usuario está disponible en la categoría utilizando una lista de opciones de recetas
        print("La receta no existe. Por favor, verifica el nombre de la categoría y la receta.")
        return
    ruta_receta = ruta / categoria / f"{receta}.txt"  # para construir la ruta de la receta utilizando el nombre de la categoría y el nombre de la receta con extensión .txt
    if ruta_receta.exists():  # para verificar si la receta existe utilizando exists()
        print(ruta_receta.read_text())  # para leer el contenido de la receta utilizando read_text()
    else:
        print("La receta no existe. Por favor, verifica el nombre de la categoría y la receta.")

def crear_receta():
    categoria = input("¿Qué categoría quieres elegir? (carnes, ensaladas, etc.) ")
    receta = input("¿Qué receta quieres crear? ")
    contenido = input("Escribe el contenido de la receta: ")
    ruta_receta = ruta / categoria / f"{receta}.txt"  # para construir la ruta de la nueva receta utilizando el nombre de la categoría y el nombre de la receta con extensión .txt
    if not ruta_receta.parent.exists():  # para verificar si la categoría existe utilizando parent.exists()
        print("La categoría no existe. Por favor, crea la categoría antes de crear la receta.")
        return
    ruta_receta.write_text(contenido)  # para escribir el contenido de la nueva receta utilizando write_text()
    print(f"La receta '{receta}' ha sido creada en la categoría '{categoria}'.")    

def crear_categoria():
    categoria = input("¿Qué categoría quieres crear? ")
    ruta_categoria = ruta / categoria  # para construir la ruta de la nueva categoría utilizando el nombre de la categoría
    if ruta_categoria.exists():  # para verificar si la categoría ya existe utilizando exists()
        print("La categoría ya existe. Por favor, elige otro nombre.")
        return
    ruta_categoria.mkdir()  # para crear la nueva categoría utilizando mkdir()
    print(f"La categoría '{categoria}' ha sido creada.")

def eliminar_receta():
    categoria = input("¿Qué categoría quieres elegir? (carnes, ensaladas, etc.) ")
    receta = input("¿Qué receta quieres eliminar? ")
    ruta_receta = ruta / categoria / f"{receta}.txt"  # para construir la ruta de la receta a eliminar utilizando el nombre de la categoría y el nombre de la receta con extensión .txt
    if ruta_receta.exists():  # para verificar si la receta existe utilizando exists()
        ruta_receta.unlink()  # para eliminar la receta utilizando unlink()
        print(f"La receta '{receta}' ha sido eliminada de la categoría '{categoria}'.")
    else:
        print("La receta no existe. Por favor, verifica el nombre de la categoría y la receta.")

def eliminar_categoria():   
    categoria = input("¿Qué categoría quieres eliminar? ")
    ruta_categoria = ruta / categoria  # para construir la ruta de la categoría a eliminar utilizando el nombre de la categoría
    if ruta_categoria.exists():  # para verificar si la categoría existe utilizando exists()
        for receta in ruta_categoria.glob("*.txt"):  # para eliminar todas las recetas dentro de la categoría utilizando glob() para buscar archivos con extensión .txt
            receta.unlink()  # para eliminar cada receta utilizando unlink()
        ruta_categoria.rmdir()  # para eliminar la categoría utilizando rmdir()
        print(f"La categoría '{categoria}' y todas sus recetas han sido eliminadas.")
    else:
        print("La categoría no existe. Por favor, verifica el nombre de la categoría.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la opción que deseas ejecutar: ")
        if opcion == "1":
            leer_receta()
        elif opcion == "2":
            crear_receta()
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            eliminar_receta()
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            print("¡Gracias por usar el programa de recetas! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 6.")





