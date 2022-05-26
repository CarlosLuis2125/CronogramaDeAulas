import this
import calendario
import cadastrarProfessor
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.email = ""
this.senha = ""


def loginProfessor():
    print("Informe o seu email: ")
    this.email = input()
    print("Informe a sua senha: ")
    this.senha = input()

    msg = "Acesso negado! Preencha os campos corretamente."

    try:
        sql = "select senha from Professor where email = '{}';".format(this.email)
        con.execute(sql)#Prepara o comando para ser executado

        for (senha) in con:
            print(senha[0])
            if this.senha == senha[0]:
                print("Acesso Liberado")
                calendario.coletar()

    except Exception as erro:
      print(erro)

    print(msg)
