'''
*Nombre
*Apellido
*Nota Matematica
*Nota Lengua
*Nota geografía
*Promedio

-Los alumnos pueden dar exámenes.

La escuela también tiene profesores que tienen las siguientes características:

*Nombre
*Apellido
*Materia que enseña

-Los profesores toman exámenes y le dan al alumno una nota.

Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores 
y que el resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).
'''
import random

class Escuela():
    def __init__(self, nombre, apellido, nota_matematica, nota_lengua, nota_geografia):
        self.nombre = nombre
        self.apellido = apellido
        self.nota_matematica = 0
        self.nota_lengua = 0
        self.nota_geografia = 0

    def rendir_examen_matematica(self):
        self.nota_matematica = random.randint(0, 10)
        return self.nota_matematica
    
    def rendir_examen_lengua(self):
        self.nota_lengua = random.randint(0,10)
        return self.nota_lengua

    def rendir_examen_geografia(self): 
        self.nota_geografia = random.randint(0, 10)
        return self.nota_geografia
    
    def sacar_promedio_alumno(self, nota_matematica, nota_lengua, nota_geografia):
        promedio = (nota_matematica + nota_lengua + nota_geografia) / 3
        return promedio



    

    
    




