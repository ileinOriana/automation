import unittest

#Las clases se escriben en camelCase

class PruebasDeStandards(unittest.TestCase):
#Aca decimos que esta clase extiende del Padre unittest.TestCase

    def test_suma(self): 
        a = 2 + 2 
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 5 + 1
        b = 8 + 20
        self.assertNotEqual(a,b)

    def test_algo_es_verdadero(self):
        a = 2 + 2 
        b = 3 + 1 
        self.assertTrue(a == b, "a y b deberian ser iguales")

    def test_algo_es_mayor(self):
        a = 5
        b = 3 
        self.assertTrue(a>b, "a deberia ser mayor a b")

    
    def test_algo_es_mayor_II(self):
        a = 5 
        b = 1
        self.assertGreater(a, b)

    def test_algo_es_mayor_igual(self):
        a = 5.0
        b = 5
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 5
        b = 8 
        self.assertLess(a,b, "a debe ser menor que b")

    def test_algo_es_menor_igual(self):
        a = 20
        b = 21
        self.assertLessEqual(a, b)
    
    #Para comparar listas
    def test_comparar_listas(self):
        a = [1, 2, "fruta"]
        b = [1, 2, "fruta"]
        self.assertListEqual(a, b, "las listas no son iguales")
    
    def test_comparar_tuplas(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b, "las tuplas no son iguales")
    
    def test_comparar_diccionarios(self):
        a = {"id": 1, 'nombre': 'pepe', 'edad': 30 }
        b = {"id": 1, 'nombre': 'pepe', 'edad': 30 }
        self.assertDictEqual(a, b, "los diccionarios no son iguales")

if __name__ == "__main__":
    unittest.main()