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

        comando_cadastrar=f'INSERT INTO cliente(idcliente,nome,cpf,datacheckin,datacheckout,telefone,email,estado,cidade,codquarto) VALUES({id},"{nome}",{cpf},"{checkin}","{checkout}",{telefone},"{email}","{estado}","{cidade}",{codigoq})'
        x= "Ocupado"
        comando_troca= f'UPDATE quarto SET estado = "{x}" WHERE numquarto = {codigoq}'
        cursor.execute(comando_cadastrar)
        hotelbanco.commit()
        cursor.execute(comando_troca)
        hotelbanco.commit()
        

insert_cliente()