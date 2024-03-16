from tkinter import *
from tkinter import ttk
import random as rd
import string as st

corTela = '#0d1b1f'
corFundo = '#5f686b'
corBotao = '#f5b400'
corTecla = '#ffffff'


janela = Tk()
janela.title('Gerador de senhas')
janela.geometry('500x380')


tela = Frame(janela, width=500, height=80, bg=corTela)
tela.grid(row=0, column=0)

opcao = Frame(janela, width=500, height=400, bg=corFundo)
opcao.grid(row=1, column=0)


tLabel = Label(tela, text='Escolha o tamanho da senha:', width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
tLabel.place(x=10,y=0)


def tam8():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=8))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=8))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=8))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=8))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=8))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam9():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=9))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=9))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=9))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=9))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=9))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam10():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=10))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=10))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=10))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=10))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=10))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam11():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=11))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=11))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=11))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=11))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=11))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam12():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=12))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=12))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=12))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=12))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=12))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam13():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=13))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=13))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=13))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=13))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=13))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam14():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=8))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=8))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=8))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=8))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=8))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam15():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=15))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=15))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=15))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=15))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=15))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)


def tam16():
    janela2 = Toplevel()
    janela2.title('gerador de senha, tamanho: 8')
    janela2.geometry('500x380')

    tela = Frame(janela2, width=500, height=80, bg=corTela)
    tela.grid(row=0, column=0)

    opcao = Frame(janela2, width=500, height=400, bg=corFundo)
    opcao.grid(row=1, column=0)

   


    letrasm = st.ascii_lowercase
    letrasM = st.ascii_uppercase
    numeros = st.digits
    caracteres = st.punctuation
    Mmn2 = letrasM + letrasm + numeros
    Mmc2 = letrasM + letrasm + caracteres
    Mnc2 = letrasM + caracteres + numeros
    mnc2 = letrasm + numeros + caracteres
    tot2 = letrasM + letrasm + caracteres + numeros
    valor = StringVar()

    def Mmn():
        senha = ''.join(rd.SystemRandom().choices(Mmn2, k=16))
        valor.set(senha)
        return senha
    def Mmc():
        senha = ''.join(rd.SystemRandom().choices(Mmc2, k=16))
        valor.set(senha)
        return senha
    def Mnc():
        senha = ''.join(rd.SystemRandom().choices(Mnc2, k=16))
        valor.set(senha)
        return senha
    def mnc():
        senha = ''.join(rd.SystemRandom().choices(mnc2, k=16))
        valor.set(senha)
        return senha
    def tot():
        senha = ''.join(rd.SystemRandom().choices(tot2, k=16))
        valor.set(senha)
        return senha
    

    tLabel = Label(tela, textvariable=valor, width=23, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 25 '), bg=corTela, fg=corTecla)
    tLabel.place(x=10,y=0)

    bMmn = Button(opcao,command=Mmn, text=f'Letras\nMaiúsculas,\nMinúsculas,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmn.grid(row=0,column=0)
    bMmn.place(x=5,y=8)
    bMmc = Button(opcao,command=Mmc, text=f'Letras\nMaiúsculas,\nMinúsculas,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMmc.grid(row=0,column=0)
    bMmc.place(x=175,y=8)
    bMnc = Button(opcao,command=Mnc, text=f'Letras\nMaiúsculas,\nNúmeros,\nCaracteres\nEspeciais', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bMnc.grid(row=0,column=0)
    bMnc.place(x=5,y=150)
    bmnc = Button(opcao,command=mnc, text=f'Letras\nMinúsculas,\nCaracteres\nEspeciais,\nNúmeros', width=11, height=5, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bmnc.grid(row=0,column=0)
    bmnc.place(x=175,y=150)
    bT = Button(opcao,command=tot, text='Todos', width=11, height=11, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
    bT.grid(row=0,column=0)
    bT.place(x=340,y=8)



#fileira um

bt1 = Button(opcao, command=tam8, text='8', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt1.grid(row=0, column=0)
bt1.place(x=5,y=10)
bt2 = Button(opcao,command=tam9, text='9', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt2.grid(row=0, column=0)
bt2.place(x=170,y=10)
bt3 = Button(opcao,command=tam10, text='10', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt3.grid(row=0, column=0)
bt3.place(x=335,y=10)

#fileira dois
bt4 = Button(opcao,command=tam11, text='11', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt4.grid(row=0, column=0)
bt4.place(x=5,y=110)
bt5 = Button(opcao, command=tam12, text='12', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt5.grid(row=0, column=0)
bt5.place(x=170,y=110)
bt6 = Button(opcao, command=tam13, text='13', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt6.grid(row=0, column=0)
bt6.place(x=335,y=110)

#fileira tres
bt7 = Button(opcao, command=tam14, text='14', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt7.grid(row=0, column=0)
bt7.place(x=5,y=210)
bt8 = Button(opcao, command=tam15, text='15', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt8.grid(row=0, column=0)
bt8.place(x=170,y=210)
bt9 = Button(opcao, command=tam16, text='16', width=10, height=2, font=('Ivy 18 bold'), relief=RAISED, overrelief=RIDGE)
bt9.grid(row=0, column=0)
bt9.place(x=335,y=210)


janela.mainloop()