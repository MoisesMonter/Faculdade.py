from distutils.log import info
from tkinter import *

class Click:
    def cmd_click():
        print("Olá Mundo!")
    
    def cmd_import_info(info1,info2):
        print(info1,'\n',info2)

if (__name__) == "__main__":

    menu = Tk()
    menu.geometry("750x500+600+200")
    menu.minsize(width=500,height=400)
    menu.maxsize(width=750,height=500)
    menu.resizable(False,True)
    menu.iconbitmap("icon/IF.ico")
    menu.title("Funcao Button")
    menu['bg']='gray' #<< letras minusculas
    ck=Click

    '''botão comum seu command serve para acessar uma função'''
    cmd = Button(menu,text='Run!',command=ck.cmd_click)
    cmd.pack()
    info1= [1,0,1]
    info2= [0,1,0]
    '''botão que leva informação, usa lambda dentrodo comand para jogar uma informação dentro da função'''
    cmd_info = Button(menu,text='info', command= lambda:ck.cmd_import_info(info1,info2))
    cmd_info.pack()
    cmd_info['bg']='gray'
    label1= Label(menu,text="MENU",font='Verdana 20 bold',bg='red')
    label1.pack()
    label2= Label(menu,text="Texto grande",font='Verdana 40 bold',fg="#aaaaaa",bg='blue',width=40,height=20)
    label2.pack()


    menu.mainloop()