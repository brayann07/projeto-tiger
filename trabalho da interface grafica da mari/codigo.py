import mysql.connector
hotelbanco = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database= "hoteltiger"
)
cursor = hotelbanco.cursor()
def insert_cliente():
    id = int(input("Qual o id do cliente:"))
    comando_pesquisa = f'SELECT * FROM cliente where idcliente= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        print("Já existe!")
    else:
        nome = input("Qual o nome:")
        cpf = int(input("Qual o cpf:"))
        checkin = input("Qual a data de check-in:")
        checkout = input("Qual a data de check-out:")
        telefone = int(input("Qual o telefone:"))
        email = input("Qual o email:")
        estado = input("Qual o estado:")
        cidade= input("Qual sua cidade:")
        codigoq = input("Qual o codigo do quarto:")
        comando_pesquisa = f'SELECT * FROM quarto where numquart= {codigoq} and quarto.estado like "%Ocupado%"'
        cursor.execute(comando_pesquisa)
        y =cursor.fetchone()
        if y >= 1:
            print("quarto ja ocupado")
        
        else:
            comando_cadastrar=f'INSERT INTO cliente(idcliente,nome,cpf,datacheckin,datacheckout,telefone,email,estado,cidade,codquarto) VALUES({id},"{nome}",{cpf},"{checkin}","{checkout}",{telefone},"{email}","{estado}","{cidade}",{codigoq})'
            x= "Ocupado"
            comando_troca= f'UPDATE quarto SET estado = "{x}" WHERE numquarto = {codigoq}'
            cursor.execute(comando_cadastrar)
            hotelbanco.commit()
            cursor.execute(comando_troca)
            hotelbanco.commit()
        
def insert_funiconario():
    id = int(input("Qual o id do funcionario:"))
    comando_pesquisa = f'SELECT * FROM funcionario where idfuncionario= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        print("Já existe!")
    else:
        nome = input("Qual o nome:")
        cargo = int(input("Qual o cargo:"))
        cargahoraria = input("Qual a carga horária:")
        turno = input("Qual a hora do turno")
        email = input("Qual o email:")
        estado = input("Qual o estado:")
        cidade= input("Qual sua cidade:")
        telefone = int(input("Qual o telefone:"))
        cpf = int(input("qual o cpf"))
        
        comando_cadastrar=f'INSERT INTO funcionario(idfuncionario,nome,cargo,cargahoraria,turno,telefone,email,estado,cidade,cpf) VALUES({id},"{nome}","{cargo}","{cargahoraria}","{turno}",{telefone},"{email}","{estado}","{cidade}",{cpf})'
        cursor.execute(comando_cadastrar)
        hotelbanco.commit()

def read_quarto():
    op = input("voce quer pesquisar o quarto por...\n1 - numero\n2 - andar\n3 - estado(ocupado/desocupado/limpando)")
    if op == "1":
        id = int(input("qual numero do quarto que voce quer pesquisar"))
        comando_pesquisa = f'SELECT * FROM quarto where numquarto = {id}'
        cursor.execute(comando_pesquisa)
        x =cursor.fetchall()
        for i in x:
            print(f'Número do quarto: {i[0]}\nAndar: {i[1]}\nEstado atual: {i[2]}\n')
        
    elif op == "2":
        andar = int(input("qual numero do andar que voce quer pesquisar"))
        comando_pesquisa = f'SELECT * FROM quarto where andar = {andar}'
        cursor.execute(comando_pesquisa)
        x =cursor.fetchall()
        for i in x:
            print(f'Número do quarto: {i[0]}\nAndar: {i[1]}\nEstado atual: {i[2]}\n')            

    elif op == "3":
        estado = int(input("qual numero do estado que voce quer pesquisar"))
        comando_pesquisa = f'SELECT * FROM quarto where estado = {estado}'
        cursor.execute(comando_pesquisa)
        x =cursor.fetchall()
        for i in x:
            print(f'Número do quarto: {i[0]}\nAndar: {i[1]}\nEstado atual: {i[2]}\n')    
    else:
        print("digite corretamente")

def read_cliente():
    op = int(input("Você quer pesquisar por...\n1 - nome\n2 - quarto"))
    if op == 1:
        nome = input("Qual o nome do cliente?")
        comando_pesquisa = f'SELECT * FROM cliente where nome like "%{nome}%"'
        cursor.execute(comando_pesquisa)
        x =cursor.fetchall()
        for i in x:
            print(f'\nID: {i[0]}\nNome: {i[1]}\nCPF: {i[2]}\nData de Checkin: {i[3]}\nData de Check-out: {i[4]}\nTelefone: {i[5]}\nE-mail: {i[6]}\nEstado: {i[7]}\nCidade: {i[8]}\nNúmero do quarto: {i[9]}\n')
    elif op == 2:
        quarto = int(input("Digite o número do quarto: "))
        comando_pesquisa = f'SELECT * FROM cliente where codquarto = {quarto}'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchall()
        for i in x:
            print(f'\nID: {i[0]}\nNome: {i[1]}\nCPF: {i[2]}\nData de Checkin: {i[3]}\nData de Check-out: {i[4]}\nTelefone: {i[5]}\nE-mail: {i[6]}\nEstado: {i[7]}\nCidade: {i[8]}\nNúmero do quarto: {i[9]}\n')

def read_funcionario():
    op = int(input("Você quer pesquisar por...\n1 - nome\n2 - cargo"))
    if op == 1:
        nome = input("qual o nome do funcionário?")
        comando_pesquisa = f'SELECT * FROM funcionarios where nome like "%{nome}%"'
        cursor.execute(comando_pesquisa)
        x =cursor.fetchall()
        for i in x:
            print(f'\nID: {i[0]}\nNome: {i[1]}\nCargo: {i[2]}\nCarga horária: {i[3]}\nTurno: {i[4]}\nE-mail: {i[5]}\nEstado: {i[6]}\nCidade: {i[7]}\nTelefone: {i[8]}\nCPF: {i[9]}\n')
    elif op == 2:
        cargo = int(input("Digite o cargo: "))
        comando_pesquisa = f'SELECT * FROM funcionarios where cargo like "%{cargo}%"'
        cursor.execute(comando_pesquisa)
        x = cursor.fetchall()
        for i in x:
            print(f'\nID: {i[0]}\nNome: {i[1]}\nCargo: {i[2]}\nCarga horária: {i[3]}\nTurno: {i[4]}\nE-mail: {i[5]}\nEstado: {i[6]}\nCidade: {i[7]}\nTelefone: {i[8]}\nCPF: {i[9]}\n')
def update_quarto():
    num = int(input("qual o número do quarto que voce quer alterar o estado"))
    comando_pesquisa = f'SELECT * FROM quarto where numquarto = {num}'
    cursor.execute(comando_pesquisa)
    x = cursor.fetchall()
    if x:
        op = input("você quer alterar o estado do quarto para...\n1 - livre\n2 - limpando")
        if op == "1":
            comando_update = f'UPDATE quarto set estado = "Livre" where numquarto = {num}'
            cursor.execute(comando_update)
            hotelbanco.commit()
        if op == "2":
            comando_update = f'UPDATE quarto set estado = "Limpando" where numquarto = {num}'
            cursor.execute(comando_update)
            hotelbanco.commit()
        else:
            print("erro")

def update_cliente():
    id = int(input("qual o id do cliente"))
    comando_pesquisa = f'SELECT * FROM cliente where idcliente= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        op = input("voce quer mudar...\n1 - o quarto\n2 - data de checkout dos clientes")
        if op == "1":
            num = int(input("qual o número do novo quarto do cliente"))
            comando_update = f'UPDATE cliente set codquarto = {num} where idcliente = {id};update quarto set estado = "Ocupado" where numquarto = {num}'
            cursor.execute(comando_update)
            hotelbanco.commit()
        if op == "2":
            data = input("Digite a nova data de checkout (yyyy/mm/dd):")
            comando_update = f"update cliente set datacheckout = {data} where idcliente = {id}"
            cursor.execute(comando_update)
            hotelbanco.commit()
        else:
            print("erro")

def update_funcionario():
    id = int(input("qual o id do funcionario"))
    comando_pesquisa = f'SELECT * FROM funcionario where idfuncionario= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        cargo = input("qual o novo cargo do funcionario")
        comando_update = f'update funcionarios set cargo = "{cargo}" where idfuncinoario = {id}'
        cursor.execute(comando_update)
        hotelbanco.commit()
    else:
        print("erro")

def delete_cliente():
    id = int(input("qual o id do funcionario"))
    comando_pesquisa = f'SELECT * FROM funcionario where idfuncionario= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        comando_delete = f'delete * from cliente where idcliente = {id}'
        cursor.execute(comando_delete)
        hotelbanco.commit()
    else:
        print("id nao encontrado")

def delete_funcionario():
    id = int(input("Qual o id do funcionario:"))
    comando_pesquisa = f'SELECT * FROM funcionario where idfuncionario= {id}'
    cursor.execute(comando_pesquisa)
    x =cursor.fetchone()
    if x:
        comando_delete = f'delete * from funciarios where idfuncionario = {id}'
        cursor.execute(comando_delete)
        hotelbanco.commit()
    else:
        print("id nao encontrado")

while True:
    op = input("Escolha uma das opções abaixo:\n1/C-Cadastrar\n2/P-Pesquisar\n3/A-Alterar\n4/D-Deletar\n5/S-Sair\n").upper()
    if op == "5" or op=="S":
        print("Fechando...")
    elif op=="1" or op=="C":
        opition = input("Escolha uma das opções abaixo:\n1/C-Cliente\n2/F-Funcionário\n").upper()
        if opition=="1" or opition=="C":
            insert_cliente()
        elif opition=="2" or opition=="F":
            insert_funiconario()
        else:
            print("digite uma opção válida")
    elif op=="2" or op=="P":
        opition = input("Escolha uma das opções abaixo:\n1/C-Cliente\n2/F-Funcionário\n3/Q-Quarto\n").upper()
        if opition == "1" or opition=="C":
            read_cliente()
        elif opition=="2" or opition=="F":
            read_funcionario()
        elif opition=="3" or opition=="Q":
            read_quarto()
        else:
            print("digite uma opção válida")
    elif op=="3" or op=="A":
        opition = input("Escolha uma das opções abaixo:\n1/C-Cliente\n2/F-Funcionário\n3/Q-Quarto\n").upper()
        if opition == "1" or opition=="C":
            update_cliente()
        elif opition=="2" or opition=="F":
            update_funcionario()
        elif opition=="3" or opition=="Q":
            update_quarto()
        else:
            print("digite uma opção válida")
    elif op=="4" or op=="E":
        opition = input("Escolha uma das opções abaixo:\n1/C-Cliente\n2/F-Funcionário\n").upper()
        if opition == "1" or opition=="C":
            delete_cliente()
        elif opition=="2" or opition=="F":
            delete_funcionario()
        else:
            print("digite uma opção válida")      
    else:
        print('Digite uma opção válida')