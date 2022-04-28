# Classe criada para os nós da Lista

# Um Nó de uma lista ligada simples tem de criar:
# item de dados - self.item = data - passado através do construtor
# item de referência - self.ref - referência inicia no null

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
    
    def get_item(self):
        return self.item
    
    def get_ref(self):
        return self.ref