#========================================
#     IMPORTANDO        
#========================================
from tkinter import *
from tkinter import Canvas
from tkinter import ttk
from PIL import Image, ImageTk

#========================================
#     CONTA     
#========================================
conta = "12345"
saldo = 1000.00


#========================================
#     FUNÇÕES     
#========================================
def abrir_frame_de_menu():
    if conta == conta_entry.get():
        frame_de_menu.lift()
#========================================
#     CRIANDO JANELA        
#========================================
janela = Tk()
janela.title("Simulador-de-Caixa-Eletronico-SENAI")
janela.geometry("650x500")
janela.resizable(False, False)

#CRIANDO CANVAS
canvas = Canvas(janela, width = 650,
                height = 500, bg="#4A4A4A")
canvas.pack()

imagem_1 = Image.open("imagem.png")
imagem_1 = imagem_1.resize((650, 500))
fundo_1 = ImageTk.PhotoImage(imagem_1)

canvas.create_image(0, 0, image=fundo_1, anchor="nw")

#========================================
#     FRAME DE ABERTURA       
#========================================
frame_de_abertura = Frame(canvas, width=450, height=400)
frame_de_abertura.place(x=100, y=50)

imagem_2 = Image.open("image.png")
imagem_2 = imagem_2.resize((450, 400))
fundo_2 = ImageTk.PhotoImage(imagem_2)

label_fundo_2 = Label(frame_de_abertura, image=fundo_2, bd=0)
label_fundo_2.place(x=0, y=0)

Label(frame_de_abertura, text="BEM VINDO\n" \
                                 "AO\n" \
                           "CAIXA ELETRÔNICO", 
                          font=("robot", 15 ,"bold",),
                          justify="center", fg="#0057B8"
                          ).place(x=225, y=30, anchor="n")

Label(frame_de_abertura, text="Digite as Informaçês de Login", 
                         font=("robot", 8 ,"bold",),
                         justify="center", fg="#0057B8"
                         ).place(x=225, y=125, anchor="n", width=200, height=25)

Label(frame_de_abertura, text="Nome de Usuário:",
                         font=("robot", 12 ,"bold",),
                         justify="center", fg="#0057B8").place(x=225, y=175, anchor="n", width=200, height=25)

conta_entry = Entry(frame_de_abertura, justify="center")
conta_entry.place(x=225, y=210, anchor="n", width=200, height=25)

Label(frame_de_abertura, text="Senha:",
                         font=("robot", 12 ,"bold",),
                         justify="center", fg="#0057B8").place(x=225, y=250, anchor="n", width=200, height=25)

senha = Entry(frame_de_abertura, justify="center", show="*")
senha.place(x=225, y=285, anchor="n", width=200, height=25)

entrar = Button(frame_de_abertura, text="ENTRAR", font=("robot", 12 ,"bold",),
                 bg="#0057B8", fg="white", command=abrir_frame_de_menu)
entrar.place(x=225, y=330, anchor="n", width=200, height=30)

#========================================
#     FRAME DE MENU       
#========================================
frame_de_menu = Frame(canvas, width=450, height=400)
frame_de_menu.place(x=100, y=50)

label_fundo_2 = Label(frame_de_menu, image=fundo_2, bd=0)
label_fundo_2.place(x=0, y=0)

Label(frame_de_menu, text="MENU", 
                     font=("robot", 25 ,"bold",),
                     justify="center", fg="#0057B8"
                     ).place(x=225, y=30, anchor="n", width=200, height=50)

Label(frame_de_menu, text="1. Consultar\n o saldo", font=("robot", 15 ,"bold",),
                     fg="#0057B8"
                     ).place(x=50, y=100, width=150, height=110)

Label(frame_de_menu, text="2. Sacar\n dinheiro", font=("robot", 15 ,"bold",),
                     fg="#0057B8"
                     ).place(x=250, y=100, width=150, height=110)

Label(frame_de_menu, text="3. Depositar\n dinheiro", font=("robot", 15 ,"bold",),
                     fg="#0057B8"
                     ).place(x=50, y=250, width=150, height=110)

Label(frame_de_menu, text="4. Sair", font=("robot", 15 ,"bold",),
                     fg="#0057B8"
                     ).place(x=250, y=250, width=150, height=110)

#========================================
#     MOLDURA        
#========================================
# MOLDURA SUPERIOR - PAREDE INTERNA
canvas.create_polygon(
    90, 25,
    560, 25,
    510, 150,
    140, 150,
    fill="#292929", outline="#1A1A1A", width=3)

# MOLDURA ESQUERDA - PAREDE INTERNA
canvas.create_polygon(
    90, 25,
    140, 150,
    140, 350,
    90, 485,
    fill="#292929", outline="#1A1A1A", width=3)

# MOLDURA DIREITA - PAREDE INTERNA
canvas.create_polygon(
    560, 25,
    510, 150,
    510, 350,
    560, 485,
    fill="#B0B0B0", outline="#777777", width=3)

# # MOLDURA INFERIOR - PAREDE INTERNA
canvas.create_polygon(
    90, 485,
    140, 350,
    510, 350,
    560, 485,
    fill="#666666", outline="#333333", width=3)

#========================================
#     BOTOES        
#========================================
botao_consultar_saldo = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5)
botao_consultar_saldo.place(x=15, y=150)

botao_sacar_dinheiro = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5)
botao_sacar_dinheiro.place(x=570, y=150)

botao_depositar = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5)
botao_depositar.place(x=15, y=300)

botao_sair = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5)
botao_sair.place(x=570, y=300)

frame_de_abertura.lift()
janela.mainloop()