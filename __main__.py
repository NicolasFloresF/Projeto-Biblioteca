"""
Construção de sistema para automatizar
o gerenciamento de uma biblioteca
● Gerenciamento de usuários (CRUD).
● Gerenciamento de livros (CRUD).
● Registro de empréstimos e devoluções.
"""

# Estaremos trabalhando com JSON ao longo do trabalho 1
import json
from tkinter import *
from tabulate import tabulate
from getpass import getpass


# Limpa a tela
def limpar():
    print("\033c", end="")


# Função para percorrer arquivo JSON e retornar seu conteúdo em uma variavel a ser operada
def carregar_usuarios(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
        dados = json.load(arquivo)
    return dados


# Persiste os dados nos arquivos json
def guardarDados(nomeArquivo, dadosUsuario):
    # persistir também os dados dos livros
    with open(nomeArquivo, "w") as arquivo:
        json.dump(dadosUsuario, arquivo, indent=4)
    limpar()


# -----------CRUDS USUARIO-----------


# Insere o novo usuario na variavel dados
def cadastrarUsuario(dados):
    id = dados["usuarios"][-1]["id"] + 1
    usuario = input("Insira seu nome: ")
    while TRUE:
        senha = getpass("Insira sua senha: ")
        confirma = getpass("Confirme sua senha: ")
        if(senha == ''):
            limpar()
            print("Senha não pode ser vazia, tente novamente")
        elif(senha != confirma):
            limpar()
            print("Senhas não coincidem, tente novamente")
        else:
            break

    # criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados"
    novoUsuario = {
        "id": id,
        "nome": usuario,
        "senha": senha,
        "admin": "nao",
        "livros_emprestimos": [],
    }
    dados["usuarios"].append(novoUsuario)
    limpar()
    print("Cadastro realizado com sucesso")

    return dados


# Retorna a lista de todos os usuários cadastrados e seus livros emprestados
def consultarUsuarios(dados, waitInp=TRUE):
    usuarios = dados["usuarios"]

    print(tabulate(usuarios, headers="keys", tablefmt="github"))
    if waitInp:
        input("Tecle Enter para sair.: ")
        limpar()


# Seleciona o usuário através do nome e permite a edição dos seus dados
def editarUsuarios(dados):
    usuarios = dados["usuarios"]
    flag = FALSE

    while TRUE:
        consultarUsuarios(dados, FALSE)
        usuarioId = input(
            "Digite o id do usuario a ser alterado ou pressione enter para sair.: "
        )

        if usuarioId == "":
            break
        limpar()

        for usuario in usuarios:
            if str(usuario["id"]) == usuarioId:
                flag = TRUE
                break

        if flag:
            while TRUE:
                print(
                    f"1 - nome: {usuario['nome']}\n2 - senha: {usuario['senha']}\n3 - admin: {usuario['admin']}\n4 - voltar"
                )
                comando = input("Digite o que deseja alterar.: ")
                if comando == "1":
                    usuario["nome"] = input("Digite o novo nome.: ")
                    limpar()
                elif comando == "2":
                    usuario["senha"] = input("Digite a nova senha.: ")
                    limpar()
                elif comando == "3":
                    if usuario["admin"] == "sim":
                        usuario["admin"] = "nao"
                        limpar()
                        print(f"{usuario['nome']} deixou de ser administrador!")
                    else:
                        usuario["admin"] = "sim"
                        limpar()
                        print(f"{usuario['nome']} virou administrador!")
                elif comando == "4":
                    limpar()
                    break
        else:
            print("Não existe um usuario com este id")

    return dados


# Exclui o usuário a partir do seu nome
def excluirUsuario(dados):
    usuarios = dados["usuarios"]
    flag = FALSE

    while TRUE:
        consultarUsuarios(dados, FALSE)
        usuarioId = input(
            "Digite o id do usuario a ser excluido ou pressione enter para sair.: "
        )

        if usuarioId == "":
            break

        for i in range(len(usuarios)):
            if str(usuarios[i]["id"]) == usuarioId:
                flag = TRUE
                break

        if flag:
            while TRUE:
                confirmacao = input(
                    f"Deseja mesmo excluir {usuarios[i]['titulo']}? [Sim/Nao].: "
                )
                if confirmacao == "Sim":
                    del usuarios[i]
                    limpar()
                    print("usuario excluido com sucesso")
                    break
                elif confirmacao == "Nao":
                    limpar()
                    print("Operação abortada")
                    break
                limpar()
        else:
            limpar()
            print("Não existe um usuario com este id")


# -----------CRUDS LIVROS-----------


def cadastrarLivro(dados):
    id = dados["livros"][-1]["id"] + 1
    titulo = input("Insira o titulo do livro.: ")
    autor = input("Insira o autor do livro.: ")
    ano = input("Insira o ano do livro.: ")
    idioma = input("Insira o idioma do livro.: ")
    paginas = input("Insira quantidade de paginas do livro.: ")
    editora = input("Insira a editora do livro.: ")
    # criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados"
    novoLivro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "idioma": idioma,
        "paginas": paginas,
        "editora": editora,
        "locado": False
    }
    dados["livros"].append(novoLivro)
    limpar()
    print("Cadastro realizado com sucesso")

    return dados


def consultarLivro(dados, waitInp=TRUE):
    livros = dados["livros"]

    print(tabulate(livros, headers="keys", tablefmt="github"))
    if waitInp:
        input("Tecle Enter para sair.: ")
        limpar()


def editarLivro(dados):
    livros = dados["livros"]
    flag = FALSE

    while TRUE:
        consultarLivro(dados, FALSE)
        livroId = input(
            "Digite o id do livro a ser alterado ou pressione enter para sair.: "
        )

        if livroId == "":
            break
        limpar()

        for livro in livros:
            if str(livro["id"]) == livroId:
                flag = TRUE
                break

        if flag:
            while TRUE:
                print(
                    f"1 - titulo: {livro['titulo']}\n2 - autor: {livro['autor']}\n3 - ano: {livro['ano']}"
                )
                print(
                    f"4 - idioma: {livro['idioma']}\n5 - paginas {livro['paginas']}\n6 - editora: {livro['editora']}\n7 - Voltar"
                )
                comando = input("Digite o que deseja alterar.: ")
                if comando == "1":
                    livro["titulo"] = input("Digite o novo titulo.: ")
                elif comando == "2":
                    livro["autor"] = input("Digite o novo autor.: ")
                elif comando == "3":
                    livro["ano"] = input("Digite o novo ano.: ")
                elif comando == "4":
                    livro["idioma"] = input("Digite o novo idioma.: ")
                elif comando == "5":
                    livro["paginas"] = input("Digite o novo paginas.: ")
                elif comando == "6":
                    livro["editora"] = input("Digite o novo editora.: ")
                elif comando == "7":
                    limpar()
                    break
                limpar()
        else:
            print("Não existe um livro com este id")

    return dados


def excluirLivro(dados):
    livros = dados["livros"]
    flag = FALSE

    while TRUE:
        consultarLivro(dados, FALSE)
        livroId = input(
            "Digite o id do livro a ser excluido ou pressione enter para sair.: "
        )

        if livroId == "":
            break

        for i in range(len(livros)):
            if str(livros[i]["id"]) == livroId:
                flag = TRUE
                break

        if flag:
            while TRUE:
                confirmacao = input(
                    f"Deseja mesmo excluir {livros[i]['titulo']}? [Sim/Nao].: "
                )
                if confirmacao == "Sim":
                    del livros[i]
                    limpar()
                    print("Livro excluido com sucesso")
                    break
                elif confirmacao == "Nao":
                    limpar()
                    print("Operação abortada")
                    break
                limpar()
        else:
            limpar()
            print("Não existe um livro com este id")

    return dados


# varios livros?
# crud de registros
# disponibilidade de livros

# - (pode ser editado se estiver em empréstimo?) pode editar
# necessidade de listar os empréstimos de livros?
def solicitarLivro():
    ...


def devolverLivro():
    ...


def editaConta(dados, id):
    usuarios = dados["usuarios"]
    while TRUE:
        print(
            f"1 - nome: {usuarios[id]['nome']}\n2 - senha"
        )
        comando = input("Digite o que deseja alterar.: ")
        if comando == "1":
            usuarios[id]["nome"] = input("Digite o novo nome.: ")
        elif comando == "2":
            while TRUE:
                senha = getpass("Insira sua senha atual: ")
                if usuarios[id]["senha"] == senha:
                    usuarios[id]["senha"] = input("Digite a nova senha.: ")
                else:
                    limpar()
                    print("senha incorreta, tente novamente!")

    input("Tecle Enter para sair.: ")



def consultaLivros():
    ...


# -----------BIBLIOTECA-----------


# Função principal contendo todos os CRUDS de livros e usuario
def biblioteca(dados, admin, sessionId):
    while True:
        print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
        if admin == "nao":
            comando = input(
                "1 - Solicitar livro\n2 - Devolver livro\n3 - Editar conta\n4 - Meus livros\n5 - Sair\n"
            )
            if comando == "1":
                solicitarLivro()
            elif comando == "2":
                devolverLivro()
            elif comando == "3":
                editaConta(dados,sessionId)
            elif comando == "4":
                consultaLivros()
            elif comando == "4":
                guardarDados("dados.json", dados)
                break
        if admin == "sim":
            print(
                "Gerenciamento de livros: \n1 - Cadastrar Livro\n2 - Consultar livros\n3 - Editar Livros\n4 - Excluir Livro"
            )
            print(
                "\nGerenciamento de usuarios: \n5 - Cadastrar usuário\n6 - Consultar usuarios\n7 - Editar Usuario\n8 - Excluir usuário\n9 - Salvar e sair"
            )
            comando = input(".: ")
            if comando == "1":
                limpar()
                dados = cadastrarLivro(dados)
            elif comando == "2":
                limpar()
                consultarLivro(dados)
            elif comando == "3":
                limpar()
                dados = editarLivro(dados)
            elif comando == "4":
                limpar()
                dados = excluirLivro(dados)
            elif comando == "5":
                limpar()
                dados = cadastrarUsuario(dados)
            elif comando == "6":
                limpar()
                consultarUsuarios(dados)
            elif comando == "7":
                limpar()
                dados = editarUsuarios(dados)
            elif comando == "8":
                limpar()
                dados = excluirUsuario(dados)
            elif comando == "9":
                limpar()
                guardarDados("dados.json", dados)
                exit()
                # break
        limpar()


# Verificação de credencias de login
def login(dados):
    usuarios = dados["usuarios"]
    limpar()
    while TRUE:
        print("---LOGIN---")
        usuario = input("Insira seu nome: ")
        senha = getpass("Insira sua senha: ")
        for i in range(len(usuarios)):
            if usuario == usuarios[i]["nome"] and senha == usuarios[i]["senha"]:
                limpar()
                print(f"SEJA BEM VINDO {usuario}")
                biblioteca(dados, usuarios[i]["admin"], i)
                # return usuario, dados["usuarios"][i]["admin"]
        limpar()
        print("Nome ou senha incorreto, por favor tente novamente")
    # return "0", "0"


def home():
    dados = carregar_usuarios("dados.json")
    quantUsuarios = len(dados["usuarios"])

    while True:
        print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
        comando = input("1 - Logar\n2 - Cadastrar\n3 - Finalizar programa\n")
        if comando == "1":

            limpar()
            # Caso o login ocorra com sucesso retorna o usuario para utilizar nas operações futuras
            usuario = "0"
            while usuario == "0":
                usuario, admin = login(dados, quantUsuarios)
            limpar()
            # Envia as informações para a parte principal
            biblioteca(dados, admin)
        if comando == "2":
            limpar()
            # Armazena o novo usuario na variavel dados
            dados = cadastrarUsuario(dados)
            admin = "nao"
            limpar()
            # Envia as informações para a parte principal
            biblioteca(dados, admin)

        if comando == "3":
            print("Obrigado por utilizar nosso sistema.\nAtt: \n-EdCarvalho\n-NiFlores")
            break


def main():
    dados = carregar_usuarios("dados.json")
    login(dados)


if __name__ == "__main__":
    main()
