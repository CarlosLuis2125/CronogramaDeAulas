import this
import mysql.connector
import conexao


db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


this.email = ""
this.senha = ""
this.nome = ""
def inserir(email, senha, nome):
    try:
        sql = "insert into Professor(email, senha, nome) values('{}','{}','{}')".format(email, senha, nome)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
      print(erro)



def coletarDados():

    this.email = []
    this.senha = []
    this.nome = []



    print('Informe o e-mail do professor: ')
    this.email = input()

    print('informe a senha de login do(a) professor(a)')
    this.senha = input()

    print('Informe o nome do professor: ')
    this.nome = input()

    inserir(this.email, this.senha, this.nome)

def  mostrarDados():
    coletarDados()
    print(f'\n\n\n E-mail: {this.email}.\n Senha: {this.senha}.\n Nome: {this.nome} ')

    print('Cadastrado com sucesso!!')