import unittest
from division import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
            self.assertEqual(dividir(6, 2), 3)
            self.assertEqual(dividir(-4, 2), -2)
            
            # manejo de error división por cero
            with self.assertRaises(ZeroDivisionError):
                dividir(5, 0)
                
if __name__ == "__main__":
    unittest.main()