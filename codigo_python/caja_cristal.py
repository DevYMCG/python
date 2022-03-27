from operator import truediv
import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor(self):
        edad = 30

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    
    def test_es_menor(self):
        edad = 13

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()
