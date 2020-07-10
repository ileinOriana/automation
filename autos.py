'''
Dada una concesionaria de autos, un cliente va a solicitar un presupuesto,
debe preguntarsele:

*Nombre y apellido del comprador.
*Marca
*Puertas
*Color

Marcas posibles y sus precios:
1. Ford: $100000
2. Chevrolet: $120000  
3. Fiat: $80000

Por la cantidad de puertas se añade un precio: 
2: $50000
4: $65000
5: $78000

Dependiendo del color, se deben sumar:
1. Blanco: $10000
2. Azul: $20000
3. Negro: $30000

'''

car_value = 0
client_name = ""

def client_full_name():
    client_name = str(input('Indique nombre y apellido, por favor: '))
    return client_name

def car_brand_budget():
    car_brand = int(input('Marque 1 si desea un Ford, 2 si desea un Chevrolet o 3 si desea un Fiat: '))
    if car_brand == 1:
        return 100000
    elif car_brand == 2:
        return 120000
    elif car_brand == 3:
        return 80000
    print(' El auto de esa marca vale ', car_brand, 'pesos' )

def car_door_budget():
    car_doors = int(input('¿Desea 2, 4 o 5 puertas?: '))
    if car_doors == 2: 
        return 50000
    elif car_doors == 4:
        return 65000
    elif car_doors == 5:
        return 78000
    print ('Con ese número de puertas vale', car_doors, 'pesos')

def car_color_budget():
    car_color = int(input('Marque 1 para el color blanco, 2, para el color azul, 3 para el color negro: '))
    if car_color == 1:
        return 10000
    elif car_color == 2:
        return 20000
    elif car_color == 3:
        return 30000
    print('Ese color tiene un valor de ', car_color)

def car_total_price():
    amount = car_value
    print(client_name, 'El costo del auto es de', car_value, 'pesos')


client_full_name()
car_brand_budget()
car_door_budget()
car_color_budget()

car_total_price()





