import atualizarSenha
import atuzalizarNome
import cadastrarProfessor
import consultarProfessor
import excluirData
import login
import this
import calendario

this.opcao = -2
this.codigo = 0


def mostrarMenu():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Cadastrar Professor' +
          '\n2. Calendário' +
          '\n3. Login' +
          '\n4. Consultar' +
          '\n5. Atualizar nome' +
          '\n6. Atualizar senha' +
          '\n7. Excluir data' +
          '\n8. Sair')

    this.opcao = int(input())

def operacoes():
    while this.opcao != 6:
        mostrarMenu()
        if this.opcao == 1:
            cadastrarProfessor.coletarDados()
        elif this.opcao == 2:
            calendario.consultar()
        elif this.opcao == 3:
            login.loginProfessor()
        elif this.opcao == 4:
            print(consultarProfessor.selecionar())
        elif this.opcao == 5:
            print(atuzalizarNome.novoNome(this.email, this.nome))
        elif this.opcao == 6:
            print(atualizarSenha.atualizarSenha(this.email, this.senha))
        elif this.opcao == 7:
            print(excluirData.excluir(this.codigo))
        else:
            print('Opção inválida! Tente novamente')
