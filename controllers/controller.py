from models.LinkedList import LinkedList
l = LinkedList()

def impressao ():
    return l.traverse_list()

def rpi (lista: list, registo: str)-> list:
    l.insert_at_start(registo)
    return lista

def rpf (lista: list, registo: str)-> list:
    l.insert_at_end(registo)
    return lista


def rpde (lista: list, paisn: str, paisr: str) -> list:
    l.insert_after_item(paisr, paisn)
    return lista

def rpae (lista, paisn, paisr)-> list:
    l.insert_before_item(paisr, paisn)
    return lista

def rpii(lista, indice, paisn)-> list:
    l.insert_at_index(indice, paisn)
    return lista

def vne ():
    return l.get_count()

def vp (pais):
    if l.search_item (pais) == True:
        return True
    else:
        return False

def epe () -> str:
    l.reverse_linkedlist()
    pais = l.get_last_node()
    l.reverse_linkedlist()
    l.delete_at_start() 
    return pais

def eue () -> list:
    pais = l.get_last_node()
    l.delete_at_end()
    return pais

def pep(pais):
    if l.search_itemsp(pais) == False:
        return False
    else:
        return True

def ep(pais):
    l.delete_element_by_value(pais)
    return pais