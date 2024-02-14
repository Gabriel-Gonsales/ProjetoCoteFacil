class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = No(raiz)

    def inserir(self, valor):
        self._inserir(self.raiz, valor)

    def _inserir(self, no_atual, valor):
        # Verifica se o valor deve ser inserido à esquerda ou à direita
        if valor < no_atual.valor:
            # Insere à esquerda se o nó atual não tiver um filho à esquerda
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                # Caso contrário, chama recursivamente para o filho à esquerda
                self._inserir(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            # Insere à direita se o nó atual não tiver um filho à direita
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                # Caso contrário, chama recursivamente para o filho à direita
                self._inserir(no_atual.direita, valor)
        else:
            # Ignora valores duplicados (opcional)
            pass

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no_atual, valor):
        # Retorna o nó atual se for nulo ou se o valor for encontrado
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        # Chama recursivamente para o filho à esquerda se o valor for menor
        if valor < no_atual.valor:
            return self._buscar(no_atual.esquerda, valor)
        # Chama recursivamente para o filho à direita se o valor for maior
        return self._buscar(no_atual.direita, valor)
