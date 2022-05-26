import conexao
import cadastrarProfessor






db_connection = conexao.conectar()
con = db_connection.cursor()



def novoNome(email, nome):
    cadastrarProfessor
    print('Informe o email do professor: ')
    email = input()
    print('Informe o novo nome do professor: ')
    nome = input()
    try:
        sql = "update Professor set nome = '{}' where email = '{}'".format(nome, email)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)