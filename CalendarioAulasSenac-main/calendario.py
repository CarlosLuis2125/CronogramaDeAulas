import this
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.data = ""
this.turno = ""
this.materia = ""
this.professor = ""
this.horario = ""

def meses():
    this.janeiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.fevereiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.marco = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.abril = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.maio = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.junho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.julho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.agosto = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.setembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.outubro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.novembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.dezembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def convertDate(texto):
    separate = texto.split('/')
    day = separate[0]
    month = separate[1]
    year = separate[2]
    return '{}-{}-{}'.format(year, month, day)


def coletar():
    print("Agendar Aula")
    print("Informe a data da aula: (dia/mês/ano)")
    this.data = input()

    print("Informe o turno: ")
    print("1. Manhã")
    print("2. Tarde")
    print("3. Noite")
    this.turno = input()

    print("Informe a matéria: ")
    this.materia = input()

    print("Informe o nome do professor: ")
    this.professor = input()

    codigo = (convertDate(this.data) + "(" + this.turno + ")")

    separado = this.data.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]



    inserir(codigo, dia, mes, ano, this.turno, this.materia, this.professor)


def inserir(codigo, dia, mes, ano, turno, materia, professor):
    try:
        sql = "insert into calendario(codigo, dia, mes, ano, turno, materia, professor) values('{}','{}','{}','{}','{}','{}','{}')".format(codigo, dia, mes, ano, turno, materia, professor)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()  # Executa o comando no banco de dados
        print("Aula agendada!")
    except Exception as erro:
      print(erro)


def consultar():
    print("Consultar aulas agendadas")

    print("Informe a data da aula: (dia/mês/ano)")
    this.data = input()

    print("Informe o turno: ")
    print("1. Manhã")
    print("2. Tarde")
    print("3. Noite")
    this.turno = int(input())

    cod = (convertDate(this.data) + "(" + str(this.turno) + ")")

    sql = "select * from calendario where codigo = '{}'".format(cod)
    con.execute(sql)  # Prepara o comando para ser executado

    msg = "Nenhuma aula Agendada!"

    for (codigo, dia, mes, ano , turno, materia, professor) in con:
        if this.turno == 1:
           this.horario = "Manhã"
        elif this.turno == 2:
           this.horario = "Tarde"
        elif this.turno == 3:
            this.horario = "Noite"
        else:
            print("Insira uma opção válida!")

        if cod == codigo:
            msg = "Data: " + str(dia) + "/" + str(mes) + "/" + str(ano) + "\nTurno: " + str(this.horario) + "\nMatéria: " + materia  + "\nProfessor: " + professor


    print(msg + "\n")

