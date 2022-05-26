import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='cronogramaDeAulas')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as error: #Salvando o erro na variável error
        if error.errno == errorcode.ER_BAD_DB_ERROR: #Caso banco de dados não exista
            print('Banco de dados não existe!')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:#Caso haja um erro de usuário
            print('Email ou senha incorretos!')
        else:
            print(error)
    else:
        db_connection.close()