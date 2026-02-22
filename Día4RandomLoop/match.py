
serie = "N-02"

if serie == "N-01":
    print("La serie es N-01")
elif serie == "N-02":
    print("La serie es N-02")
elif serie == "N-03":
    print("La serie es N-03")
else:
    print("La serie no es ni N-01 ni N-02") 


#match es similar a switch en otros lenguajes de programación, pero con una sintaxis diferente. Se utiliza para comparar un valor con varios patrones posibles y ejecutar el bloque de código correspondiente al primer patrón que coincida. En este caso, se compara la variable "serie" con los valores "N-01", "N-02" y "N-03". Si ninguno de los patrones coincide, se ejecuta el bloque de código bajo el caso "_", que actúa como un caso por defecto.
match serie:
    case "N-01":
        print("La serie es N-01")
    case "N-02":
        print("La serie es N-02")
    case "N-03":
        print("La serie es N-03")
    case _:
        print("La serie no es ni N-01 ni N-02")

cliente = {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Buenos Aires'}

pelicula = {'titulo': 'Inception', 'ficha_tecnica' : 
            {'protagonista':'Keanu', 'director': 'Christopher Nolan'},
             'año': 2010}    
elmentos = [cliente, pelicula, 'libro']

for e in elmentos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}:
            print(f"El cliente se llama {nombre}, tiene {edad} años y vive en {ciudad}.")
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}, 'año': año}:
            print(f"La película se llama {titulo}, protagonizada por {protagonista}, dirigida por {director} y estrenada en {año}.")
        case _:
            print("El elemento no es ni un cliente ni una película.")

 


