import unittest
import cambioTexto

class TestCambioTexto(unittest.TestCase):

    def test_todo_mayuscula(self):
        self.assertEqual(cambioTexto.todo_mayuscula("hola"), "HOLA")
        self.assertEqual(cambioTexto.todo_mayuscula("mundo"), "MUNDO")
        self.assertEqual(cambioTexto.todo_mayuscula("python"), "PYTHON")
        
# Ejecutar las pruebas
# siempre el main para ejecutar las pruebas, no olvidar esto       
if __name__ == '__main__':
    unittest.main() 
    
    