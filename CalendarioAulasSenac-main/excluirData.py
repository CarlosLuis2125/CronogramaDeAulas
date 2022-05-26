import mysql.connector
import conexao
import this

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def excluir(codigo):
    print('Informe o código que deseja apagar: ')
    codigo = input()
    try:
        sql = "delete from calendario where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)

