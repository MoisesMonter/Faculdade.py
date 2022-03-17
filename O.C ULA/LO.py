from ULA import *


class LO:
    def __init__(self):
        Calculated.__init__(self)
        self.bin1 = []
        self.bin2 = []
    
    @property
    def listLO(self):
        self.limpar_tela()
        self.__str__("Selecione -1- Para Operações Lógicas\nSelecione -2- Para Operações Aritimeticas.\n(0-Interromper)Digite:")

    @listLO.setter
    def listLO(self):
        bin1 = list
        bin2 = list