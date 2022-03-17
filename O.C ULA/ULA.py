from os import system,name



class astr:
    def __init__(self):
        pass

    def __str__(self,value):
        print(value)

    def limpar_tela(self):    
        system('cls' if name == 'nt' else 'clear')

    def select_type(self,ty):
        x =''
        lista={}
        for i in range(0,8,1):
            x= str(format(i, "b"))
            
            for j in range(0,3,1):
                if int(len(x)) <3:
                    x = '0'+x
            lista[i]=x

        cont = int(0)
        negative=''
        neglista={}
        dictbin={}
        for val in lista.values():
            cont = cont-1
            x =str(val)
            negative=''
            for i in range(0,len(x),1):
                
                if x[i]== '0':
                    negative = negative+"1"
                else:
                    negative= negative+'0'
            print(cont,':',negative)
            neglista[cont]=negative

        dictbin = {**neglista,**lista}
        
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
                    self.__str__("Digite se o Binario vai ser positivo ou negativo([1] = + //[2] = - )  ")
                    acess_bin = input() #transforma variavel reciclada no valor que busca
                    if acess_bin == '2':
                        return_list.append('-')
                    else:
                        return_list.append('+')
                    self.limpar_tela()
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
                        if acess_int <0:
                            return_list.append('-')
                            for key,values in dictbin.items():
                                if str(acess_int) == str(key):
                                    for i in range(0,len(str(values)),1):
                                        return_list.append(int(values[i]))

                        if acess_int >=1:
                            return_list.append('+')
                            for key,values in dictbin.items():
                                if str(acess_int) == str(key):
                                    for i in range(0,len(str(values)),1):
                                        return_list.append(int(values[i]))

                        return return_list




            if search_with == int(0):#voltar inicio da calculadora!
                return 0


class LO(astr):
    def __init__(self,value):
        astr.__init__(self)
        self.value = value
        self.stringv = ''
        self.bin1 = []
        self.bin2 =[]


    def OU(self):
        #print(self.bin1[1:],' or ',self.bin2[1:],' =')
        self.stringv = str(self.bin1[1:])+' OR '+str(self.bin2[1:])+' = '
        if self.bin1[0] == '-' or self.bin2[0] == '-':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                print(type(x))
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==int(1):
                        self.stringv = self.stringv+"0"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==1:
                        self.stringv = self.stringv+"1"
        elif self.bin1[0] == '+' and self.bin2[0] == '+':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==int(1):
                        self.stringv = self.stringv+"1"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==int(1):
                        self.stringv = self.stringv+"1"
        #print(self.stringv)
        #input()
        return self.stringv

    def NOT(self):
        #print(self.bin1[1:],' or ',self.bin2[1:],' =')
        self.stringv = 'NOT: '+str(self.bin1[1:])+' = '
        self.bin1.pop(0)
        for x in self.bin1:
            if x == int(0):
                self.stringv = self.stringv+"1"
            elif x == int(1):
                self.stringv = self.stringv+"0"
        #print(self.stringv)
        #input()
        return self.stringv


    def AND(self):
        #print(self.bin1[1:],' or ',self.bin2[1:],' =')
        self.stringv = str(self.bin1[1:])+' AND '+str(self.bin2[1:])+' = '
        if self.bin1[0] == '-' or self.bin2[0] == '-':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==int(1):
                        self.stringv = self.stringv+"1"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==1:
                        self.stringv = self.stringv+"0"
        elif self.bin1[0] == '+' and self.bin2[0] == '+':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==int(1):
                        self.stringv = self.stringv+"0"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==int(1):
                        self.stringv = self.stringv+"1"
        #print(self.stringv)
        #input()
        return self.stringv

    def XOR(self):
        #print(self.bin1[1:],' or ',self.bin2[1:],' =')
        self.stringv = str(self.bin1[1:])+' XOR '+str(self.bin2[1:])+' = '
        if self.bin1[0] == '-' or self.bin2[0] == '-':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                print(type(x))
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==int(1):
                        self.stringv = self.stringv+"0"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==1:
                        self.stringv = self.stringv+"0"
        elif self.bin1[0] == '+' and self.bin2[0] == '+':
            self.bin1.pop(0);self.bin2.pop(0)
            for x,y in zip(self.bin1,self.bin2):
                if x == int(0):
                    if y == int(0):
                        self.stringv = self.stringv+"0"
                    elif y ==int(1):
                        self.stringv = self.stringv+"1"
                elif x == int(1):
                    if y == int(0):
                        self.stringv = self.stringv+"1"
                    elif y ==int(1):
                        self.stringv = self.stringv+"0"
        #print(self.stringv)
        #input()
        return self.stringv


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
                self.bin1 = self.select_type('1º ->OU/OR')
                self.bin2 = self.select_type('2º ->OU/OR')
                self.OU()
                select = -1
            elif select == int(2):
                self.__str__("opc2")
                self.bin1 = self.select_type('1º ->NÃO/NOT')
                self.select_type('NOT')
                self.NOT()
                select = -1
            elif select == int(3):
                self.__str__("opc2")
                self.bin1 = self.select_type('1º ->E/AND')
                self.bin2 = self.select_type('2º ->E/AND')
                self.select_type('AND')
                self.AND()
                select = -1
            elif select == int(4):
                self.__str__("opc2")
                self.bin1 = self.select_type('1º ->(Ou-ECLUSIVO)/XOR')
                self.bin2 = self.select_type('2º ->(Ou-ECLUSIVO)/XOR')
                self.select_type('XOR')
                self.XOR()
                select = -1
            else:
                self.__str__("Stop!")
                return 0

        return self.stringv





#construindo...
class OPA(astr):
    def __init__(self,value):
        astr.__init__(self)
        self.value= value 
        self.bin1 = int
        self.bin2 = []




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
                self.__str__("opc1")
                self.select_type('ADIÇÃO/ADDITION')
            elif select == int(2):
                self.__str__("opc2")
                self.select_type('SUBTRACAO/SUBTRACTION')
                break
            elif select == int(3):
                self.__str__("opc3")
                self.select_type('DIVISÃO/DIVISION')
                break
            elif select == int(4):
                self.__str__("opc4")
                self.select_type('MULTIPLICAÇÃO/MULTIPLICATION')
            elif select == int(0):
                self.__str__("Stop!")
                return 0
        self.value = 1






class Calculated(OPA,LO,astr): #Classe simples que não necessita de variaveis condicionais para acessala porém usam três variaveis locais
    def __init__(self,info = 0):
        OPA.__init__(self,info)
        LO.__init__(self,info)
        astr.__init__(self)
        self.__info = info #valor final do resultado

    @property
    def menu(self):
        if self.__info == 1:
            self.listLO = 0
            self.__info = self.listLO

            return self.__info
        elif self.__info == 2:
            self.listOPA = 0
            self.__info = self.listOPA
        
        return self.__info
        
        
    @menu.setter
    def menu(self,value):
        value = int
        while value != -1:
            self.limpar_tela()
            self.__str__("Selecione -1- Para Operações Lógicas\nSelecione -2- Para Operações Aritimeticas.\n(0-Parar)Digite:")
            #value = int(input())
            value = 1
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