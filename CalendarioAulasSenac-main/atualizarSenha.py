import conexao
import this
import cadastrarProfessor

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()



def atualizarSenha(email, senha):
    cadastrarProfessor
    # Coletando a digitação do usuário
    print('Informe o email: ')
    email = input()
    print('Informe a nova senha: ')
    senha = input()


    try:
        sql = "update Professor set senha = '{}' where email = '{}'".format(senha, email)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)