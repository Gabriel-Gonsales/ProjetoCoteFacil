import unittest
import Arvore

class TesteArvoreBinaria(unittest.TestCase):
    def setUp(self):
        self.arvore = Arvore.ArvoreBinaria(5)
        self.arvore.inserir(3)
        self.arvore.inserir(7)
        self.arvore.inserir(2)
        self.arvore.inserir(4)
        self.arvore.inserir(6)
        self.arvore.inserir(8)

    def test_buscar_valor_existente(self):
        self.assertIsNotNone(self.arvore.buscar(4))

    def test_buscar_valor_inexistente(self):
        self.assertIsNone(self.arvore.buscar(9))

    def test_inserir_valor_duplicado(self):
        self.arvore.inserir(3)
        self.assertIsNotNone(self.arvore.buscar(3))

if __name__ == '__main__':
    unittest.main()
