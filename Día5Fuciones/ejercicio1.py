def devolver_distiintos(a,b,c):
   suma = a + b + c # Calcula la suma de los tres números
   lista = [a, b, c] # Crea una lista con los tres números

   if suma  > 15:
         return max(lista) # Si la suma es mayor a 15, devuelve el número más grande de la lista utilizando la función max()
   elif suma < 10:
         return min(lista) # Si la suma es menor a 10, devuelve el número más pequeño de la lista utilizando la función min()
   else:
         lista.sort() # Si la suma está entre 10 y 15 (inclusive), ordena la lista de números utilizando el método sort()
         return lista[1] # Devuelve el número del medio de la lista ordenada,
   
#devolver_distiintos(5, 3, 5) # Llama a la función devolver_distiintos con los argumentos 5, 3 y 2, devuelve el número más grande de la lista ya que la suma es mayor a 15
print(devolver_distiintos(5, 3, 24)) # Imprime el resultado de la función devolver_distiintos con los argumentos 5, 3 y 2,
