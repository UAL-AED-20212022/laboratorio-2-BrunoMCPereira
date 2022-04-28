from models.Node import Node
# importa do Node a classe que define a estrutura de dados

# item de dados - self.item = data - passado através do construtor
# item de referência - self.ref - referência inicia no null

class LinkedList: # Classe que vai conter os metodos que operam sobre a lista
    def __init__(self):
        self.start_node = None # Definimos o start_node (membro que aponta para o primeiro nó)
        # Neste caso o nó inicial é definido com "None" uma vez que a lista está vazia
    
    def traverse_list(self): # Metodo que se destina a correr a lista e assim ler os dados contidos nela:
        if self.start_node is None:
            print("List has no element") # Se o membro que aponta para o primeiro nó se mantiver vazia, devolve essa mensagem
            return
        else:
            n =  self.start_node # Definimos n como nó:
            while n is not None: # Corremos todos os nós da lista
                print(n.item, " ") 
                n = n.ref

    def insert_at_end(self, data):
        new_node = Node(data) # novo nó é = self.item - item = Instrução passada pelo construtor

        if self.start_node is None: #Se a lista estiver vazia
            self.start_node = new_node # define o novo nó como o nó de inicio - o primeiro nó
            return
        n = self.start_node # Definimos n como nó:
        while n.ref is not None: # Corremos todos os nós da lista - assim que o nó seguinte não existir:
            n = n.ref # o novo nó será a referência devolvida none
        n.ref = new_node # e "preenche" essa referência com os novos dados
    
    def insert_at_start(self, data):
        new_node = Node(data) # novo nó é = self.item - item = Instrução passada pelo construtor
        new_node.ref = self.start_node # a referência do novo nó é determinada como o nó de inicio
        self.start_node = new_node # "insere" os dados no nó definido - nó de inicio

    
    def insert_after_item(self, x, data):
        n = self.start_node # Definimos n como nó:
        print(n.ref)
        while n is not None: # corremos todos os nós até o nó não conter informação
            if n.item == x: # se a informação dos dados do nó iterado for igual à item (valor inserido pelo construtor) 
                break # Quebramos o ciclo de iterações
            n = n.ref # e determinamos a referência do nó 
        if n is None: # se após as iterações n for none (ou seja n.ref arquivou none)
            print("item not in the list")
        else: # Caso n contenha a informação inserida pelo construtor
            new_node = Node(data) # novo nó é = self.item - item = Instrução passada pelo construtor
            new_node.ref = n.ref # a referência do nó criado é a mesma que o nó que continha a informação
            n.ref = new_node 

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item is not None:
                if n.ref.item == x:
                    break 
                n = n.ref

        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False


    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref
    
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no elemnet to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")

        else:
            n.ref = n.ref.ref
            
    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not  None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next

        self.start_node = prev
    
    def get_last_node(self): 
        #retorna o último elemento da lista
        n = 1
        temp = self.start_node
        length = 0
        while temp is not None:
            temp = temp.ref
            length += 1

        if n > length: 
            return
        temp = self.start_node
        for i in range(0, length - n):
            temp = temp.ref
        return temp.item

    def search_itemsp(self, x):
        if self.start_node is None:
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                return True
            n = n.ref
        return False