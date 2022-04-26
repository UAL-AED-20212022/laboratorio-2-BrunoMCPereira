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
    elif l.search_item (pais) == False: 
        return False

def epe (lista: list) -> list:
    l.delete_at_start() 
    return lista

def eue (lista: list) -> list:
    l.delete_at_end()
    return lista

def ep(lista, pais):
    if l.search_item(pais) == False:
        return False
    elif l.search_item(pais) == True:
        return True