class Vehiculo():
    def __init__(self, color, marca, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_inicial = 0 
        self.encendido = False

    def encender_auto(self):
        self.encendido = True
    
    def apagar_auto(self):
        self.encendido = False

    def mostrar_velocimetro(self):
        print('La velocidad inicial es de'+ str(self.velocidad_inicial) + 'de un máximo de ' + str(self.velocidad_maxima))

    def acelerar(self,velocidad):
        if self.encendido == True:
            if self.velocidad_inicial + velocidad > 180:
                self.velocidad_inicial = 180
            else:
                self.velocidad_inicial = self.velocidad_inicial + velocidad
        else:
            print('Para acelerar necesitas encender el auto')
        self.mostrar_velocimetro() #Aca estoy invocando un metodo dentro de otro metodo, lo cual está bien.

    def frenar(self, velocidad):
        if self.velocidad_inicial - velocidad < 0:
            self.velocidad_inicial = 0
        else:
            self.velocidad_inicial = self.velocidad_inicial - velocidad
        self.mostrar_velocimetro()
    
    def get_properties(self):
        return dict({"color": self.color, "marca": self.marca, "velocidad_maxima": self.velocidad_maxima})


class Camion(Vehiculo):
    def __init__(self, color, marca, velocidad_maxima, carga_maxima):
        self.carga_maxima = carga_maxima
        self.carga_actual = 0
        Vehiculo.__init__(self, color, marca, velocidad_maxima)
    
    def cargar(self, cantidad):
        self.carga_actual = self.carga_actual + cantidad
    
    def mostrar_velocimetro(self):
        print('La velocidad inicial es de'+ str(self.velocidad_inicial) + 'de un máximo de ' + str(self.velocidad_maxima) 
        + 'y la carga es'+ str(self.carga_actual))

    
class Automovil(Vehiculo):
    def __init__(self, puertas, color, marca, velocidad_maxima):
        self.puertas = puertas
        Vehiculo.__init__(self, color, marca, velocidad_maxima)

    def abrir_puertas(self, nro_puertas):
        print('Se abren las puertas')
    
   
mi_auto = Automovil(4, 'gris', 'toyota', 180)
print(mi_auto.get_properties())
#print(mi_auto.color)

#mi_auto.encender_auto()
#mi_auto.acelerar(200)
#mi_auto.acelerar(170)
#mi_auto.frenar(5500)
#mi_auto.apagar_auto()

#mi_camion = Camion('azul', 'Scania', 120, 2000)

#mi_camion.encender_auto()
#mi_camion.acelerar(20)

#mi_camion.carga_actual = 500
#print(mi_camion.carga_actual)
#mi_camion.acelerar(100)