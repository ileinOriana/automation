colores = ('Amarillo', 'Azul', 'Verde')
print(colores)

#Para acceder al subíndice dentro de una tupla
print(colores[1])

print('Verde' in colores)
#Retorna True o False porque pregunta si existe o no

#Diccionarios

usuario = {'id': 6, 'name': 'Pedro', 'age': 18, 'casado': True}
print(usuario['name'])

#Si quiero agregar algo al diccionario, funciona como en la lista 
#Y el elemento nuevo lo agregará al final, si existe, lo sustituye. 
usuario['apellido'] = 'Pérez'
print(usuario)

#Si quiero conocer todas las claves del diccionario
print(usuario.keys())

#Si quiero conoces los valores del diccionario
print(usuario.values())

if 'id' in usuario:
    print('Tiene ID')

print('-------------------')
#Para eliminar un elemento del diccionario
del usuario['apellido']
print(usuario)

#Para vacíar el diccionario 
usuario.clear()
print(usuario)