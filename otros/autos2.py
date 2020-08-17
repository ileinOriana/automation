def calcular_precio(marca, puertas, color, ventas):
    print(marca, puertas, color, ventas)
    marcas = {'ford': 100000, 'chevrolet': 120000, 'fiat': 80000}
    print(marcas)
    colores = {'blanco': 20000, 'azul': 30000, 'negro': 35000}
    print(colores)
    puertas = {2: 5000, 4:65000, 5:78000}
    print(puertas)
    precio = marcas[marca] + colores[color] + puertas[puerta]
    if ventas > 5 and ventas < 11:
        precio = precio * 0.9 
    elif ventas > 10 and ventas <51:
        precio = precio *0.85
    elif ventas > 50:
        precio = precio * 0.82
    return precio


mas_clientes = 'si'
ventas = []
marcas = ['ford', 'chevrolet', 'fiat']
puertas = [2, 4, 5]
colores = ['blanco', 'azul', 'negro']

while mas_clientes == 'si':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    marca = ''
    puerta = 0 
    color = ''
    while marca not in marcas:
        marca = input('Ingrese marca: ').lower()
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de puertas: '))
    while color not in colores:
        color = input('Ingrese color: ')
    
    ventas.append({'nombre': nombre, 'apellido': apellido, 'marca': marca, 'puertas': puerta, 'color': color})
    mas_clientes = input('¿Hay más clientes?: ')

largo = len(ventas)

for venta in ventas: 
    precio = calcular_precio(marca, puerta, color, largo)
    print("La persona: " + venta['nombre'] + " " + venta['apellido'] + "compró un auto marca" + venta['marca'] +
    str(venta['puertas']) + "puertas y color" + venta['color'] + "con un precio de "+ str(precio))
