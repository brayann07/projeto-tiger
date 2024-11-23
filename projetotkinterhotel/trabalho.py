import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
hotelbanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hoteltiger"
)
cursor = hotelbanco.cursor()
def deleteselect():
    janelaselecao = tk.Tk()
    janelaselecao.title("Hotel Tiger")
    janelaselecao.geometry("1920x1280")
    janelaselecao.configure(background="#c8dbde")

    font=("Comic Sans MS",20)

    titulo = tk.Label(janelaselecao, text="Quem será descadastrado?", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    titulo.pack()

    frame = tk.Frame(janelaselecao, bg="#c8dbde")
    frame.pack(pady=10)
    botaoclientes = tk.Button(frame, width=10, height=1,font=font, text="Clientes",background="#bed1d4", borderwidth=0, relief="flat", command=deletarclientes)
    botaoclientes.pack(side="left", padx=30)

    botaovoltar = tk.Button(frame, width=10, height=1,font=font, text="Funcionários",background="#bed1d4", borderwidth=0, relief="flat", command=deletarfuncionarios)
    botaovoltar.pack(side="left", padx=30)
def validar(texto):
    if texto.isdigit() or texto =="":
        return True
    else:
        return False
def selecao():
    janelaselecao = tk.Tk()
    janelaselecao.title("Hotel Tiger")
    janelaselecao.geometry("1920x1280")
    janelaselecao.configure(background="#c8dbde")
    font=("Comic Sans MS",  20) 
    titulo = tk.Label(janelaselecao, text="Qual seria o tipo de cadastro?", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    titulo.pack()

    frame = tk.Frame(janelaselecao, bg="#c8dbde")
    frame.pack(pady=10)
    botaoclientes = tk.Button(frame, width=10, height=1, text="Clientes", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=cadastrarclientes)
    botaoclientes.pack(side="left", padx=30)

    botaovoltar = tk.Button(frame, width=10, height=1, text="Funcionários", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=cadastrarfuncionarios)
    botaovoltar.pack(side="left", padx=30)
    janelaselecao.mainloop()

def cadastrarclientes():
    janelaclientes = tk.Tk()
    janelaclientes.title("Hotel Tiger")
    janelaclientes.geometry("1920x1280")
    janelaclientes.configure(background="#c8dbde")
    validacao = janelaclientes.register(validar)
    font=("Comic Sans MS",20)
    titulo = tk.Label(janelaclientes, text="Cadastro", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack()

    idprint = tk.Label(janelaclientes, text="Id do Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(janelaclientes, font=font, validate="key", validatecommand=(validacao, "%P"))
    idclientes.pack()

    nomeprint = tk.Label(janelaclientes, text="Nome", font=font, background='#c8dbde')
    nomeprint.pack(pady=10)
    nome = tk.Entry(janelaclientes, font=font)
    nome.pack()

    cpfprint = tk.Label(janelaclientes, text="CPF", font=font, background='#c8dbde')
    cpfprint.pack(pady=10)
    cpf = tk.Entry(janelaclientes, font=font, validate="key", validatecommand=(validacao, "%P"))
    cpf.pack()

    datainprint = tk.Label(janelaclientes, text="Data Check-IN", font=font, background='#c8dbde')
    datainprint.pack(pady=10)
    datain = tk.Entry(janelaclientes, font=font)
    datain.pack()

    dataoutprint = tk.Label(janelaclientes, text="Data Check-Out", font=font, background='#c8dbde')
    dataoutprint.pack(pady=10)
    dataout = tk.Entry(janelaclientes, font=font)
    dataout.pack()

    telefoneprint = tk.Label(janelaclientes, text="Telefone", font=font, background='#c8dbde')
    telefoneprint.pack(pady=10)
    telefone = tk.Entry(janelaclientes, font=font, validate="key", validatecommand=(validacao, "%P"))
    telefone.pack()

    emailprint = tk.Label(janelaclientes, text="E-mail", font=font, background='#c8dbde')
    emailprint.pack(pady=10)
    email = tk.Entry(janelaclientes, font=font)
    email.pack()

    estadoprint = tk.Label(janelaclientes, text="Estado", font=font, background='#c8dbde')
    estadoprint.pack(pady=10)
    estado = tk.Entry(janelaclientes, font=font)
    estado.pack()

    cidadeprint = tk.Label(janelaclientes, text="Cidade", font=font, background='#c8dbde')
    cidadeprint.pack(pady=10)
    cidade = tk.Entry(janelaclientes, font=font)
    cidade.pack()

    quartoprint = tk.Label(janelaclientes, text="Número do Quarto", font=font, background='#c8dbde')
    quartoprint.pack(pady=10)
    quarto = tk.Entry(janelaclientes, font=font, validate="key", validatecommand=(validacao, "%P"))
    quarto.pack()

    frame_botoes = tk.Frame(janelaclientes, bg="#c8dbde")
    frame_botoes.pack(pady=20)

    def pegar():
        idclientis = idclientes.get()
        nomecliente = nome.get()
        cpfcliente = cpf.get()
        datacheckin = datain.get()
        datacheckout = dataout.get()
        telefonecliente = telefone.get()
        emailcliente = email.get()
        estadocliente = estado.get()
        cidadecliente = cidade.get()
        numeroquarto = quarto.get()

        campos_obrigatorios = [
            ("ID Cliente", idclientis),
            ("Nome", nomecliente),
            ("CPF", cpfcliente),
            ("Data Check-in", datacheckin),
            ("Data Check-out", datacheckout),
            ("Telefone Cliente", telefonecliente),
            ("E-Mail Cliente", emailcliente),
            ("Estado Cliente", estadocliente),
            ("Cidade Cliente", cidadecliente),
            ("Número Quarto", numeroquarto)
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            inserir(idclientis, nomecliente, cpfcliente, datacheckin, datacheckout, telefonecliente, emailcliente, estadocliente, cidadecliente, numeroquarto)

    def inserir(idclientis, nomecliente, cpfcliente, datacheckin, datacheckout, telefonecliente, emailcliente, estadocliente, cidadecliente, numeroquarto):
        comando_pesquisa = f'SELECT * FROM cliente where idcliente= {idclientis}'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchone()
        if x:
            mensagem.config(text="Já existe esse código!")
        else:
            comando_cadastrar = f'INSERT INTO cliente(idcliente,nome,cpf,datacheckin,datacheckout,telefone,email,estado,cidade,codquarto) VALUES({idclientis},"{nomecliente}",{cpfcliente},"{datacheckin}","{datacheckout}",{telefonecliente},"{emailcliente}","{estadocliente}","{cidadecliente}",{numeroquarto})'
            x = "Ocupado"
            comando_troca = f'UPDATE quarto SET estado = "{x}" WHERE numquarto = {numeroquarto}'
            cursor.execute(comando_cadastrar)
            hotelbanco.commit()
            cursor.execute(comando_troca)
            hotelbanco.commit()
            mensagem.config(text="Cadastro realizado com sucesso!")

    botaocadastro = tk.Button(frame_botoes, width=9, height=1, text="Cadastrar", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=pegar)
    botaocadastro.pack(side="left", padx=20)

    botaovoltar = tk.Button(frame_botoes, width=9, height=1, text="Voltar", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=lambda: janelaclientes.destroy())
    botaovoltar.pack(side="left", padx=20)

    
    mensagem = tk.Label(janelaclientes, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    janelaclientes.mainloop()
def cadastrarfuncionarios():
    janelafuncionarios = tk.Tk()
    janelafuncionarios.title("Hotel Tiger")
 
    janelafuncionarios.geometry("1920x1280")
    janelafuncionarios.configure(background="#c8dbde")
    validacao = janelafuncionarios.register(validar)
    font=("Comic Sans MS",20)
        
    titulo = tk.Label(janelafuncionarios, text="Cadastro", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack()

    idprint = tk.Label(janelafuncionarios, text="Id do Funcionário", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idfuncionarios = tk.Entry(janelafuncionarios, font=font, validate="key", validatecommand=(validacao, "%P"))
    idfuncionarios.pack()

    nomeprint = tk.Label(janelafuncionarios, text="Nome", font=font, background='#c8dbde')
    nomeprint.pack(pady=10)
    nome = tk.Entry(janelafuncionarios, font=font)
    nome.pack()

    cpfprint = tk.Label(janelafuncionarios, text="CPF", font=font, background='#c8dbde')
    cpfprint.pack(pady=10)
    cpf = tk.Entry(janelafuncionarios, font=font, validate="key", validatecommand=(validacao, "%P"))
    cpf.pack()

    telefoneprint = tk.Label(janelafuncionarios, text="Telefone", font=font, background='#c8dbde')
    telefoneprint.pack(pady=10)
    telefone = tk.Entry(janelafuncionarios, font=font, validate="key", validatecommand=(validacao, "%P"))
    telefone.pack()

    emailprint = tk.Label(janelafuncionarios, text="E-mail", font=font, background='#c8dbde')
    emailprint.pack(pady=10)
    email = tk.Entry(janelafuncionarios, font=font)
    email.pack()

    estadoprint = tk.Label(janelafuncionarios, text="Estado", font=font, background='#c8dbde')
    estadoprint.pack(pady=10)
    estado = tk.Entry(janelafuncionarios, font=font)
    estado.pack()

    cidadeprint = tk.Label(janelafuncionarios, text="Cidade", font=font, background='#c8dbde')
    cidadeprint.pack(pady=10)
    cidade = tk.Entry(janelafuncionarios, font=font)
    cidade.pack()

    cargoprint = tk.Label(janelafuncionarios, text="Cargo", font=font, background='#c8dbde')
    cargoprint.pack(pady=10)
    cargo = tk.Entry(janelafuncionarios, font=font)
    cargo.pack()

    cargahorariaprint = tk.Label(janelafuncionarios, text="Carga Horária", font=font, background='#c8dbde')
    cargahorariaprint.pack(pady=10)
    cargahoraria= tk.Entry(janelafuncionarios, font=font, validate="key", validatecommand=(validacao, "%P"))
    cargahoraria.pack()

    turnoprint = tk.Label(janelafuncionarios, text="Turno", font=font, background='#c8dbde')
    turnoprint.pack(pady=10)
    turno = tk.Entry(janelafuncionarios, font=font)
    turno.pack()   
    def pegarfuncionarios():
        idfuncionario = idfuncionarios.get()
        nomefuncionario = nome.get()
        cpffuncionario = cpf.get()
        telefonefuncionario= telefone.get()
        emailfuncionario = email.get()
        estadofuncionario = estado.get()
        cidadefuncionario= cidade.get()
        cargofuncionario= cargo.get()
        cargahorariafuncionarios = cargahoraria.get()
        turnofuncionarios = turno.get()
        campos_obrigatorios = [
            ("ID Funcionário", idfuncionario),
            ("Nome", nomefuncionario),
            ("CPF", cpffuncionario),
            ("Telefone Funcionario", telefonefuncionario),
            ("E-Mail Funcionario", emailfuncionario),
            ("Estado Funcionario", estadofuncionario),
            ("Cidade Funcionário", cidadefuncionario),
            ("Cargo Funcionário", cargofuncionario),
            ("Carga Horária",cargahorariafuncionarios),
            ("Turno Funcionários",turnofuncionarios),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta Informações!")
        else:
            inserirfuncionarios(idfuncionario, nomefuncionario, cpffuncionario,telefonefuncionario, emailfuncionario, estadofuncionario, cidadefuncionario, cargofuncionario,cargahorariafuncionarios,turnofuncionarios)

    def inserirfuncionarios(idfuncionario, nomefuncionario, cpffuncionario,telefonefuncionario, emailfuncionario, estadofuncionario, cidadefuncionario, cargofuncionario,cargahorariafuncionarios,turnofuncionarios):
            comando_pesquisa = f'SELECT * FROM funcionarios where idfuncionarios= {idfuncionario}'
            cursor.execute(comando_pesquisa)
            x = cursor.fetchone()
            if x:
                mensagem.config(text="Já existe esse código!")
            else:
                comando_cadastrar = f'INSERT INTO funcionarios(idfuncionarios,nome,cargo,cargahoraria,turno,email,estado,cidade,telefone,cpf) VALUES({idfuncionario},"{nomefuncionario}","{cargofuncionario}",{cargahorariafuncionarios},"{turnofuncionarios}","{emailfuncionario}","{estadofuncionario}","{cidadefuncionario}",{telefonefuncionario},{cpffuncionario})'
                hotelbanco.commit()
                cursor.execute(comando_cadastrar)
                hotelbanco.commit()
                mensagem.config(text="Cadastrado com sucesso")

    
    frame_botoes = tk.Frame(janelafuncionarios, bg="#c8dbde")
    frame_botoes.pack(pady=20)  

    botaocadastro = tk.Button(frame_botoes, width=9, height=1, text="Cadastrar", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=pegarfuncionarios)
    botaocadastro.pack(side="left", padx=20)

    botaovoltar = tk.Button(frame_botoes, width=9, height=1, text="Voltar", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=lambda: janelafuncionarios.destroy())
    botaovoltar.pack(side="left", padx=20)


    mensagem = tk.Label(janelafuncionarios, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    janelafuncionarios.mainloop()

def deletarclientes():
    janelaclientes = tk.Tk()  
    janelaclientes.title("Hotel Tiger")
    janelaclientes.geometry("1920x1280")
    janelaclientes.configure(background="#c8dbde")
    validacao = janelaclientes.register(validar)
    
    font=("Comic Sans MS",20)

    titulo = tk.Label(janelaclientes, text="Deletar", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack()

    idprint = tk.Label(janelaclientes, text="Id do Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(janelaclientes, font=font,validate="key", validatecommand=(validacao, "%P"))
    idclientes.pack()

    codquartu = tk.Label(janelaclientes, text="Código do Quarto",font=font, background='#c8dbde')
    codquartu.pack(pady=10)
    codquarto = tk.Entry(janelaclientes, font=font,validate="key", validatecommand=(validacao, "%P"))
    codquarto.pack()

    def deletar():
        idclients = idclientes.get()
        codquarts = codquarto.get()
        delete(idclients, codquarts)


    def delete(idclients, codquarts):
        comando_pesquisa = f'SELECT * FROM cliente WHERE idcliente = {idclients}'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchone()
        if x:
            y = "Limpeza"
            comandoupdate = f'UPDATE quarto SET estado = "{y}" WHERE numquarto = {codquarts}'
            cursor.execute(comandoupdate)
            hotelbanco.commit() 
            comandodeletar = f'DELETE FROM cliente WHERE idcliente = {idclients}'
            cursor.execute(comandodeletar)
            hotelbanco.commit()
            mensagem.config(text="Deletado com sucesso")
        else:
            mensagem.config(text="Esse id não existe!")

    
    frame_botoes = tk.Frame(janelaclientes, bg="#c8dbde")
    frame_botoes.pack(pady=20)  

    botaocadastro = tk.Button(frame_botoes, width=7, height=1, text="Excluir", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=deletar)
    botaocadastro.pack(side="left",padx=20)

    botaovoltar = tk.Button(frame_botoes, width=7, height=1, text="Voltar", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=lambda: janelaclientes.destroy())
    botaovoltar.pack(side="left",padx=20)

    
    mensagem = tk.Label(janelaclientes, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    janelaclientes.mainloop()
def deletarfuncionarios():
    janelaclientes = tk.Tk()
    janelaclientes.title("Hotel Tiger")
    janelaclientes.geometry("1920x1280")
    janelaclientes.configure(background="#c8dbde")
    validacao = janelaclientes.register(validar)
    
    font=("Comic Sans MS",20)  

    titulo = tk.Label(janelaclientes, text="Deletar", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack()

    idprint = tk.Label(janelaclientes, text="Id do Funcionario", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idfun = tk.Entry(janelaclientes, font=font, validate="key", validatecommand=(validacao, "%P"))
    idfun.pack()
    def deletarfunc():
        idfuncionar= idfun.get()
        delete(idfuncionar)
    def delete(idfuncionar):
        comando_pesquisa = f'SELECT * FROM funcionarios where idfuncionarios= {idfuncionar}'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchone()
        if x:
            comandodeletar = f'DELETE FROM funcionarios where idfuncionarios={idfuncionar}'
            cursor.execute(comandodeletar)
            hotelbanco.commit()
            mensagem.config(text="Deletado com sucesso!")
        else:
            mensagem.config(text="Esse id não existe!")
    frame_botoes = tk.Frame(janelaclientes, bg="#c8dbde")
    frame_botoes.pack(pady=20)  
    
    botaocadastro = tk.Button(frame_botoes, width=7, height=1, text="Excluir", font=font, background="#bed1d4", borderwidth=0, relief="flat", command=deletarfunc)
    botaocadastro.pack(side="left", padx=20)

    botaovoltar = tk.Button(frame_botoes, width=7, height=1, text="Voltar", font=font, background="#bed1d4", borderwidth=0, relief="flat",command=lambda: janelaclientes.destroy())
    botaovoltar.pack(side="left", padx=20)
    
    mensagem = tk.Label(janelaclientes, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    janelaclientes.mainloop()

def idfunc():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    validacao = janelaselecao1.register(validar)
    font=("Comic Sans MS", 20)
    
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o id do funcionário?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Id do Funcionário", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    idclientes.pack()

    def idfunccolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            idcommitfunc(idgeral)

    def idcommitfunc(idgeral):
        comandopesquisa = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idgeral}'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum funcionário encontrado com esse id!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCARGO: {i[2]}\nCARGA HORÁRIA: {i[3]}\nTURNO: {i[4]}\nEMAIL: {i[5]}\nESTADO: {i[6]}\nCIDADE: {i[7]}\nTELEFONE: {i[8]}\nCPF: {i[9]}", font=font, bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=idfunccolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

   
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def nomefunc():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    font=("Comic Sans MS", 20)
    
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o Nome do funcionário?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Nome do Funcionário", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada, font=font)
    idclientes.pack()

    def nomefunccolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            nomecommitfunc(idgeral)

    def nomecommitfunc(idgeral):
        comandopesquisa = f'SELECT * FROM funcionarios WHERE nome like "{idgeral}"'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum funcionário encontrado com esse nome!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCARGO: {i[2]}\nCARGA HORÁRIA: {i[3]}\nTURNO: {i[4]}\nEMAIL: {i[5]}\nESTADO: {i[6]}\nCIDADE: {i[7]}\nTELEFONE: {i[8]}\nCPF: {i[9]}", font=font, bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=nomefunccolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def cargofunc():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    font=("Comic Sans MS", 20)
    
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o cargo do funcionário?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Cargo do Funcionário", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada, font=font)
    idclientes.pack()

    def cargofunccolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            cargocommitfunc(idgeral)

    def cargocommitfunc(idgeral):
        comandopesquisa = f'SELECT * FROM funcionarios WHERE cargo like "{idgeral}"'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum funcionário encontrado com esse cargo!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCARGO: {i[2]}\nCARGA HORÁRIA: {i[3]}\nTURNO: {i[4]}\nEMAIL: {i[5]}\nESTADO: {i[6]}\nCIDADE: {i[7]}\nTELEFONE: {i[8]}\nCPF: {i[9]}", font=font, bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=cargofunccolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def idclientes():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    validacao = janelaselecao1.register(validar)
    font=("Comic Sans MS", 20)
    
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o id do cliente?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Id do Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    idclientes.pack()

    def idclientecolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            idcommitcliente(idgeral)

    def idcommitcliente(idgeral):
        comandopesquisa = f'SELECT * FROM cliente WHERE idcliente = {idgeral}'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum cliente encontrado com esse id!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCPF: {i[2]}\nDATA CHECK-IN: {i[3]}\nDATA CHECK-OUT: {i[4]}\nTELEFONE: {i[5]}\nE-MAIL: {i[6]}\nESTADO: {i[7]}\nCIDADE: {i[8]}\nCÓDIGO DO QUARTO: {i[9]}", font=font,bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=idclientecolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar",  font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def nomeclientes():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    font=("Comic Sans MS", 20)
    
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o nome do cliente?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Nome do Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada,font=font)
    idclientes.pack()

    def nomeclientecolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            nomecommitcliente(idgeral)

    def nomecommitcliente(idgeral):
        comandopesquisa = f'SELECT * FROM cliente WHERE nome like "{idgeral}"'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum cliente encontrado com esse nome!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCPF: {i[2]}\nDATA CHECK-IN: {i[3]}\nDATA CHECK-OUT: {i[4]}\nTELEFONE: {i[5]}\nE-MAIL: {i[6]}\nESTADO: {i[7]}\nCIDADE: {i[8]}\nCÓDIGO DO QUARTO: {i[9]}", font=font,bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=nomeclientecolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def quartoclientes():
    janelaselecao1 = tk.Tk()
    janelaselecao1.title("Hotel Tiger")
    janelaselecao1.geometry("1920x1280")
    janelaselecao1.configure(background="#c8dbde")
    font=("Comic Sans MS", 20)
    validacao = janelaselecao1.register(validar)   
    frameentrada = tk.Frame(janelaselecao1, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada, text="Qual seria o quarto do cliente?", font=("Comic Sans MS", 30, "bold"), background="#c8dbde")
    titulo.pack(pady=20)

    idprint = tk.Label(frameentrada, text="Quarto do Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    idclientes = tk.Entry(frameentrada,font=font,validate="key",validatecommand=(validacao, "%P"))
    idclientes.pack()

    def quartoclientecolocar():
        mensagem.config(text="")
        
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()

        idgeral = idclientes.get()
        campos_obrigatorios = [("ID Cliente", idgeral)]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            quartocommitcliente(idgeral)

    def quartocommitcliente(idgeral):
        comandopesquisa = f'SELECT * FROM cliente WHERE codquarto = {idgeral}'
        cursor.execute(comandopesquisa)  
        dados_tabela = cursor.fetchall()

        if not dados_tabela:
            mensagem.config(text="Nenhum cliente encontrado com esse quarto!", fg="blue")
        else:
            for i in dados_tabela:
                resultado = tk.Label(resultado_frame, text=f"ID: {i[0]}\nNOME: {i[1]}\nCPF: {i[2]}\nDATA CHECK-IN: {i[3]}\nDATA CHECK-OUT: {i[4]}\nTELEFONE: {i[5]}\nE-MAIL: {i[6]}\nESTADO: {i[7]}\nCIDADE: {i[8]}\nCÓDIGO DO QUARTO: {i[9]}", font=font,bg="#bed1d4")
                resultado.pack()

    botaoidcliente = tk.Button(frameentrada, text="Pesquisar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=quartoclientecolocar)
    botaoidcliente.pack(side="top", padx=10, pady=10)

    botaonomecliente = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaselecao1.destroy())
    botaonomecliente.pack(side="top", padx=10, pady=10)

    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)

    resultado_frame = tk.Frame(janelaselecao1, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Resultados", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)

    janelaselecao1.mainloop()
def pesquisar():
    janelaselecao = tk.Tk()
    janelaselecao.title("Hotel Tiger")
    janelaselecao.geometry("1920x1280")
    janelaselecao.configure(background="#c8dbde")
    font=("Comic Sans MS",20)
    
    titulo = tk.Label(janelaselecao, text="Qual seria o tipo de pesquisa?", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    titulo.pack()
    
    printfunc = tk.Label(janelaselecao, text="Funcionários", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    printfunc.pack()

    frame = tk.Frame(janelaselecao, bg="#c8dbde")
    frame.pack(padx=30)

    botaoidfunc = tk.Button(frame, text="ID", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=idfunc)
    botaoidfunc.pack(side="left", padx=10, pady=10)
    botaonomefunc = tk.Button(frame, text="Nome", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=nomefunc)
    botaonomefunc.pack(side="left", padx=10, pady=10)
    botaocargofunc = tk.Button(frame, text="Cargo", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=cargofunc)
    botaocargofunc.pack(side="left", padx=10, pady=10)

    printclie = tk.Label(janelaselecao, text="Clientes", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    printclie.pack()

    framecliente= tk.Frame(janelaselecao, bg="#c8dbde")
    framecliente.pack(padx=20)

    botaoidcliente = tk.Button(framecliente, text="ID", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=idclientes)
    botaoidcliente.pack(side="left", padx=10, pady=10)
    botaonomecliente = tk.Button(framecliente, text="Nome", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=nomeclientes)
    botaonomecliente.pack(side="left", padx=10, pady=10)
    botaoquartocliente = tk.Button(framecliente, text="Quarto", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=quartoclientes)
    botaoquartocliente.pack(side="left", padx=10, pady=10)
    janelaselecao.mainloop()
    
def alteraremailfunc():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font =("Comic Sans MS",20)
    validacao = janelaquarto.register(validar)
    frameentrada = tk.Frame(janelaquarto, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada,text="Qual é o código e e-mail do funcionário?", font=("Comic Sans MS", 30,"bold"),background="#c8dbde")
    titulo.pack(pady=10)
    quartocod = tk.Label(frameentrada, text="Id Funcionário", font=font, background='#c8dbde')
    quartocod.pack(pady=10)
    funccod = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    funccod.pack()
    emailcod= tk.Label(frameentrada, text="E-Mail Funcionário", font=font, background='#c8dbde')
    emailcod.pack(pady=10)
    emailfunc = tk.Entry(frameentrada, font=font)
    emailfunc.pack()
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def emailantigofunc():
        idfunc = funccod.get()
        emailfuncio = emailfunc.get()

        
        campos_obrigatorios = [
            ("ID Func", idfunc),
            ("Email", emailfuncio),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            pegaremailantigo(idfunc, emailfuncio)


    def pegaremailantigo(idfunc, emailfuncio):
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        
        for widget in resultado_frame.winfo_children():
                widget.destroy()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mail Antigo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadoantigo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadoantigo.pack(pady=10)

            
            alteraremaildofuncionario(idfunc, emailfuncio)
        else:
            mensagem.config(text="Nenhum funcionário com esse ID!")


    def alteraremaildofuncionario(idfunc, emailfuncio):
        
        comandosql = f'UPDATE funcionarios SET email = "{emailfuncio}" WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        hotelbanco.commit()

        
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mail Novo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadonovo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadonovo.pack(pady=10)
            mensagem.config(text="Alterado!")

            

    
    frame = tk.Frame(janelaquarto, bg="#c8dbde")
    frame.pack(side="left", padx=40, pady=20, anchor="n")

    botaoalterar = tk.Button(frameentrada, text="Alterar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=emailantigofunc)
    botaoalterar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white",
    borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaquarto.destroy())
    botaovoltar.pack(side="top", padx=15, pady=10)
    
    resultado_frame = tk.Frame(janelaquarto, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)
    
    janelaquarto.mainloop()
def alterarcargahorariafunc():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font =("Comic Sans MS",20)
    validacao = janelaquarto.register(validar)
    frameentrada = tk.Frame(janelaquarto, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada,text="Qual é o código e e-mail do funcionário?", font=("Comic Sans MS", 30,"bold"),background="#c8dbde")
    titulo.pack(pady=10)
    quartocod = tk.Label(frameentrada, text="Id Funcionário", font=font, background='#c8dbde')
    quartocod.pack(pady=10)
    funccod = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    funccod.pack()
    emailcod= tk.Label(frameentrada, text="Carga Horária Funcionário", font=font, background='#c8dbde')
    emailcod.pack(pady=10)
    emailfunc = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    emailfunc.pack()
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def cargahorariaantigafunc():
        idfunc = funccod.get()
        emailfuncio = emailfunc.get()

        
        campos_obrigatorios = [
            ("ID Func", idfunc),
            ("Email", emailfuncio),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            pegarcargahorariaantigo(idfunc, emailfuncio)


    def pegarcargahorariaantigo(idfunc, emailfuncio):
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        
        for widget in resultado_frame.winfo_children():
                widget.destroy()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="Carga Horária Antiga", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadoantigo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadoantigo.pack(pady=10)

            
            alterarcargahdofuncionario(idfunc, emailfuncio)
        else:
            mensagem.config(text="Nenhum funcionário com esse ID!")


    def alterarcargahdofuncionario(idfunc, emailfuncio):
        
        comandosql = f'UPDATE funcionarios SET cargahoraria = {emailfuncio} WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        hotelbanco.commit()

        
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="Carga Horária Nova", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadonovo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadonovo.pack(pady=10)
            mensagem.config(text="Alterado!")

            

    
    frame = tk.Frame(janelaquarto, bg="#c8dbde")
    frame.pack(side="left", padx=40, pady=20, anchor="n")

    botaoalterar = tk.Button(frameentrada, text="Alterar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=cargahorariaantigafunc)
    botaoalterar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white",
    borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaquarto.destroy())
    botaovoltar.pack(side="top", padx=15, pady=10)
    
    resultado_frame = tk.Frame(janelaquarto, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)
    
    janelaquarto.mainloop()
def alterarcargofunc():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font =("Comic Sans MS",20)
    frameentrada = tk.Frame(janelaquarto, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada,text="Qual é o código e cargo do funcionário?", font=("Comic Sans MS", 30,"bold"),background="#c8dbde")
    titulo.pack(pady=10)
    quartocod = tk.Label(frameentrada, text="Id Funcionário", font=font, background='#c8dbde')
    quartocod.pack(pady=10)
    funccod = tk.Entry(frameentrada, font=font)
    funccod.pack()
    emailcod= tk.Label(frameentrada, text="Cargo Funcionário", font=font, background='#c8dbde')
    emailcod.pack(pady=10)
    emailfunc = tk.Entry(frameentrada, font=font)
    emailfunc.pack()
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def cargoantigofunc():
        idfunc = funccod.get()
        emailfuncio = emailfunc.get()

        
        campos_obrigatorios = [
            ("ID Func", idfunc),
            ("Email", emailfuncio),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            pegarcargoantigo(idfunc, emailfuncio)


    def pegarcargoantigo(idfunc, emailfuncio):
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        
        for widget in resultado_frame.winfo_children():
                widget.destroy()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mail Antigo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadoantigo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadoantigo.pack(pady=10)

            
            alterarcargodofuncionario(idfunc, emailfuncio)
        else:
            mensagem.config(text="Nenhum funcionário com esse ID!")


    def alterarcargodofuncionario(idfunc, emailfuncio):
        
        comandosql = f'UPDATE funcionarios SET cargo = "{emailfuncio}" WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        hotelbanco.commit()

        
        comandosql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mailçll Novo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadonovo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCARGO: {x[2]}\nCARGA HORÁRIA: {x[3]}\nTURNO: {x[4]}\nEMAIL: {x[5]}\nESTADO: {x[6]}\nCIDADE: {x[7]}\nTELEFONE: {x[8]}\nCPF: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadonovo.pack(pady=10)
            mensagem.config(text="Alterado!")

            

    
    frame = tk.Frame(janelaquarto, bg="#c8dbde")
    frame.pack(side="left", padx=40, pady=20, anchor="n")

    botaoalterar = tk.Button(frameentrada, text="Alterar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=cargoantigofunc)
    botaoalterar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white",
    borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaquarto.destroy())
    botaovoltar.pack(side="top", padx=15, pady=10)
    
    resultado_frame = tk.Frame(janelaquarto, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)
    
    janelaquarto.mainloop()

def alteraremailclientes():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font =("Comic Sans MS",20)
    validacao = janelaquarto.register(validar)
    frameentrada = tk.Frame(janelaquarto, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada,text="Qual é o código e e-mail do cliente?", font=("Comic Sans MS", 30,"bold"),background="#c8dbde")
    titulo.pack(pady=10)
    quartocod = tk.Label(frameentrada, text="Id Cliente", font=font, background='#c8dbde')
    quartocod.pack(pady=10)
    funccod = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    funccod.pack()
    emailcod= tk.Label(frameentrada, text="E-mail Cliente", font=font, background='#c8dbde')
    emailcod.pack(pady=10)
    emailfunc = tk.Entry(frameentrada, font=font)
    emailfunc.pack()
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def emailantigoclientes():
        idfunc = funccod.get()
        emailfuncio = emailfunc.get()

        
        campos_obrigatorios = [
            ("ID Func", idfunc),
            ("Email", emailfuncio),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            pegaremailclientesantigo(idfunc, emailfuncio)


    def pegaremailclientesantigo(idfunc, emailfuncio):
        comandosql = f'SELECT * FROM cliente WHERE idcliente = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        
        for widget in resultado_frame.winfo_children():
                widget.destroy()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mail Antigo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadoantigo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCPF: {x[2]}\nDATA CHECK-IN: {x[3]}\nDATA CHECK-OUT: {x[4]}\nTELEFONE: {x[5]}\nE-MAIL: {x[6]}\nESTADO: {x[7]}\nCIDADE: {x[8]}\nCÓDIGO DO QUARTO: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadoantigo.pack(pady=10)

            
            alteraremaildocliente(idfunc, emailfuncio)
        else:
            mensagem.config(text="Nenhum funcionário com esse ID!")


    def alteraremaildocliente(idfunc, emailfuncio):
        
        comandosql = f'UPDATE cliente SET email = "{emailfuncio}" WHERE idcliente = {idfunc}'
        cursor.execute(comandosql)
        hotelbanco.commit()

        
        comandosql = f'SELECT * FROM cliente WHERE idcliente = {idfunc}'
        cursor.execute(comandosql)
        x = cursor.fetchone()

        if x:
            
            titulo_resultados = tk.Label(resultado_frame, text="E-mail Novo", font=("Comic Sans MS", 30, "bold"),
                                        bg="#bed1d4")
            titulo_resultados.pack(pady=10)

            resultadonovo = tk.Label(
                resultado_frame,
                text=f"ID: {x[0]}\nNOME: {x[1]}\nCPF: {x[2]}\nDATA CHECK-IN: {x[3]}\nDATA CHECK-OUT: {x[4]}\nTELEFONE: {x[5]}\nE-MAIL: {x[6]}\nESTADO: {x[7]}\nCIDADE: {x[8]}\nCÓDIGO DO QUARTO: {x[9]}",
                font=font,
                bg="#bed1d4"
            )
            resultadonovo.pack(pady=10)
            mensagem.config(text="Alterado!")

            

    
    frame = tk.Frame(janelaquarto, bg="#c8dbde")
    frame.pack(side="left", padx=40, pady=20, anchor="n")

    botaoalterar = tk.Button(frameentrada, text="Alterar", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=emailantigoclientes)
    botaoalterar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(frameentrada, text="Voltar", font=font, background='#bed1d4', fg="white",
    borderwidth=0, relief="flat", highlightthickness=0, command=lambda: janelaquarto.destroy())
    botaovoltar.pack(side="top", padx=15, pady=10)
    
    resultado_frame = tk.Frame(janelaquarto, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)
    
    janelaquarto.mainloop()
def alterarquartoclientes():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font = ("Comic Sans MS", 20)
    validacao = janelaquarto.register(validar)
    titulo = tk.Label(
        janelaquarto, 
        text="Qual é o código e quarto do cliente?", 
        font=("Comic Sans MS", 30, "bold"),
        background="#c8dbde"
    )
    titulo.pack(pady=10)
    idprint = tk.Label(janelaquarto, text="Id Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    clientecod = tk.Entry(janelaquarto, font=font, validate="key", validatecommand=(validacao, "%P"))
    clientecod.pack()
    printtexto = tk.Label(janelaquarto, text="Quarto Cliente", font=font, background='#c8dbde')
    printtexto.pack(pady=10)
    quartocod = tk.Entry(janelaquarto, font=font, validate="key", validatecommand=(validacao, "%P"))
    quartocod.pack()
    mensagem = tk.Label(janelaquarto, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def alterarquartochecar():
        idclientis = clientecod.get()
        quartocliente = quartocod.get()
        
        campos_obrigatorios = [
            ("ID Cliente", idclientis),
            ("Número Quarto", quartocliente)
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]

        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitquarto(idclientis, quartocliente)

    def commitquarto(idclientis, quartocliente):
        comando_pesquisa = f'SELECT codquarto FROM cliente WHERE idcliente = {idclientis}'
        cursor.execute(comando_pesquisa)
        cliente_atual = cursor.fetchone()
        if not cliente_atual:
            mensagem.config(text="Cliente não encontrado!")
            return
        quarto_atual = cliente_atual[0]
        comandocheck = f'SELECT * FROM quarto WHERE numquarto = {quartocliente} AND estado = "Ocupado"'
        cursor.execute(comandocheck)
        novo_quarto_ocupado = cursor.fetchone()
        if novo_quarto_ocupado:
            mensagem.config(text="Quarto já ocupado!")
        else:
            if quarto_atual:
                comandolimpeza = f'UPDATE quarto SET estado = "Limpeza" WHERE numquarto = {quarto_atual}'
                cursor.execute(comandolimpeza)
            comandoocupar = f'UPDATE quarto SET estado = "Ocupado" WHERE numquarto = {quartocliente}'
            cursor.execute(comandoocupar)
            sqlcomando = f'UPDATE cliente SET codquarto = {quartocliente} WHERE idcliente = {idclientis}'
            cursor.execute(sqlcomando)
            hotelbanco.commit()
            mensagem.config(text="Alterado com sucesso!")
    botaoalterar = tk.Button(
            janelaquarto, 
            text="Alterar", 
            font=font, 
            background='#bed1d4', 
            fg="white", 
            borderwidth=0, 
            relief="flat", 
            highlightthickness=0, 
            command=alterarquartochecar
    )
    botaoalterar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(
            janelaquarto, 
            text="Voltar", 
            font=font, 
            background='#bed1d4', 
            fg="white",
            borderwidth=0, 
            relief="flat", 
            highlightthickness=0, 
            command=lambda: janelaquarto.destroy()
        )
    botaovoltar.pack(side="top", padx=15, pady=10)
    janelaquarto.mainloop()
def alterardatacheck():
    janeladata = tk.Tk()
    janeladata.title("Hotel Tiger")
    janeladata.geometry("1920x1280")
    janeladata.configure(background="#c8dbde")
    font = ("Comic Sans MS", 20)
    def validar_data(texto):
        if len(texto) > 10:
            return False  # Limita o número de caracteres a 10
        for char in texto:
            if char not in "0123456789/":  
                return False  # Permite apenas números e '/'
        return True

    def validar_numero(texto):
        return texto.isdigit() or texto == ""

    validacao_data = janeladata.register(validar_data)
    validacao_numero = janeladata.register(validar_numero)

    titulo = tk.Label(
        janeladata, 
        text="Alteração de data", 
        font=("Comic Sans MS", 30, "bold"),
        background="#c8dbde"
    )
    titulo.pack()
    idprint = tk.Label(janeladata, text="Id Cliente", font=font, background='#c8dbde')
    idprint.pack(pady=10)
    clientecod = tk.Entry(janeladata, font=font,  validate="key", 
    validatecommand=(validacao_numero, "%P") )
    clientecod.pack()
    printtexto = tk.Label(janeladata, text="Data Check-In Cliente", font=font, background='#c8dbde')
    printtexto.pack(pady=10)
    datacheckincod = tk.Entry(janeladata, font=font, validate="key", validatecommand=(validacao_data, "%P"))
    datacheckincod.pack()
    printtextob = tk.Label(janeladata, text="Data Check-Out Cliente", font=font, background='#c8dbde')
    printtextob.pack(pady=10)
    datacheckoutcod = tk.Entry(janeladata, font=font,validate="key", validatecommand=(validacao_data, "%P"))
    datacheckoutcod.pack()
    def datacheckincheck():
        idclients = clientecod.get()
        datain = datacheckincod.get()
        campos_obrigatorios = [
            ("ID Cliente", idclients),
            ("Data in", datain)
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitdatain(idclients, datain)
    def commitdatain(idclients, datain):
        comandosql = f'SELECT * from cliente where idcliente= {idclients}'
        cursor.execute(comandosql)
        x = cursor.fetchone()
        if x:
            sqlcomando = f'UPDATE cliente SET datacheckin= "{datain}" WHERE idcliente = {idclients}'
            cursor.execute(sqlcomando)
            hotelbanco.commit()
            mensagem.config(text="Alterado com sucesso!")
        else:
            mensagem.config(text="Cliente Inexistente")
    def datacheckoutcheck():
        idclients = clientecod.get()
        dataout = datacheckoutcod.get()
        campos_obrigatorios = [
            ("ID Cliente", idclients),
            ("Data in", dataout)
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitdataout(idclients, dataout)
    def commitdataout(idclients, dataout):
        comandosql = f'SELECT * from cliente where idcliente= {idclients}'
        cursor.execute(comandosql)
        x = cursor.fetchone()
        if x:
            sqlcomando = f'UPDATE cliente SET datacheckout= "{dataout}" WHERE idcliente = {idclients}'
            cursor.execute(sqlcomando)
            hotelbanco.commit()
            mensagem.config(text="Alterado com sucesso!")
        else:
            mensagem.config(text="Cliente Inexistente")
    def amboscheck():
        idclients = clientecod.get()
        datain = datacheckincod.get()
        dataout = datacheckoutcod.get()
        campos_obrigatorios = [
            ("ID Cliente", idclients),
            ("Data In", datain),
            ("Data Out",dataout)
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
    
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitdataambos(idclients, datain, dataout)
    def commitdataambos(idclients, datain, dataout):
        comandosql = f'SELECT * from cliente where idcliente= {idclients}'
        cursor.execute(comandosql)
        x = cursor.fetchone()
        if x:
            sqlcomando = f'UPDATE cliente SET datacheckin= "{datain}" WHERE idcliente = {idclients}'
            cursor.execute(sqlcomando)
            hotelbanco.commit()
            sqlcommand = f'UPDATE cliente SET datacheckout= "{dataout}" WHERE idcliente = {idclients}'
            cursor.execute(sqlcommand)
            hotelbanco.commit()
            mensagem.config(text="Alterado com sucesso!")
        else:
            mensagem.config(text="Cliente Inexistente")
    botaoalterar = tk.Button(
            janeladata, 
            text="Alterar Check-In", 
            font=font, 
            background='#bed1d4', 
            fg="white", 
            borderwidth=0, 
            relief="flat", 
            highlightthickness=0,
            command = datacheckincheck
    )
    botaoalterar.pack(padx=15, pady=10)

    botaoalterarcheckout = tk.Button(
            janeladata, 
            text="Alterar Check-Out", 
            font=font, 
            background='#bed1d4', 
            fg="white",
            borderwidth=0, 
            relief="flat", 
            highlightthickness=0,
            command = datacheckoutcheck
    )
    botaoalterarcheckout.pack(padx=15, pady=10)
    
    botaoalterarambos = tk.Button(
            janeladata, 
            text="Alterar Ambos", 
            font=font, 
            background='#bed1d4', 
            fg="white",
            borderwidth=0, 
            relief="flat", 
            highlightthickness=0,
            command = amboscheck
    )
    botaoalterarambos.pack(padx=15, pady=10)
    botaovoltar = tk.Button(
        janeladata, 
        text="Voltar", 
        font=font, 
        background='#bed1d4', 
        fg="white",
        borderwidth=0, 
        relief="flat", 
        highlightthickness=0,
        command=lambda: janeladata.destroy()
    )
    botaovoltar.pack(padx=15, pady=10)
    mensagem = tk.Label(janeladata, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    janeladata.mainloop()
def alterarestadoquarto():
    janelaquarto = tk.Tk()
    janelaquarto.title("Hotel Tiger")
    janelaquarto.geometry("1920x1280")
    janelaquarto.configure(background="#c8dbde")
    font =("Comic Sans MS",20)
    validacao = janelaquarto.register(validar)
    frameentrada = tk.Frame(janelaquarto, bg="#c8dbde")
    frameentrada.pack(side="left", padx=40, pady=20, anchor="n")
    titulo = tk.Label(frameentrada,text="Qual é o código do quarto?", font=("Comic Sans MS", 30,"bold"),background="#c8dbde")
    titulo.pack(pady=10)
    quartocod = tk.Label(frameentrada, text="Código Quarto", font=font, background='#c8dbde')
    quartocod.pack(pady=10)
    codigo = tk.Entry(frameentrada, font=font, validate="key", validatecommand=(validacao, "%P"))
    codigo.pack()
    mensagem = tk.Label(frameentrada, text="", font=font, background="#c8dbde", fg="blue")
    mensagem.pack(pady=10)
    def liberarquarto():
        cod = codigo.get()
        campos_obrigatorios = [
            ("ID Cliente", cod),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitestadoliberar(cod)
    def commitestadoliberar(cod):
        comando_pesquisa = f'SELECT estado FROM quarto WHERE numquarto = {cod}'
        cursor.execute(comando_pesquisa)
        resultado = cursor.fetchone()
        if resultado: 
            estado = resultado[0]
            if estado == "Ocupado":  
                mensagem.config(text="O quarto está ocupado!")
            else:
                y = "Livre"
                comando_alterar = f'UPDATE quarto SET estado = "{y}" WHERE numquarto = {cod}'
                cursor.execute(comando_alterar)
                hotelbanco.commit()
                mensagem.config(text="Alteração realizada com sucesso!")
        else:
            mensagem.config(text="Esse código de quarto não existe!")
    def ocuparquarto():
        cod = codigo.get()
        campos_obrigatorios = [
            ("ID Cliente", cod),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitestadoocupar(cod)
    def commitestadoocupar(cod):
        comando_pesquisa = f'SELECT estado FROM quarto WHERE numquarto = {cod}'
        cursor.execute(comando_pesquisa)
        resultado = cursor.fetchone()
        if resultado: 
            estado = resultado[0]
            if estado == "Livre":  
                mensagem.config(text="Apenas quartos que estão para limpar podem ser alterados!")
            else:
                y = "Ocupado"
                comando_alterar = f'UPDATE quarto SET estado = "{y}" WHERE numquarto = {cod}'
                cursor.execute(comando_alterar)
                hotelbanco.commit()
                mensagem.config(text="Alteração realizada com sucesso!")
        else:
            mensagem.config(text="Esse código de quarto não existe!")
    def limparquarto():
        cod = codigo.get()
        campos_obrigatorios = [
            ("ID Cliente", cod),
        ]
        erros = [campo for campo, valor in campos_obrigatorios if not valor]
        if erros:
            mensagem.config(text="Falta informações!")
        else:
            commitestadolimpar(cod)
    def commitestadolimpar(cod):
        comando_pesquisa = f'SELECT estado FROM quarto WHERE numquarto = {cod}'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchone()
        if x:
            y = "Limpeza"
            comando_alterar = f'UPDATE quarto SET estado = "{y}" WHERE numquarto = {cod}'
            cursor.execute(comando_alterar)
            hotelbanco.commit()
            mensagem.config(text="Alteração realizada com sucesso!")
        else:
            mensagem.config(text="Esse código de quarto não existe!")
    def atualizarbanco():
        comandosql = 'SELECT * from quarto'
        cursor.execute(comandosql)
        x = cursor.fetchall()
        for widget in resultado_frame.winfo_children():
            if widget != titulo_resultados:
                widget.destroy()
        for i in x:
            resultado = tk.Label(resultado_frame,text=f"NÚMERO QUARTO:{i[0]}  ANDAR:{i[1]}  ESTADO:{i[2]}",font=font, bg="#bed1d4")
            resultado.pack(side="top")
    
    frame = tk.Frame(janelaquarto, bg="#c8dbde")
    frame.pack(side="left", padx=40, pady=20, anchor="n")

    botaolivre = tk.Button(frameentrada, text="Abrir Quarto", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=liberarquarto)
    botaolivre.pack(side="top", padx=15, pady=10)
    botaoocupado = tk.Button(frameentrada, text="Ocupar Quarto", font=font, background='#bed1d4', fg="white",
    borderwidth=0, relief="flat", highlightthickness=0, command=ocuparquarto)
    botaoocupado.pack(side="top", padx=15, pady=10)
    botaolimpar = tk.Button(frameentrada, text="Limpar Quarto", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=limparquarto)
    botaolimpar.pack(side="top", padx=15, pady=10)
    botaoatualizar = tk.Button(frameentrada, text="Atualizar Tabela", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=atualizarbanco)
    botaoatualizar.pack(side="top", padx=15, pady=10)
    botaovoltar = tk.Button(
        frameentrada, 
        text="Alterar Ambos", 
        font=font, 
        background='#bed1d4', 
        fg="white",
        borderwidth=0, 
        relief="flat", 
        highlightthickness=0,
        command=lambda: janelaquarto.destroy()
    )
    botaovoltar.pack(padx=15, pady=10)
    
    resultado_frame = tk.Frame(janelaquarto, bg="#bed1d4", bd=2, relief="solid", padx=20, pady=20)
    resultado_frame.pack(side="right", padx=40, pady=20, fill="both", expand=True)

    titulo_resultados = tk.Label(resultado_frame, text="Lista de Quartos", font=("Comic Sans MS", 30, "bold"), bg="#bed1d4")
    titulo_resultados.pack(pady=10)
    atualizarbanco()
    janelaquarto.mainloop()

def alterar():
    janelaselecao = tk.Tk()
    janelaselecao.title("Hotel Tiger")
    janelaselecao.geometry("1920x1280")
    janelaselecao.configure(background="#c8dbde")
    font=("Comic Sans MS",20)
    
    titulo = tk.Label(janelaselecao, text="Qual seria o tipo de alteração?", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    titulo.pack()
    
    printfunc = tk.Label(janelaselecao, text="Funcionários", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    printfunc.pack()

    frame = tk.Frame(janelaselecao, bg="#c8dbde")
    frame.pack(padx=30)
    botaoemailfunc = tk.Button(frame, text="E-Mail", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alteraremailfunc)
    botaoemailfunc.pack(side="left", padx=10, pady=10)
    botaonomefunc = tk.Button(frame, text="Cargo", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alterarcargofunc)
    botaonomefunc.pack(side="left", padx=10, pady=10)
    botaocargofunc = tk.Button(frame, text="Carga Horária", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alterarcargahorariafunc)
    botaocargofunc.pack(side="left", padx=10, pady=10)

    printclie = tk.Label(janelaselecao, text="Clientes", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    printclie.pack()

    framecliente= tk.Frame(janelaselecao, bg="#c8dbde")
    framecliente.pack(padx=20)

    botaonomecliente = tk.Button(framecliente, text="E-Mail", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alteraremailclientes)
    botaonomecliente.pack(side="left", padx=10, pady=10)
    botaoquartocliente = tk.Button(framecliente, text="Quarto", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alterarquartoclientes)
    botaoquartocliente.pack(side="left", padx=10, pady=10)
    botaodatacheckcliente = tk.Button(framecliente, text="Data-Check", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alterardatacheck)
    botaodatacheckcliente.pack(side="left", padx=10, pady=10)

    printquarto = tk.Label(janelaselecao, text="Quarto", font=("Comic Sans MS",30,"bold"),background="#c8dbde")
    printquarto.pack()

    framequarto = tk.Frame(janelaselecao,bg="#c8dbde")
    framequarto.pack(padx=20)

    botaoestadoquarto = tk.Button(framequarto, text="Estado do Quarto", font=font, background='#bed1d4', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=alterarestadoquarto)
    botaoestadoquarto.pack(padx=10, pady=10)

    janelaselecao.mainloop()

def principal():
    janela = tk.Tk()
    janela.title("Hotel Tiger")
    janela.geometry("1920x1280")
    janela.configure(background='#FFDAB9')

    #imagem = Image.open("fundotiger.png")  
    #imagem_tk = ImageTk.PhotoImage(imagem)

    #labeldaimagem = tk.Label(janela, image=imagem_tk,highlightthickness=0,borderwidth=0)
    #labeldaimagem.pack()

    frame = tk.Frame(janela, bg="#FFDAB9")
    frame.pack(expand=True)

    botaocadastrar = tk.Button(frame, text="Cadastrar",font=("Comic Sans MS", 20), background='#f7c497', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=selecao,width=12,height=2)
    botaocadastrar.pack(side="left", padx=10, pady=10)

    botaoalterar = tk.Button(frame, text="Alterar", font=("Comic Sans MS",20),background='#f7c497', fg="white", borderwidth=0, relief="flat", highlightthickness=0,width=12,height=2,command=alterar)
    botaoalterar.pack(side="left", padx=10, pady=10)

    botaopesquisa = tk.Button(frame, text="Pesquisa", font=("Comic Sans MS",  20),background='#f7c497', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=pesquisar,width=12,height=2)
    botaopesquisa.pack(side="left", padx=10, pady=10)

    botaodeletar = tk.Button(frame, text="Deletar", font=("Comic Sans MS",  20), background='#f7c497', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=deleteselect,width=12,height=2)
    botaodeletar.pack(side="left", padx=10, pady=10)
    def sair():
        janela.destroy()
    botaosair = tk.Button(frame, text="Sair", font=("Comic Sans MS",  20), background='#f7c497', fg="white", borderwidth=0, relief="flat", highlightthickness=0, command=sair,width=12,height=2)
    botaosair.pack(side="left", padx=10, pady=10)

    janela.mainloop()
principal()
      