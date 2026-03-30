#tuplas
precios_cafe = [('americano', 1.5), ('capuchino', 2.0), ('latte', 2.5)]

for tipo, precio in precios_cafe:
    print(f"El precio del {tipo} es {precio} euros.")   

precios_cafe = [('americano', 1.5), ('capuchino', 2.0), ('latte', 2.5)]

def cafe_mas_caro(precios):
    cafe_mas_caro = max(precios, key=lambda x: x[1]) # Utiliza la función max con una función lambda para encontrar el café más caro en la lista de precios
    return cafe_mas_caro # Devuelve el café más caro encontrado

cafe_mas_caro(precios_cafe) # Llama a la función cafe_mas_caro con el argumento precios_cafe, devuelve el café más caro en la lista de precios
print(cafe_mas_caro(precios_cafe)) # Imprime el resultado de la función cafe_mas_caro con el argumento precios_cafe, que es el café más caro en


#cafe más barato utilizando un for para recorrer la lista de precios y comparar cada precio con el precio menor encontrado hasta ahora, actualizando el café más barato si se encuentra un precio menor.
precios_cafe = [('americano', 1.5), ('capuchino', 2.0), ('latte', 2.5)]
def cafe_mas_barato(precios):
   precio_menor = 0
   cafe_mas_barato = ''

   for tipo, precio in precios:
       if precio_menor == 0 or precio < precio_menor: # Verifica si el precio actual es menor que el precio menor encontrado hasta ahora
           precio_menor = precio # Si es así, actualiza el precio menor con el precio actual
           cafe_mas_barato = tipo # Actualiza el café más barato con el tipo de café actual
       else:
           pass
        
          
   return (cafe_mas_barato,precio_menor) # Devuelve el café más barato encontrado


cafe_mas_barato(precios_cafe) # Llama a la función cafe_mas_barato con el argumento precios_cafe, devuelve el café más barato en la lista de precios
print(cafe_mas_barato(precios_cafe)) # Imprime el resultado de la función cafe_mas_barato con el argumento precios_cafe, que es el café más barato en
