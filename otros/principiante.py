import random

#Tirar un dado de 5 valores 
#Si es 1, gana una flor. 
#Si es 2, gana un tatuaje. 
#Si es 3, gana un libro. 
#Si es 4, gana un viaje. 
#Si es 5, no gana nada. 

def lanzar_dados():
    value = random.randint(1, 5)
    return value

def descifrar_premio(num):
    if num == 1:
        print('ganaste una flor')       
    elif num == 2: 
        print('ganaste un tatuaje')
    elif num == 3: 
        print('ganaste un libro')
    elif num == 4: 
        print('ganaste un viaje')
    else: 
        print('no ganaste nada')

dado = lanzar_dados()
print('tu dado es ', dado)
descifrar_premio(dado)