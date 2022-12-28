from platform import system as S_op
from os import system as Varrer

def Limpar(plataforma):
    if len(plataforma) >0:
        Varrer(plataforma)
    if plataforma == "Windows":
        Varrer('cls')
    else:
        Varrer('clear')
    return plataforma

def Incrementar(deque,bool):
    if bool == True:
        front = int(input("Digite valor de entrada:"))
        deque.insert(0,front)
    else:
        rear = int(input("Digite valor de entrada:"))
        if len(deque) <=0:
            deque.append(rear)
        else:
            deque.extend([rear])
            
    return deque

def Decrementar(deque,bool):
    if bool == True:
        if len(deque) <=0:
            print("lsita vazia")
        else:
            deque.pop(0)
    else:
        deque.pop()
    return deque


if __name__ == "__main__":
    deque = []
    plataforma = Limpar("")
    while True:
        Limpar(plataforma)
        print(deque)
        x = int(input("0 - Sair\n1 - Incrementar Inicio\n2- Incrementar Final\n3 Deletar Inicio\n4Deletar Final\n\nSelecione:"))
        if x == 0:
            break
        elif x ==1:
            deque = Incrementar(deque,True)
        elif x ==2:
            deque = Incrementar(deque,False)
        elif x == 3:
            deque = Decrementar(deque,True)
        elif x == 4:
            deque = Decrementar(deque,False)