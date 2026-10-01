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
janela.geometry("650x500")
janela.configure(bg="#D3D3D3")
janela.resizable(False, False)

#CRIANDO CANVAS
canvas = Canvas(janela, width = 650,
                height = 500, bg="#4A4A4A")
canvas.pack()

#========================================
#     FRAMES        
#========================================
frame_de_abertura = Frame(canvas, width=450, height=400, bg="#C9E6F3")
frame_de_abertura.place(x=100, y=50)

#========================================
#     BOTÕES        
#========================================
botao_consultar_saldo = Button(canvas, text=">", font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", fg="#F2F2F2")
botao_consultar_saldo.place(x=25, y=150)

botao_sacar_dinheiro = Button(canvas, text="<", font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", fg="#F2F2F2")
botao_sacar_dinheiro.place(x=570, y=150)

botao_depositar = Button(canvas, text=">", font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", fg="#F2F2F2")
botao_depositar.place(x=25, y=300)

botao_sair = Button(canvas, text="<", font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", fg="#F2F2F2")
botao_sair.place(x=570, y=300)

janela.mainloop()