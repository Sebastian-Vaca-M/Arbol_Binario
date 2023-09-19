'''
Title: Representacion de una estructura ADT Nodo
Autor: Sebastian Vaca Mejia
Date: 17/09/2023
Version: v1 .0
'''
#Clase Nodo que representa una estructura ADT
class Nodo:
    ''' 
    Método que crea instancias de la clase Nodo 
    '''
    def __init__(self,valor):
        self.__dato = valor
        self.__hijoIzquierdo = None
        self.__hijoDerecho = None

#Métodos getter y setter de la clase Nodo
    def getDato(self):
        return self.__dato
    def setDato(self, dato):
        self.__dato = dato
    '''
    Método que retorna el Nodo Izquierdo
    '''
    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo
    def setHijoIzquierdo(self, nodo):
        self.__hijoIzquierdo = nodo
    '''
    Método que retorna el Nodo Derecho
    '''
    def getHijoDerecho(self):
        return self.__hijoDerecho
    def setHijoDerecho(self, nodo):
        self.__hijoDerecho = nodo
    