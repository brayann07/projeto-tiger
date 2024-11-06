import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
# Conexão com o banco de dados
hotelbanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hoteltiger"
)
cursor = hotelbanco.cursor()
# Funções!
def validar(texto):
    if texto.isdigit() or texto =="":
        return True
    else:
        return False
def select():
    janela.destroy()
    font = ("Arial",15,"bold")
    janelaescolha= tk.Tk()
    janelaescolha.title("Seleção")
    janelaescolha.geometry("1920x1080")
    janelaescolha.configure(background="#c8dbde")
    titulo = tk.Label(janelaescolha, text="Qual seria o tipo de cadastro?", font=("Arial",20,"bold"),background="#c8dbde")
    titulo.pack()
    botaoclientes = tk.Button(janelaescolha, width=10, height=2, text="Cliente", font=font, background="#36A6B7", borderwidth=0, relief="flat", command=cadastrarclientes)
    botaoclientes.pack(pady=20)
    botaofuncionarios = tk.Button(janelaescolha,width=10, height=2, text="Funcionario", borderwidth=0, relief="flat", background="#36A6B7",font=font)
    botaofuncionarios.pack(pady=20)
    janelaescolha.mainloop()
def cadastrarclientes():
    janelanova = tk.Tk()
    validacao = janelanova.register(validar)
    janelanova.title("Hotel Tiger")
    janelanova.geometry("1920x1280")
    janelanova.configure(background="#c8dbde")
    font=("Open Sans",13,"bold")

    imagema = Image.open("cadastro.png")
    imagema = imagema.resize((600,300))
    imagem_tka = ImageTk.PhotoImage(imagema)
    
    label_imagema = tk.Label(janelanova, image=imagem_tka, borderwidth=0,highlightthickness=0)
    label_imagema.pack() 

    nomeprint = tk.Label(janelanova, text="Nome",font=font,background='#c8dbde')
    nomeprint.pack(pady=10)
    nome = tk.Entry(janelanova, font=font,text="")
    nome.pack()

    cpfprint = tk.Label(janelanova, text="CPF",font=font,background='#c8dbde')
    cpfprint.pack(pady=10)
    cpf = tk.Entry(janelanova,font=font,text="", validate="key",validatecommand=(validacao, "%P"))
    cpf.pack()

    datainprint = tk.Label(janelanova, text="Data Check-IN",font=font,background='#c8dbde')
    datainprint.pack(pady=10)
    datain = tk.Entry(janelanova,font=font,text="")
    datain.pack()

    dataoutprint = tk.Label(janelanova, text="Data Check-Out",font=font,background='#c8dbde')
    dataoutprint.pack(pady=10)
    dataout = tk.Entry(janelanova,font=font,text="")
    dataout.pack()

    telefoneprint = tk.Label(janelanova, text="Telefone",font=font,background='#c8dbde')
    telefoneprint.pack(pady=10)
    telefone = tk.Entry(janelanova,font=font,text="",validate="key",validatecommand=(validacao, "%P"))
    telefone.pack()
    
    emailprint = tk.Label(janelanova, text="E-mail",font=font,background='#c8dbde',)
    emailprint.pack(pady=10)
    email = tk.Entry(janelanova,font=font,text="")
    email.pack()

    estadoprint = tk.Label(janelanova, text="Estado",font=font,background='#c8dbde')
    estadoprint.pack(pady=10)
    estado = tk.Entry(janelanova, font=font,text="")
    estado.pack()

    cidadeprint = tk.Label(janelanova, text="Cidade",font=font,background='#c8dbde')
    cidadeprint.pack(pady=10)
    cidade = tk.Entry(janelanova, font=font,text="")
    cidade.pack()

    quartoprint = tk.Label(janelanova, text="Número do Quarto",font=font,background='#c8dbde')
    quartoprint.pack(pady=10)
    quarto = tk.Entry(janelanova,font=font,text="",validate="key",validatecommand=(validacao, "%P"))
    quarto.pack()
    janelanova.mainloop()
# Interface Gráfica
janela = tk.Tk()
janela.title("Hotel Tiger")
janela.geometry("1920x1280")
janela.configure(background='#FFDAB9')
font = ("Arial",20,"bold")

imagem = Image.open("fundotiger.png")
imagem_tk = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(janela, image=imagem_tk, borderwidth=0,highlightthickness=0 )
label_imagem.pack(pady=10)

frame = tk.Frame(janela, background="#FFDAB9")
frame.pack(expand=True, padx=50, pady=50)
# botões do código
botaocadastrar = tk.Button(frame, width=15, height=2, text="Cadastrar", font=font, background="#f7c497", borderwidth=0, relief="flat", command=select)

botaoalterar = tk.Button(frame, width=15, height=2, text="Alterar", font=font, background="#f7c497", borderwidth=0, relief="flat")

botaopesquisa = tk.Button(frame, width=15, height=2, text="Pesquisar", font=font, background="#f7c497", borderwidth=0, relief="flat")

botaodeletar = tk.Button(frame, width=15, height=2, text="Excluir", font=font, background="#f7c497", borderwidth=0, relief="flat")
def sair():
    janela.destroy()
botaosair = tk.Button(frame, width=15, height=2, text="Sair", font=font, background="#f7c497", borderwidth=0, relief="flat",command=sair)


botaocadastrar.pack(side="left",padx=20)
botaoalterar.pack(side="left",padx=20)
botaopesquisa.pack(side="left",padx=20)
botaodeletar.pack(side="left",padx=20)
botaosair.pack(side="left",padx=20)

janela.mainloop()
