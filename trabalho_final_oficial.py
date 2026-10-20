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
arquivo_contas = "dados.txt"

saldo_inicial = 1000.00
0000000000
contas = {}

saldo_atual = 0.00

conta_atual = ""

#========================================
#     FUNÇÕES
#========================================
def botoes_laterais(estado):
    botao_consultar_saldo.config(state=estado)
    botao_sacar_dinheiro.config(state=estado)
    botao_depositar.config(state=estado)
    botao_sair.config(state=estado)

def carregar_contas():
    global contas

    contas = {}

    arquivo = open(arquivo_contas, "a")
    arquivo.close()
    arquivo = open(arquivo_contas, "r")

    for linha in arquivo:
        dados = linha.strip().split(";")

        if len(dados) == 2:
            contas[dados[0]] = float(dados[1])

    arquivo.close()

def salvar_contas():
    arquivo = open(arquivo_contas, "w")
    for conta, saldo in contas.items():
        arquivo.write(f"{conta};{saldo:.2f}\n")

    arquivo.close()

def abrir_frame_de_menu():
    global saldo_atual, conta_atual
    conta_atual = conta_entry.get().strip()
    if conta_atual == "":
        label_login.config(text="Digite o número da conta")
        return

    carregar_contas()

    if conta_atual in contas:
        saldo_atual = contas[conta_atual]
    else:
        saldo_atual = saldo_inicial
        contas[conta_atual] = saldo_atual
        salvar_contas()

    label_login.config(text="")
    botoes_laterais("normal")
    frame_de_menu.lift()

def atualizar_saldo():
    if conta_atual != "":
        contas[conta_atual] = saldo_atual
        salvar_contas()

def sacar_dinheiro(valor):
    global saldo_atual

    if valor > 0 and valor <= saldo_atual:
        saldo_atual -= valor
        atualizar_saldo()
        return True

    return False

def depositar_dinheiro(valor):
    global saldo_atual

    if valor > 0:
        saldo_atual += valor
        atualizar_saldo()
        return True

    return False

def consultar_saldo():
    label_saldo.config(
        text=f"R$ {saldo_atual:.2f}".replace(".", ",")
    )
    frame_consultar_saldo.lift()

def abrir_consultar_saldo():
    botoes_laterais("disabled")
    consultar_saldo()

def abrir_sacar_dinheiro():
    label_resultado_saque.config(text="")
    valor_saque.delete(0, END)
    botoes_laterais("disabled")
    frame_sacar_dinheiro.lift()

def abrir_depositar_dinheiro():
    label_resultado_deposito.config(text="")
    valor_deposito.delete(0, END)
    botoes_laterais("disabled")
    frame_depositar_dinheiro.lift()

def sacar():
    texto = valor_saque.get().strip().replace(",", ".")

    if texto == "":
        label_resultado_saque.config(text="Digite o valor do saque")
        return

    if not texto.isdigit():
        label_resultado_saque.config(
            text="Erro: digite um valor inteiro, sem letras ou decimais"
        )
        return

    valor = int(texto)

    if valor <= 0:
        label_resultado_saque.config(text="Digite um valor positivo")
        return

    if valor > saldo_atual:
        label_resultado_saque.config(text="Erro: saldo insuficiente")
        return

    # Encontra uma combinação de cédulas para o valor solicitado.
    cedulas = [100, 50, 20, 10, 5, 2]
    combinacoes = {0: []}

    for total in range(1, valor + 1):
        combinacoes[total] = None
        for cedula in cedulas:
            anterior = total - cedula
            if anterior >= 0 and combinacoes[anterior] is not None:
                tentativa = combinacoes[anterior] + [cedula]
                if combinacoes[total] is None or len(tentativa) < len(combinacoes[total]):
                    combinacoes[total] = tentativa

    if combinacoes[valor] is None:
        label_resultado_saque.config(
            text="O caixa não consegue formar esse valor com as cédulas disponíveis"
        )
        return

    if not sacar_dinheiro(valor):
        label_resultado_saque.config(text="Erro: saque não realizado")
        return

    valor_saque.delete(0, END)

    quantidades = {}
    for cedula in combinacoes[valor]:
        quantidades[cedula] = quantidades.get(cedula, 0) + 1

    resultado = ["Saque realizado com sucesso!"]
    for cedula in cedulas:
        quantidade = quantidades.get(cedula, 0)
        if quantidade > 0:
            nome = "cédula" if quantidade == 1 else "cédulas"
            resultado.append(f"{quantidade} {nome} de R$ {cedula}")

    resultado.append(
        f"Saldo atual: R$ {saldo_atual:.2f}".replace(".", ",")
    )
    label_resultado_saque.config(text="\n".join(resultado))

def depositar():
    texto = valor_deposito.get().strip().replace(",", ".")

    if texto == "":
        label_resultado_deposito.config(text="Digite o valor do depósito")
        return

    if not texto.isdigit():
        label_resultado_deposito.config(
            text="Erro: digite um valor inteiro, sem letras ou decimais"
        )
        return

    valor = int(texto)

    if valor <= 0:
        label_resultado_deposito.config(
            text="Digite um valor inteiro positivo"
        )
        return
    depositar_dinheiro(valor)
    valor_deposito.delete(0, END)

    label_resultado_deposito.config(
        text=(
            "Depósito realizado com sucesso!\n"
            + f"Saldo atual: R$ {saldo_atual:.2f}".replace(".", ",")
        )
    )

def sair():
    atualizar_saldo()
    janela.destroy()

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

label_login = Label(frame_de_abertura, text="Digite o número da conta",
                         font=("robot", 8, "bold"),
                         justify="center", fg="#0057B8")
label_login.place(x=225, y=125, anchor="n", width=200, height=25)

Label(frame_de_abertura, text="Número da Conta:",
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
                     ).place(x=0, y=35, width=450, height=40)

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
botao_consultar_saldo = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, 
                               bg="#8A8A8A", bd=5, command=lambda: abrir_consultar_saldo()
                               if frame_de_menu.winfo_viewable() else None)
botao_consultar_saldo.place(x=15, y=150)

botao_sacar_dinheiro = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5, command=abrir_sacar_dinheiro)
botao_sacar_dinheiro.place(x=570, y=150)

botao_depositar = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5, command=abrir_depositar_dinheiro)
botao_depositar.place(x=15, y=300)

botao_sair = Button(canvas, font=("robot", 12, "bold"), width=5, height=5, bg="#8A8A8A", bd=5, command=sair)
botao_sair.place(x=570, y=300)

botoes_laterais("disabled")
#========================================
#     FRAME CONSULTAR SALDO
#========================================
frame_consultar_saldo = Frame(canvas, width=450, height=400)
frame_consultar_saldo.place(x=100, y=50)

label_fundo_2 = Label(frame_consultar_saldo, image=fundo_2, bd=0)
label_fundo_2.place(x=0, y=0)

Label(frame_consultar_saldo, text="CONSULTAR SALDO",
     font=("robot", 20, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=0, y=35, width=450, height=40)

Label(frame_consultar_saldo, text="SALDO DISPONÍVEL",
     font=("robot", 11, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=50, y=120, width=350, height=25)

frame_painel_saldo = Frame(frame_consultar_saldo, bg="#EAF3FF",
                          highlightbackground="#0057B8",
                          highlightthickness=2
                          )
frame_painel_saldo.place(x=50, y=155, width=350, height=80)

label_saldo = Label(frame_painel_saldo, text="R$ 1000,00",
                   font=("robot", 22, "bold"), fg="#0057B8",
                   bg="#EAF3FF"
                   )
label_saldo.place(relx=0.5, rely=0.5, anchor="center")

Button(frame_consultar_saldo, text="VOLTAR",
      font=("robot", 11, "bold"), bg="#0057B8",
      fg="white", command=lambda: (frame_de_menu.lift(), botoes_laterais("normal")
)).place(x=125, y=300, width=200, height=35)

frame_consultar_saldo.lower()

#========================================
#     FRAME DE SACAR DINHEIRO
#========================================
frame_sacar_dinheiro = Frame(canvas, width=450, height=400)
frame_sacar_dinheiro.place(x=100, y=50)

label_fundo_2 = Label(frame_sacar_dinheiro, image=fundo_2, bd=0)
label_fundo_2.place(x=0, y=0)

Label(frame_sacar_dinheiro, text="SACAR DINHEIRO",
     font=("robot", 20, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=0, y=35, width=450, height=40)

Label(frame_sacar_dinheiro, text="DIGITE O VALOR DO SAQUE",
     font=("robot", 11, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=50, y=120, width=350, height=25)

frame_painel_saque = Frame(frame_sacar_dinheiro, bg="#EAF3FF",
                          highlightbackground="#0057B8", highlightthickness=2
                          )
frame_painel_saque.place(x=50, y=155, width=350, height=80)

valor_saque = Entry(frame_painel_saque, font=("robot", 18, "bold"),
                   justify="center", bd=0,
                   bg="#EAF3FF", fg="#0057B8"
                   )
valor_saque.place(x=10, y=15, width=326, height=45)

Button(frame_sacar_dinheiro, text="CONFIRMAR SAQUE",
      font=("robot", 10, "bold"), bg="#0057B8",
      fg="white", command=sacar
      ).place(x=125, y=250, width=200, height=35)

label_resultado_saque = Label(frame_sacar_dinheiro, text="",
                             font=("robot", 9, "bold"), fg="#0057B8",
                             bg="white"
                             )
label_resultado_saque.place(x=15, y=280, width=420, height=55)

Button(frame_sacar_dinheiro, text="VOLTAR",
      font=("robot", 11, "bold"), bg="#0057B8",
      fg="white", command=lambda: (frame_de_menu.lift(), botoes_laterais("normal")
)).place(x=125, y=335, width=200, height=35)

frame_sacar_dinheiro.lower()

#========================================
#     FRAME DE DEPOSITAR DINHEIRO
#========================================
frame_depositar_dinheiro = Frame(canvas, width=450, height=400)
frame_depositar_dinheiro.place(x=100, y=50)

label_fundo_2 = Label(frame_depositar_dinheiro, image=fundo_2, bd=0)
label_fundo_2.place(x=0, y=0)

Label(frame_depositar_dinheiro, text="DEPOSITAR DINHEIRO",
     font=("robot", 18, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=0, y=35, width=450, height=40)

Label(frame_depositar_dinheiro, text="DIGITE O VALOR DO DEPÓSITO",
     font=("robot", 11, "bold"), fg="#0057B8",
     bg="white"
     ).place(x=50, y=120, width=350, height=25)

frame_painel_deposito = Frame(frame_depositar_dinheiro, bg="#EAF3FF",
                             highlightbackground="#0057B8", highlightthickness=2
                             )
frame_painel_deposito.place(x=50, y=155, width=350, height=80)

valor_deposito = Entry(frame_painel_deposito, font=("robot", 18, "bold"),
                      justify="center", bd=0,
                      bg="#EAF3FF", fg="#0057B8"
                      )
valor_deposito.place(x=10, y=15, width=326, height=45)

Button(frame_depositar_dinheiro, text="CONFIRMAR DEPÓSITO",
      font=("robot", 10, "bold"), bg="#0057B8",
      fg="white", command=depositar
      ).place(x=125, y=250, width=200, height=35)

label_resultado_deposito = Label(frame_depositar_dinheiro, text="",
                                font=("robot", 9, "bold"), fg="#0057B8",
                                bg="white"
                                )
label_resultado_deposito.place(x=15, y=280, width=420, height=45)

Button(frame_depositar_dinheiro, text="VOLTAR",
      font=("robot", 11, "bold"), bg="#0057B8",
      fg="white", command=lambda: (frame_de_menu.lift(), botoes_laterais("normal")
)).place(x=125, y=335, width=200, height=35)

frame_depositar_dinheiro.lower()

frame_de_abertura.lift()
janela.mainloop()