from cProfile import run
import random
import os
import time
floors = 5+1      #ANDAR
max_capacity = 600  #KG
run_list = False         #se Lista de pessoas tá vasia
class elevator:

    def __init__(self,floor,capacity,people):
        self.floor = floor
        self.capacity = capacity
        self.people = people
        self.info_all = {}
        self.list_buttons = []
    
    def main(self):
        run = int(input("0- encerrar, 1 prosseguir:"))
        if run == 0:
            return "END"
        while True:
            time.sleep(1)
            self.cls()
            self.destiny() #aqui serve para puchar informações e realizar interação caso não haja ninguém no elevador
            print(len(self.list_buttons))
            if len(self.list_buttons) <1:
                run_list = False
            elif len(self.list_buttons)>=1: #aqui serve para puchar informações quando se á um lista de informações para seguir independente de pessoas dentro do elevador
                run_list = True
                self.list_point()
                '''for new_point in self.list_buttons:
                    self.floor = new_point        
                    self.local_elevator()
                    self.Q_remove_people()
                    self.Q_people()
                    self.destiny()
                    x =int(input("Algum andar foi solicitado externamente?(1 - Sim - 0 - Não)\nSelecione:"))    
                    if x  == 1:
                        run_list = False
                        self.destiny()
                    self.
                else:
                    pass'''

    def list_point(self):
        local = self.floor #local atual
        self.floor = self.list_buttons[0] #novo local de destino
        self.list_buttons.pop(0) #desempilhando informação
        info_local = int(input("Alguém No elevador solicitou Painvel novamente? (1 - Sim || 0 - Não)\nSelecione:"))
        if info_local == 0:
            pass
        else:    
            self.painel_control()
        info_local = int(input("Alguém Fora do elevador solicitou Painvel externo? (1 - Sim || 0 - Não)\nSelecione:"))
        if info_local == 0:
            pass
        else:
            nONe,info_local = self.external_button()
            self.list_buttons.append(int(info_local))
            run_list = False
        open_door_security = self.local_elevator(local)
        print(self.current_floor())    
        capacity,info = self.Q_people()
        if capacity == True:
            print(info)
        else:
            info = self.Q_remove_people()
        while len(self.info_all)>0:
            self.Q_remove_people()
            info_while = int(input("Alguém mais irá sair? (1 sim - 0 Nao)\nSelecione:"))
            if info_while == 0:
                break

            
            
        print(self.list_buttons)
        if len(self.list_buttons)>=1:
            self.list_point()
        run_list = False

               
            

    def current_floor(self):
        info =''
        if self.floor != 0:
            info = str(self.floor)+'º Andar'
        else:
            info = 'Térreo'
        return info
        

    def break_elevator(self):
        print("Houve problema de lotamento, Elevador não irá se mecher até que esteja no peso ideal.",self.info_all)
        aviso_despache = int(input("Nº da Pessoa que sairá:"))
        try:
            self.info_all.pop(aviso_despache)

            
            self.capacity = 0
            
            for x in self.info_all.values():
                self.capacity += x
            if self.capacity > max_capacity:
                print('\033[31m'+'Pessoas KG:'+str(self.capacity)+'...STOP!'+'\033[0;0m')
                self.break_elevator()
            else:
                return '\033[32m'+'Pessoas KG:'+str(self.capacity)+'\033[0;0m'
        except:
            self.break_elevator()
    def painel_control(self):
        for x in range(0,floors,1):
            if x %2 == 0:
                print('\n')
            if x == 0:
                print(x,'Terreo','\t',end='')
            elif x !=0:
                print(x,'\t\t',end='')

        
        buttons = input('\n\n'+str(floors)+"(Assistencia).\n\nListe a ordem dos botões clicados: ")
        buttons = buttons.replace(' ','.').replace(',','.').replace('_','.').replace('/','.')
        buttons = buttons.split('.')
        buttons = [int(x) for x in buttons]
        for x in range(0,len(buttons),1):
            if buttons[x] >= int(0) and buttons[x] <= int(6):
                if buttons[x] not in self.list_buttons:
                    self.list_buttons.append(buttons[x])
                #self.list_buttons.pop(x)
        print(self.list_buttons)
        
    def destiny(self):
        open_door_security = False
        if run_list == False:
            run,local = self.external_button()
            if run == 1:
                open_door_security = self.local_elevator(local)
                print(self.current_floor())    
                capacity,info = self.Q_people()
                if capacity == True:
                    print(info)
                else:
                    info = self.Q_remove_people()
                self.painel_control()

        #else:
        #    print(self.Q_people())
        #    print(self.Q_remove_people())

    def Q_people(self):
        info = int(input("Quantas pessoas entraram?\n"))
        if info ==0:
            return True,'\033[32m'+'Pessoas KG:'+str(self.capacity)+'\033[0;0m'
        self.people += info
        [self.info_all.update({x : random.randint(5,150)}) for x in range(1,self.people+1,1)]
        self.capacity = 0
        for x in self.info_all.values():
            self.capacity += x
        if self.capacity <= max_capacity:
            return True,'\033[32m'+'Pessoas KG:'+str(self.capacity)+'\033[0;0m'
        else:
            return False,'\033[31m'+'Pessoas KG:'+str(self.capacity)+'...STOP!'+'\033[0;0m'
            
    def Q_remove_people(self):
        if len(self.info_all) <1:
            return None
        if self.capacity >600:
            print('\033[31m'+'Pessoas KG:'+str(self.capacity)+'...STOP!'+'\033[0;0m')
        print(str(self.info_all).replace("{",'').replace("}",'').replace(":",": KG"))
        aviso_despache = int(input("Nº da Pessoa que sairá:"))
        try:
            self.info_all.pop(aviso_despache)
            self.capacity = 0
            for x in self.info_all.values():
                self.capacity += x
            if self.capacity <=600:
                print('\033[32m'+'Pessoas KG:'+str(self.capacity)+'\033[0;0m')
                return None
        except:
            pass
        x = int(input("Alguém mais vai sair? 1- Sim 0 - Não\nEscolha:"))
        if x !=0:
            if len(self.info_all)>0:
                self.Q_remove_people()
        else:
            pass
        
    
    def external_button(self):
        print("Qual Andar se encontra?(0-"+str(floors-1)+')')
        u_local = int(input())
        if u_local <0 or u_local >5:
            self.cls()
            self.external_button()
        x = int(input("(1 Para abrir || 0 - não abrir.\nescolha:"))
        if len(self.list_buttons)>=1 and x != 0:
            return u_local
        if x == 0:
            return 0,u_local
        else:
            return 1,u_local
    
    def local_elevator(self,local):
        for x in range(0,6,1):
            if int(x) == int(self.floor):
                print('\033[32m'+str(x)+'\033[0;0m',end=' ') 
            else:
                print(x,end=' ')
            if x %5 == 0 and x != 0:
                print('\n')
            #elif self.floor == x:
            #    print('\033[32m '+str(x)+' \033[0;0m',end='')
            #time.sleep(0.2)

        if local > self.floor:
            self.floor+=1
            self.local_elevator(local)
        elif local < self.floor:
            self.floor-=1 
            self.local_elevator(local)
        elif local == self.floor:
            return True
            
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
  
if __name__ == '__main__':
    print(elevator(0,0,0).main())