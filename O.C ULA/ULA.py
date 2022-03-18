from os import system,name



class astr:
    def __init__(self):
        pass

    def __str__(self,value):
        print(value)

    def limpar_tela(self):    
        system('cls' if name == 'nt' else 'clear')

    def list_type(self,value):
        x=''
        dicionario={}
        for i in range(0,8,1):
            x= str(format(i, "b"))
            
            for j in range(0,3,1):
                if int(len(x)) <3:
                    x = '0'+x
            dicionario[i]=x
        lista=[]
        for key,values in dicionario.items():
            if str(value) == str(key):
                for i in range(0,len(str(values)),1):
                    lista.append(int(values[i]))
        return lista
    def select_type(self):
        x =''


        search_with = 0
        cont_len=0
        return_list=[]

        while search_with != -1: #laço de repetição externo para 3 opções

            self.limpar_tela()
            self.__str__("<Deseja pegar o valor no <Em>\n[1]-Seu Valor Bin(0's & 1's).\n[2]-Por Numero Inteiro.\nSelecione(0-Voltar Para calculadora):\n")
            search_with = int(input())
            if search_with == int(1): # opção de digitar os valores em binario

                while search_with == 1: #laço de repetição interna para 3 opções
                    self.limpar_tela()
                    if cont_len != 0:
                        cont_len = 0
                        print("error: Por favor apenas 0 ou 1. ",end='')
                    self.__str__("Digite o valor[3 - posições]:\n")
                    acess_bin = input() #transforma variavel reciclada no valor que busca
                    if len(acess_bin) == 3:

                        for i in range (0,len(acess_bin),1):
                            if int(acess_bin[i]) == 0 or int(acess_bin[i]) == 1:
                                return_list.append(int(acess_bin[i]))
                                cont_len=cont_len+1
                                if cont_len == 3:
                                    return return_list
                            else:
                                pass
                        
                        return_list=[]
 
                    input()
                    acess_bin =''
    

            if search_with == int(2):

                while cont_len == 0:

                    self.limpar_tela()
                    self.__str__("Digite um valor inteiro[entre 0 a 7 ]:\n")
                    acess_int = int(input())

                    if acess_int >=0 and acess_int <=7:
                        if acess_int >=0:
                            return_list = self.list_type(acess_int)
                        return return_list




            if search_with == int(0):#voltar inicio da calculadora!
                return 0


class LO(astr):

    def __init__(self,value):
        astr.__init__(self)
        self.value = value
        self.stringv = ''


    def OR(self,A_val,B_val):
        A_val = A_val | B_val
        return int(A_val)

    def NOT(self,A_val):
        A_val = int(not A_val)
        return int(A_val)


    def AND(self,A_val,B_val):
        A_val = A_val & B_val
        return int(A_val)

    def XOR(self,A_val,B_val):
        A_val = A_val ^ B_val
        return int(A_val)

#0|0|0   |1
#0|1|1-1 |0
#1|1|0   |
class ULA(LO):
    def __init__(self,value =0):
        LO.__init__(self,value)
        self. value = value

    '''SOM irei Utilizar AND,OR,XOR,NOT Nessa exata sequencia, onde um valor Y virá para interpretar uma condição
    Condição Y > A & B = 1. Pois quando fizer isso significa que nessa casa deverá ser interagida no proximo laço.
    Laço decrementado para ficar simples de ser lido da Direita para esquerda.
    quando Y voltar 1, Estaremos tratando a proxima linha de posição ( i !=0 como condição de parada, evitar overflow).'''
    def som(self,lista,listb):
        Y=int(0)
        for i in range(2,0,-1):
            
            Y= int(self.AND(lista[i],listb[i]))
            if Y == 1:
                lista[i] = self.XOR(lista[i],Y)
                if i > -1:
                    lista[i-1] =self.NOT(lista[i-1])
            else:
                lista[i] = self.OR(lista[i],listb[i])

        print(lista)
        return lista

    def sub(self,lista,listb):
        Y=int(0)
        for i in range(2,0,-1):
            #listb[i] = self.NOT(lista[i])
            Y= int(self.XOR(lista[i],listb[i]))
            if Y == 1:
                lista[i] = self.XOR(lista[i],listb[i])
                if i != 0:
                    listb[i-1] = self.OR (lista[i-1],listb[i-1])
            else:
                lista[i] = self.NOT(lista[i])
        print(lista)
        return lista

    '''Projetando'''
    def div(self,lista,listb):

        pass
        return lista


    def mult(self,lista,listb):
        copylist=[]
        
        endlist=self.list_type(0)
        Y=int(0)

        endlist= self.list_type(0)
        for i in range(0,3,1):
            copylist= lista
            Y=int(0)
            for j in range(2,0,-1):
                copylist[j] = int(self.XOR(lista[j],listb[j]))

            
            for k in range(i,0,-1):
                Y= int(self.AND(copylist[k],copylist[k]))
                #print(endlist,'AND')
                if Y == 1:
                    endlist[k] = self.XOR(copylist[k],Y)
                    #print(endlist,'XOR')
                    if k != 0:
                        endlist[k-1] =self.NOT(copylist[i-1])
                        #print(endlist,'NOT')
                    else:
                        endlist[k] = self.OR(copylist[k],copylist[k])
                        #print(endlist,'OR')

                input(endlist)
        return lista


        print(endlist,'depois')
        return lista






class Calc(ULA,LO,astr): #Classe simples que não necessita de variaveis condicionais para acessala porém usam três variaveis locais
    def __init__(self,value=0):
        ULA.__init__(self,value)
        LO.__init__(self,value)
        astr.__init__(self)
        self.__info =''
        self.value  =value
        self.bin1 = []
        self.bin2 = []

    @property
    def menu(self): 

        if self.__info == 1:
            print("alou")
            
            self.__info = self.listLO 

            return self.__info
        elif self.__info == 2:
            
            self.__info = self.listOPA
        
        return self.__info
        
        
    @menu.setter
    def menu(self,value):
        value = int
        while value != -1:
            self.limpar_tela()
            self.__str__("Selecione -1- Para Operações Lógicas\nSelecione -2- Para Operações Aritimeticas.\n(0-Parar)Digite:")
            value = int(input())
            if value == int(1):
                self.listLO=0
                value = -1
            elif value == int(2):
                self.listOPA=0
                value = -1
            elif value == int(0):
                self.__str__("Stop!")
                exit()
        self.__info = value

    @property
    def listLO(self):
        
        return self.stringv

    @listLO.setter
    def listLO(self,select):
        
        select = int
        while select != -1:
            self.limpar_tela()
            self.__str__("(ULA-O.C-IF:2021.2.)\nSelecione -1- -OU/OR\nSelecione -2- -NÃO/NOT\nSelecione -3- -E/AND\nSelecione -4- -(OU-EXCLUSICO)/XOR\n(0-Interromper/Fechar)Digite:")
            select = int(input())
            
            if select == int(1):
                self.__str__("opc1")
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.__info = self.OR(self.bin1,self.bin2)
                print(self.__info)
                select = -1
            elif select == int(2):
                self.__str__("opc2")
                self.bin1 = self.select_type()
                self.__info = self.NOT(self.bin1)
                print(self.__info)
                select = -1
            elif select == int(3):
                self.__str__("opc2")
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.__info = self.AND(self.bin1,self.bin2)
                print(self.__info)

                select = -1
            elif select == int(4):
                self.__str__("opc2")
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.__info = self.XOR(self.bin1,self.bin2)
                print(self.__info)
                select = -1
            else:
                self.__str__("Stop!")
                return 0

        return self.stringv

    '''Def listOPA responsável por selecionar logica aritimetica Adição/Subtração/Divisão/Multiplicação'''
    @property
    def listOPA(self):
        print(self.bin1)
        input()
        return self.value

    @listOPA.setter
    def listOPA(self,select):
        
        select = int
        while select != -1:
            self.limpar_tela()
            self.__str__("Selecione -1- -ADIÇÃO/ADDITION\nSelecione -2- -SUBTRACAO/SUBTRACTION\nSelecione -3- -DIVISÃO/DIVISION\nSelecione -4- -MULTIPLICAÇÃO/MULTIPLICATION\n(0-Interromper/Fechar)Digite:")
            select = int(input())
            
            if select == int(1):
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.bin1 = self.som(self.bin1,self.bin2)
                input()
                break
            elif select == int(2):
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.bin1 = self.sub(self.bin1,self.bin2)
                input()
                break
            elif select == int(3):
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.bin1 = self.div(self.bin1,self.bin2)
                input()
                break
            elif select == int(4):
                self.bin1 = self.select_type()
                self.bin2 = self.select_type()
                self.bin1 = self.mult(self.bin1,self.bin2)
                input()
                break
            elif select == int(0):
                self.__str__("Stop!")
                return 0
        self.value = 1



if __name__ == '__main__':
    print("Run Codding")
    calcule = Calc()
    calcule.menu = 0
    #x= astr().select_type()
    #print(x) 

    '''#y=input("digite valor dois:")
    #print(bin(4))
    #calcule.menu=0
    #print(calcule.menu)

    print(2<<1)'''

    '''i=(0^0);print(0^0)
    i=(i^1);print(i^1)
    i=(i^0);print(i^0)'''

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