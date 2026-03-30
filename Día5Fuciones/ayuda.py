dic = {'clave1': 10, 'clave2': 20, 'clave3': 5}

dic.popitem() # Elimina el último elemento agregado al diccionario
print(dic) # Imprime el diccionario después de eliminar el último elemento

# para PyCharm hay ayudas, en mi casi Copilot

# cntrl + espacio para ver las opciones de autocompletado
# cntrl click para ir a la definición de una función o variable
# cntrl + shift + F10 para ejecutar el código


a = dic.pop('clave1') # Elimina el elemento con la clave 'clave1' y devuelve su valor
print(a) # Imprime el valor eliminado, que es 10
print(dic) # Imprime el diccionario después de eliminar la clave 'clave1'",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
cadena = cadena.lstrip() # Elimina los espacios en blanco al inicio de la cadena
print(cadena) # Imprime la cadena después de eliminar los espacios en blanco al inicio
cadena = cadena.lstrip(',:%_#') # Elimina los caracteres ',:%_#' al final de la cadena
print(cadena) # Imprime la cadena después de eliminar los caracteres ',:%_#' al final


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3, "naranja") # Inserta "naranja" en la posición 4 de la lista
print(frutas) # Imprime la lista de frutas después de insertar "naranja"

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

disjuntas = marcas_smartphones.isdisjoint(marcas_tv) # Verifica si los conjuntos no tienen elementos en común
print(disjuntas) # Imprime True si son disjuntos, de lo contrario False
