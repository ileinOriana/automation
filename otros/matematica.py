class matematica():
    def sumar(self, nro1, nro2):
        try:
            if nro1 < 0:
                raise Exception("Los numeros tienen que ser positivos")
        except:
            return "señor, no puede poner un numero menor a cero"
        else:
            return nro1 + nro2
    
    def restar(self, nro1, nro2):
        return nro1 - nro2
    
    def multiplicar(self, nro1, nro2):
        try:
            if not type(nro1) is int:
                raise TypeError("Solo integers")
        except TypeError:
            return("No puedo multiplicar")
        else:
            return nro1 * nro2
    
    def dividir(self, nro1, nro2):
        try:
            return nro1 / nro2
        except ZeroDivisionError:
            return "No puedes dividir entre cero"
        except TypeError:
            return "Debes ingresar numeros"
        
class mapas():
    def get_item(self, mapa, item):
        return mapa[item]

mi_calculadora = matematica()

print(mi_calculadora.dividir(7, 2.5)

mi_mapa = mapas()
print(mi_mapa.get_item({'id': 0, 'nombre': 'Pablo'}, 'id'))