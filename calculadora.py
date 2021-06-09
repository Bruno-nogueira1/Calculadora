from math import factorial, sqrt
from tkinter import *
from pyautogui import press

def apagar1():
    numero.delete(len(numero.get())-1)

def fatorial1(): 
    n1 = float(numero.get())
    n1 = factorial(n1)
    n2 = str(n1)
    numero.delete(0,END)
    numero.insert(0,n2)

def potencia1():
    n1 = float(numero.get())
    n2 = n1
    n1 = n1*n2
    n3 = str(n1)
    numero.delete(0,END)
    numero.insert(0,n3)

def raiz1():
    n1 = float(numero.get())
    n1 = sqrt(n1)
    n2 = str(n1)
    numero.delete(0,END)
    numero.insert(0,n2)

def igual1():
    n = numero.get()
    n1 = float(eval(numero.get()))
    n2 = n1
    numero.delete(0,END)
    numero.insert(0,n2)

root = Tk()
root.resizable(False,False)
root.config(background='#9f9fa3')
root.title('Calculadora')
root.iconbitmap('calculadoralogo.ico')
root.geometry('250x400')

imageigual = PhotoImage(file='iguallogo.png')
igual = Button(root,image=imageigual,background='#bfbfbf',command=igual1).place(x=190, y=340)

imagesoma = PhotoImage(file='somalogo.png')
soma = Button(root, image=imagesoma,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'+')).place(x=190,y=280)

imagemenos = PhotoImage(file='menoslogo.png')
menos = Button(root,image=imagemenos,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'-')).place(x=190, y=220)

imagevezes = PhotoImage(file='vezeslogo.png')
vezes = Button(root,image=imagevezes,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'*')).place(x=190, y=160)

imagedivisao = PhotoImage(file='divisaologo.png')
divisao = Button(root,image=imagedivisao,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'/')).place(x=67.5, y=100)

imageapagar = PhotoImage(file='apagarlogo.png')
apagar = Button(root,image=imageapagar,background='#bfbfbf',command=apagar1).place(x=190, y=100)

imagepotencia = PhotoImage(file='potencialogo.png')
potencia = Button(root,image=imagepotencia,background='#bfbfbf',command=potencia1).place(x=127.5, y=100)

imageraiz = PhotoImage(file='raizlogo.png')
raiz = Button(root,image=imageraiz,background='#bfbfbf',command=raiz1).place(x=5, y=100)

imagevirgula = PhotoImage(file='virgulalogo.png')
virgula = Button(root,image=imagevirgula,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'.')).place(x=127.5, y=340)

imagefatorial = PhotoImage(file='fatoriallogo.png')
fatorial = Button(root,image=imagefatorial,background='#bfbfbf',command=fatorial1).place(x=5, y=340)

image1 = PhotoImage(file='1logo.png')
image2 = PhotoImage(file='2logo.png')
image3 = PhotoImage(file='3logo.png')
image4 = PhotoImage(file='4logo.png')
image5 = PhotoImage(file='5logo.png')
image6 = PhotoImage(file='6logo.png')
image7 = PhotoImage(file='7logo.png')
image8 = PhotoImage(file='8logo.png')
image9 = PhotoImage(file='9logo.png')
image0 = PhotoImage(file='0logo.png')

um = Button(root,image=image1,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'1')).place(x=5, y=160)
dois = Button(root,image=image2,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'2')).place(x=67.5, y=160)
tres = Button(root,image=image3,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'3')).place(x=127.5, y=160)
quatro = Button(root,image=image4,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'4')).place(x=5, y=220)
cinco = Button(root,image=image5,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'5')).place(x=67.5, y=220)
seis = Button(root,image=image6,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'6')).place(x=127.5, y=220)
sete = Button(root,image=image7,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'7')).place(x=5, y=280)
oito = Button(root,image=image8,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'8')).place(x=67.5, y=280)
nove = Button(root,image=image9,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'9')).place(x=127.5, y=280)
zero = Button(root,image=image0,background='#bfbfbf',command=lambda:numero.insert((len(numero.get())),'0')).place(x=67.5, y=340)

numero = Entry(background='#eff3f6',borderwidth=4,relief="ridge",justify='right',font= 'Calibri 25 bold')
numero.place(x=5,y=10,width=240,height=70) 

root.mainloop()