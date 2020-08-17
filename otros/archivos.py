'''Practica para leer y escribir archivos automatizados. 
(Ejemplo, crear usuarios y agregarlos a un txt)'''

#1 Escribir en un archivo y si el archivo existe, borrarlo y crear uno nuevo
#2 Anadir algo al final del archivo
#3 Leer algo al final del archivo
#4 Escribir en un archivo y si no existe, crearlo 

#1 w de write
#2 a de append 
#3 r de read 
#4 w+

def read_file(filename):
    nuevo_archivo = open(filename, 'r')
    print(nuevo_archivo.read())
    nuevo_archivo.close()

#Crear archivo nuevo y escribir en el mismo
def create_and_write(filename):
    nuevo_archivo = open(filename, 'w+')
    nuevo_archivo.write('Lista de mercado\n')
    nuevo_archivo.close()

#Crear otros datos en el mismo archivo
def append_samefile(filename):
    nuevo_archivo = open(filename, 'a')
    nuevo_archivo.write('Bananas\nQueso\nFiambre\nSalchichas')
    nuevo_archivo.close()


create_and_write('datos_nuevos.txt')
read_file('datos_nuevos.txt')
append_samefile('datos_nuevos.txt')
read_file('datos_nuevos.txt')

'''
def read_file(filename):
    my_file = open(filename, 'r')
    print(my_file.read())
    my_file.close() 

#Crear y escribir 
my_file = open('data.txt', 'w+')
my_file.write('Oswaldo\nIlein\nOsman')
my_file.close()

#Crear otros datos
my_file = open('data.txt', 'w')
my_file.write('Oswaldo3\nIlein4\nOsman5\n')
my_file.close()

read_file('data.txt')

my_file = open('data.txt', 'a')
my_file.write('Aldo\nRomina\nRicardo')
my_file.close()

#read_file('data.txt')
my_file = open('data.txt', 'r')
print(my_file.readlines(2))

'''