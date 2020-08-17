
autos = ['Ford', 'Chevrolet', 'Fiat', 'Honda']

print(autos[2])
print(autos[-1])
print(autos[1:3])
#Va desde el 1 hasta el 2, sin contar el 3

autos.append('Toyota')
print(autos)

autos.insert(2, 'Ferrari')
#Esto agrega en el subíndice 2 al elemento 'Ferrari' 
print(autos)
print(len(autos))

#Para eliminar uso el sufijo 'del'
del autos[0]
print(autos)

#Si quiero sustituir un elemento por otro de la lista
autos[2] = 'Porsche'
print(autos)

print('Honda' in autos)