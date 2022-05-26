import conexao
import cadastrarProfessor

db_connection = conexao.conectar()
con = db_connection.cursor()

def selecionar():
    cadastrarProfessor
    try:
        sql = "select * from Professor"
        con.execute(sql)

        for (email, senha, nome) in con:
            print('\n')
            print(email, senha, nome)
        print('\n')
    except Exception as erro:
        print(erro)