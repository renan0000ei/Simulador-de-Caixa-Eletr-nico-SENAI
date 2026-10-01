#========================================
#     IMPORTANDO        
#========================================
from tkinter import *
from tkinter import Canvas
from tkinter import ttk

#========================================
#     CRIANDO JANELA        
#========================================
janela = Tk()
janela.title("Simulador-de-Caixa-Eletronico-SENAI")
janela.geometry("570x480")
janela.configure(bg="#0057B8")
janela.resizable(False, False)

#CRIANDO CANVAS
canvas = Canvas(janela, width = 510,
                height = 450, bg="#E6E6E6",
                highlightthickness=2, highlightcolor="#D3D3D3")
canvas.pack()

#========================================
#    CONTEUDO FRAME DE ABERTURA         
#========================================

#CRIANDO FRAME DE ABERTURA
frame_de_abertura = Frame(canvas, width = 510,
                height = 450, bg="#E6E6E6",
                highlightthickness=2, highlightcolor="#D3D3D3")
frame_de_abertura.place(x=0, y=0)

#CRIANDO TITULO "BEM VINDO..." E "MENU"
Label(frame_de_abertura, text="BEM VINDO\n" \
                                 "AO\n" \
                           "CAIXA ELETRONICO", 
                           font=("robot", 15 ,"bold",),
                           justify="center", fg="#0057B8"
                           ).place(x=255, y=30, anchor="n")

Label(frame_de_abertura, text="MENU", 
                           font=("robot", 10 ,"bold",),
                           justify="center", fg="#0057B8"
                           ).place(x=255, y=135, anchor="n")

#CRIANDO AS OPÇÕES(BOTÕES)
botao_consultar_saldo = Button(frame_de_abertura, text="CONSULTAR SALDO", 
                                font=("robot", 10 ,"bold",),fg="#0057B8", width=20, height=2)
botao_consultar_saldo.place(x=255, y=190, anchor="n")

botao_sacar_dinheiro = Button(frame_de_abertura, text="SACAR DINHEIRO", 
                                font=("robot", 10 ,"bold",),fg="#0057B8", width=20, height=2)
botao_sacar_dinheiro.place(x=255, y=240, anchor="n")

botao_depositar = Button(frame_de_abertura, text="DEPOSITAR", 
                                font=("robot", 10 ,"bold",),fg="#0057B8", width=20, height=2)
botao_depositar.place(x=255, y=290, anchor="n")

botao_sair = Button(frame_de_abertura, text="SAIR", 
                                font=("robot", 10 ,"bold",),fg="#0057B8",)
botao_sair.place(x=255, y=340, anchor="n")

frame_de_abertura.lift()
janela.mainloop()