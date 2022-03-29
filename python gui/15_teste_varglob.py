from distutils.log import info
from tkinter import *

def definfo():
    variavel_local.set("Olá " + box_info.get())

if (__name__) == '__main__':
    '''------gui-----'''
    main = Tk()
    main.iconbitmap('icon/IF.ico')
    main.title("variavel global")
    '''---variavel local--- sempre alterável, pode ser manipulada usando um .set()\n sem sua composição tendo então uma mudança sempre no seu valor'''
    variavel_local= StringVar() #Função nova  usando StringVar (variavel de string!)
    main.geometry('350x200+850+300')
    main.resizable(False,False)
    main['bg']='#000512'
    Label(main,bg='#000512',width=15,height=2).grid(row=0,column=0)
    label_info=Label(main,text='Digite um valor',font='Arial 10',bd=3,relief='groove',bg='white',width=15,height=1,anchor=CENTER).grid(row=1,column=1)
    '''Informaçõe necessárias\nbox infor cujo é responsável por alocar os valores dentro, fica responsável por passar informações'''
    box_info=Entry(main,bd=2,relief='raised')
    Label(main,bg='#000512',width=15,height=2).grid(row=2,column=0)

    button_info= Button(main,text='Run!',command=definfo).grid(row=3,column=1)

    Label(main,font='Arial 10',textvariable=variavel_local,bg='#000512',fg='white').grid(row=4,column=1)
    box_info.grid(row=2,column=1)

    main.mainloop()