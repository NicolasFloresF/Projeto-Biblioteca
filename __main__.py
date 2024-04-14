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


# Limpa a tela
def limpar():
    print("\033c", end="")


# Função para percorrer arquivo JSON e retornar seu conteúdo em uma variavel a ser operada
def carregar_usuarios(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
        dados = json.load(arquivo)
    return dados


# Verificação de credencias de login
def login(dados, quantUsuarios):
    print("---LOGIN---")
    usuario = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")
    for i in range(quantUsuarios):
        if (
            usuario == dados["usuarios"][i]["nome"]
            and senha == dados["usuarios"][i]["senha"]
        ):
            print(f"SEJA BEM VINDO {usuario}")
            return usuario, dados["usuarios"][i]["admin"]
    print("Nome ou senha incorreto, por favor tente novamente")
    return "0", "0"


# Persiste os dados nos arquivos json
def guardarDados(nomeArquivo, dadosUsuario):
    # persistir também os dados dos livros
    with open(nomeArquivo, "w") as arquivo:
        json.dump(dadosUsuario, arquivo, indent=4)
    limpar()
    print("Usuarios Atualizados")


# -----------CRUDS USUARIO-----------


# Insere o novo usuario na variavel dados
def cadastrarUsuario(dados):
    id = dados["usuarios"][-1]["id"] + 1
    usuario = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")
    admin = "nao"
    livros_emprestimo = []
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
def consultarUsuarios(dados):
    usuarios = dados["usuarios"]

    print(tabulate(usuarios, headers="keys", tablefmt="github"))
    input("Tecle Enter para sair .: ")
    limpar()


# Seleciona o usuário através do nome e permite a edição dos seus dados
def editarUsuarios(dados):
    usuario = input("Digite o usuario a ser alterado.: ")
    flag = 0
    for i in range(len(dados["usuarios"])):
        if usuario == dados["usuarios"][i]["nome"]:
            flag = 1
            print("Nome\nSenha\nAdmin")
            campoAlterado = input("Digite o campo que deseja alterar.: ")
            if campoAlterado == "Nome":
                nome = input("Digite o novo nome.: ")
                dados["usuarios"][i]["nome"] = nome
                limpar()
                print("Nome alterado com sucesso")
            elif campoAlterado == "Senha":
                senha = input("Digite a nova senha.: ")
                dados["usuarios"][i]["senha"] = senha
                limpar()
                print("Senha alterada com sucesso")
            elif campoAlterado == "Admin":
                admin = input("Digite sim ou nao para o campo admin.: ")
                dados["usuarios"][i]["admin"] = admin
                if admin == "sim":
                    limpar()
                    print(f"{usuario} agora é admin")
                elif admin == "nao":
                    limpar()
                    print(f"Acesso admin retirado de {usuario}")
    if flag == 0:
        limpar()
        print("Usuario nao encontrado")
    return dados


# Exclui o usuário a partir do seu nome
def excluirUsuario(dados):
    usuario = input("Digite o usuario a ser excluido.: ")
    flag = 0
    for i in range(len(dados["usuarios"])):
        if usuario == dados["usuarios"][i]["nome"]:
            flag = 1
            print(f"Deseja mesmo excluir {usuario}?")
            print("Sim\nNao")
            confirmacao = input(".: ")
            if confirmacao == "Sim":
                del dados["usuarios"][i]
                limpar()
                print("Usuario excluido com sucesso")
            elif confirmacao == "Nao":
                limpar()
                print("Operação abortada")
    if flag == 0:
        limpar()
        print("Usuario não encontrado")
    return dados


# -----------CRUDS LIVROS-----------


def cadastrarLivro(dados):
    id = dados["livros"][-1]["id"] + 1
    titulo = input("Insira o titulo do livro: ")
    autor = input("Insira o autor do livro: ")
    ano = input("Insira o ano do livro: ")
    idioma = input("Insira o idioma do livro: ")
    paginas = input("Insira quantidade de paginas do livro: ")
    editora = input("Insira a editora do livro: ")
    # criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados"
    novoLivro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "idioma": idioma,
        "paginas": paginas,
        "editora": editora,
    }
    dados["livros"].append(novoLivro)
    limpar()
    print("Cadastro realizado com sucesso")

    return dados


def consultarLivro(dados, waitInp=TRUE):
    livros = dados["livros"]

    print(tabulate(livros, headers="keys", tablefmt="github"))
    if waitInp:
        input("Tecle Enter para sair .: ")
        limpar()


def editarLivro(dados):
    livros = dados["livros"]
    consultarLivro(dados, FALSE)
    flag = FALSE

    livroId = input("Digite o id do livro a ser alterado.: ")
    limpar()

    for livro in livros:
        if livro["id"] == int(livroId):
            flag = TRUE

    if flag:
        ...
    else:
        print("Livro não encontrado!")
        input("Tecle Enter para sair .: ")
        limpar()


def excluirLivro():
    print("ok")


def solicitarLivro():
    print("ok")


def devolverLivro():
    print("ok")


# -----------BIBLIOTECA-----------


# Função principal contendo todos os CRUDS de livros e usuario
def biblioteca(dados, admin):
    while True:
        print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
        if admin == "nao":
            comando = input("1 - Solicitar livro\n2 - Devolver livro\n3 - Sair\n")
            if comando == "1":
                solicitarLivro()
            elif comando == "2":
                devolverLivro()
            elif comando == "3":
                guardarDados("dados.json", dados)
                break
        if admin == "sim":
            print("---BEM VINDO ADMIN---")
            print(
                "1 - Cadastrar Livro\n2 - Consultar livros\n3 - Editar Livros\n4 - Excluir Livro"
            )
            print(
                "5 - Cadastrar usuário\n6 - Consultar usuarios\n7 - Editar Usuario\n8 - Excluir usuário\n9 - Salvar e sair"
            )
            comando = input(".: ")
            if comando == "1":
                dados = cadastrarLivro(dados)
            elif comando == "2":
                consultarLivro(dados)
            elif comando == "3":
                dados = editarLivro(dados)
            elif comando == "4":
                dados = excluirLivro(dados)
            elif comando == "5":
                dados = cadastrarUsuario(dados)
            elif comando == "6":
                consultarUsuarios(dados)
            elif comando == "7":
                dados = editarUsuarios(dados)
            elif comando == "8":
                dados = excluirUsuario(dados)
            elif comando == "9":
                guardarDados("dados.json", dados)
                break


def home(dados, quantUsuarios):
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


def tkLogin(user): ...


def janela_login():
    janela = Tk()
    janela.title("BIBLIOTECA 7000")
    Label(janela, text="Usuário").grid(row=0, column=0)
    Label(janela, text="Senha").grid(row=1, column=0)
    user = Entry(janela)
    user.grid(row=0, column=1)
    senha = Entry(janela)
    senha.grid(row=1, column=1)
    button = Button(
        janela, text="Login", width=25, command=lambda: tkLogin(user.get())
    ).grid(row=3, column=1)
    janela.mainloop()


def main():
    dados = carregar_usuarios("dados.json")

    quantUsuarios = len(dados["usuarios"])
    print("------SEJA BEM VINDO A BIBLIOTECA 7000------")
    print(f"-TEMOS {quantUsuarios} USUARIOS CADASTRADOS-")
    home(dados, quantUsuarios)


if __name__ == "__main__":
    main()
