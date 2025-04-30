import unittest
from db import afegir_grup, consultar_grup

class TestGestorGrupsMusicals(unittest.TestCase):
    
    def test_afegir_grup(self):
        """Test per afegir un grup a la base de dades."""
        afegir_grup("The Beatles", 1960, "Rock", 4)
        grup = consultar_grup("The Beatles")
        self.assertIsNotNone(grup)
        self.assertEqual(grup[1], "The Beatles")

    def test_consultar_grup_no_existent(self):
        """Test per consultar un grup que no existeix."""
        grup = consultar_grup("Grup Inexistent")
        self.assertIsNone(grup)

if __name__ == "__main__":
    unittest.main()
