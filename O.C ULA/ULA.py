from os import system,name



class astr:
    def __init__(self):
        pass

    def __str__(self,value):
        print(value)

    def select_type(self,ty):
        
        acess_bin = str
        acess_int = int
        return_list = []
        cont_len=int(0)
        search_with = int

        while search_with != -1: #laço de repetição externo para 3 opções

            self.limpar_tela()
            self.__str__("<Deseja Digitar a busca do(a)->"+str(ty)+" <- Em>\n[1]-Por Numeros Bin(0's & 1's).\n[2]-Por Numero Inteiro.\nSelecione(0-Voltar Para calculadora):\n")
            search_with = int(input())

            if search_with == int(1): # opção de digitar os valores em binario
                
                while search_with == 1: #laço de repetição interna para 3 opções

                    self.limpar_tela()
                    self.__str__("Digite o valor[3 - posições]:\n")
                    acess_bin = input() #transforma variavel reciclada no valor que busca

                    if len(acess_bin) == 3:

                        for i in range (0,len(acess_bin),1):
                            if int(acess_bin[i]) == 0 or int(acess_bin[i]) == 1:
                                print(i ,':',type(i),'|')
                                return_list.append(int(acess_bin[i]))
                                cont_len=cont_len+1
                                if cont_len == 3:
                                    print(return_list)
                                    input()
                                    return return_list
                            else:
                                pass
                        cont_len=0
                        return_list=[]
                    print("erro")
                    input()
                    acess_bin =''
    

            if search_with == int(2):

                while cont_len == 0:

                    self.limpar_tela()
                    self.__str__("Digite um valor inteiro[entre 7 e -7 ]:\n")
                    acess_int = int(input())

                    if acess_int >=-7 and acess_int <=7:
                        cont_len=3 #define quantas casas serão lidas  <=== Alterar aqui. para mais casas
                        acess_bin = str(format(acess_int, "b")) #<----------------------------------- Responsável por transformar em binario
                        try:
                            acess_bin = acess_bin.replace('-','') #PUCHAR LEN DE ACESS_BIN 
                        except:
                            pass
                        print(acess_int,":",len(acess_bin))
                        for i in range(0,len(acess_bin),1):
                            return_list.append(int(acess_bin[i]))
                            
                        if acess_int <0:
                            for i in range (0,cont_len,1):
                                if len(return_list)<3:
                                    return_list.append(1) #incrementar valores 1 onde a posição é vasia para voltar lista
                            return_list.insert(0,'-') #definir melhor se é negativo ou positivo a info
                            print(len(return_list),'N',return_list)
                        if acess_int >=0 :
                            for i in range (0,3,1):
                                if len(return_list)<3:
                                    return_list.append(0)
                            return_list.insert(0,'+') #definir se é negativo ou positivo
                            print(len(return_list),'N',return_list)
                        input()
                        return return_list




            if search_with == int(0):#voltar inicio da calculadora!
                #self.back_calculator()
                pass
        
    
    def limpar_tela(self):    
        system('cls' if name == 'nt' else 'clear')

    def back_calculator():
        Calculated.menu = 0


class LO(astr):
    def __init__(self):
        astr.__init__(self)
        self.bin1 = int
        self.bin2 = []




    @property
    def listLO(self):
        return self.bin1

    @listLO.setter
    def listLO(self,select):
        
        select = int
        while select != -1:
            self.limpar_tela()
            self.__str__("Selecione -1- -OU/OR\nSelecione -2- -NOT\nSelecione -3- -AND\nSelecione -4- -XOR\n(0-voltar Calculadora)Digite:")
            select = int(input())
            
            if select == int(1):
                self.__str__("opc1")
                self.select_type('OU/OR')
            elif select == int(2):
                self.__str__("opc2")
                break
            elif select == int(3):
                self.__str__("opc2")
                break
            elif select == int(0):
                self.__str__("Stop!")
                self.back_calculator()
        self.__info = select


    def OU(self):
        print('ou')
        pass



class Calculated(LO,astr): #Classe simples que não necessita de variaveis condicionais para acessala porém usam três variaveis locais
    def __init__(self, info = 0):

        LO.__init__(self)
        astr.__init__(self)
        self.__info = info #valor final do resultado

    @property
    def menu(self):
        if self.__info == 1:
            self.listLO = 0
            self.__info = self.listLO
            return self.__info
        if self.__info == 2:
            return self.__info
        
        
    @menu.setter
    def menu(self,value):
        value = int
        while value != -1:
            
            self.__str__("Selecione -1- Para Operações Lógicas\nSelecione -2- Para Operações Aritimeticas.\n(0-Parar)Digite:")
            value = int(input())
            
            if value == int(1):
                self.__str__("opc1")
                break
            elif value == int(2):
                self.__str__("opc2")
                break
            elif value == int(0):
                self.__str__("Stop!")
                exit()
        self.__info = value






if __name__ == '__main__':
    print("Run Codding")
    calcule = Calculated()
    calcule.menu=0
    print(calcule.menu)

#for i in range(0,30,1):
#    print("{0:b}".format(i))
'''
000 = 0
001 = 1
010 = 2
011 = 3
100 = 4
101 = 5
110 = 6
111 = 7
#class 

print(bin(-5))#pegar binario
i = -5
print("0{0:b}".format(5))
print("{0:b}".format(-5))

print(2^3) #XOR

print(2&3) #AND

print(4|3) #OR 

print(~2) #NOT ( -2 -1)'''