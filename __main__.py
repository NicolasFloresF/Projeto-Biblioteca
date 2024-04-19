"""
Construção de sistema para automatizar
o gerenciamento de uma biblioteca
● Gerenciamento de usuários (CRUD).
● Gerenciamento de livros (CRUD).
● Registro de empréstimos e devoluções.
"""

# Estaremos trabalhando com JSON ao longo do trabalho 1
import json
import bcrypt
from getpass import getpass
from tabulate import tabulate


# Limpa a tela
def limpar():
    print("\033c", end="")


# Função para percorrer arquivo JSON e retornar seu conteúdo em uma variavel a ser operada
def carregar_usuarios(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
        dados = json.load(arquivo)
    return dados


# Persiste os dados nos arquivos json
def guardarDados(nomeArquivo):
    # persistir também os dados dos livros
    with open(nomeArquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    limpar()


# -----------CRUDS USUARIO-----------


# Insere o novo usuario na variavel dados
def cadastrarUsuario():
    id = dados["usuarios"][-1]["id"] + 1
    nome = input("Insira seu nome: ")
    email = input("Insira seu email: ")
    while True:
        senha = getpass("Insira sua senha: ")
        confirma = getpass("Confirme sua senha: ")
        if senha == "":
            limpar()
            print("Senha não pode ser vazia, tente novamente")
        elif senha != confirma:
            limpar()
            print("Senhas não coincidem, tente novamente")
        else:
            break

    senhaHashed = bcrypt.hashpw(senha.encode("utf8"), bcrypt.gensalt()).decode("utf-8")
    # criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados"
    novoUsuario = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senhaHashed,
        "admin": "nao",
        "livros_emprestimos": [],
    }
    dados["usuarios"].append(novoUsuario)
    limpar()
    print("Cadastro realizado com sucesso")

    return dados


# Retorna a lista de todos os usuários cadastrados e seus livros emprestados
def consultarUsuarios(waitInp=True):
    usuarios = dados["usuarios"]

    print(tabulate(usuarios, headers="keys", tablefmt="github"))
    if waitInp:
        input("Tecle Enter para sair.: ")
        limpar()


# Seleciona o usuário através do nome e permite a edição dos seus dados
def editarUsuarios():
    usuarios = dados["usuarios"]
    flag = False

    while True:
        consultarUsuarios(False)
        usuarioId = input(
            "Digite o id do usuario a ser alterado ou pressione enter para sair.: "
        )

        if usuarioId == "":
            break
        limpar()

        for usuario in usuarios:
            if str(usuario["id"]) == usuarioId:
                flag = True
                break

        if flag:
            while True:
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
def excluirUsuario():
    usuarios = dados["usuarios"]
    flag = False

    while True:
        consultarUsuarios(False)
        usuarioId = input(
            "Digite o id do usuario a ser excluido ou pressione enter para sair.: "
        )

        if usuarioId == "":
            break

        for i in range(len(usuarios)):
            if str(usuarios[i]["id"]) == usuarioId:
                flag = True
                break

        if flag:
            while True:
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


def cadastrarLivro():
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
        "locado": False,
    }
    dados["livros"].append(novoLivro)
    limpar()
    print("Cadastro realizado com sucesso")

    return dados


def consultarLivro(waitInp=True):
    livros = dados["livros"]

    print(tabulate(livros, headers="keys", tablefmt="github"))
    if waitInp:
        input("Tecle Enter para sair.: ")
        limpar()


def editarLivro():
    livros = dados["livros"]
    flag = False

    while True:
        consultarLivro(False)
        livroId = input(
            "Digite o id do livro a ser alterado ou pressione enter para sair.: "
        )

        if livroId == "":
            break
        limpar()

        for livro in livros:
            if str(livro["id"]) == livroId:
                flag = True
                break

        if flag:
            while True:
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


def excluirLivro():
    livros = dados["livros"]
    flag = False

    while True:
        consultarLivro(False)
        livroId = input(
            "Digite o id do livro a ser excluido ou pressione enter para sair.: "
        )

        if livroId == "":
            break

        for i in range(len(livros)):
            if str(livros[i]["id"]) == livroId:
                flag = True
                break

        if flag:
            while True:
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


# TO DO:


# gerenciar varios livros (sistema de estoque e empréstimos)
# crud de empréstimos (nova lista no json)
# relatórios
def solicitarLivro(): ...


def devolverLivro(): ...


def editaConta(id):
    usuarios = dados["usuarios"]
    while True:
        print(f"1 - nome: {usuarios[id]['nome']}\n2 - senha")
        comando = input("Digite o que deseja alterar.: ")
        if comando == "1":
            usuarios[id]["nome"] = input("Digite o novo nome.: ")
        elif comando == "2":
            while True:
                senha = getpass("Insira sua senha atual: ")
                if usuarios[id]["senha"] == senha:
                    usuarios[id]["senha"] = input("Digite a nova senha.: ")
                else:
                    limpar()
                    print("senha incorreta, tente novamente!")

    input("Tecle Enter para sair.: ")


def meusLivros(): ...


# -----------BIBLIOTECA-----------


# Função principal contendo todos os CRUDS de livros e usuario
def biblioteca(sessionId):
    usuarios = dados["usuarios"]
    print(f"SEJA BEM VINDO {usuarios[sessionId]['nome']}")

    while True:
        comando = None
        print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")

        if usuarios[sessionId]["admin"] == "nao":
            opcoes = {
                "1": solicitarLivro,
                "2": devolverLivro,
                "3": editaConta,
                "4": meusLivros,
            }

            while comando not in opcoes.keys():
                print(
                    "1 - Solicitar livro\n2 - Devolver livro\n3 - Editar conta\n4 - Meus livros\n5 - Sair"
                )

                comando = input(".: ")

                if comando == "5":
                    guardarDados("dados.json")
                    exit()

            opcoes[comando]()
            limpar()

        if usuarios[sessionId]["admin"] == "sim":
            opcoes = {
                "1": cadastrarLivro,
                "2": consultarLivro,
                "3": editarLivro,
                "4": excluirLivro,
                "5": cadastrarUsuario,
                "6": consultarUsuarios,
                "7": editarUsuarios,
                "8": excluirUsuario,
            }

            while comando not in opcoes.keys():
                print(
                    "Gerenciamento de livros: \n1 - Cadastrar Livro\n2 - Consultar livros\n3 - Editar Livros\n4 - Excluir Livro"
                )
                print(
                    "\nGerenciamento de usuarios: \n5 - Cadastrar usuário\n6 - Consultar usuarios\n7 - Editar Usuario\n8 - Excluir usuário\n9 - Salvar e sair"
                )

                if comando == "9":
                    guardarDados("dados.json")
                    exit()

                comando = input(".: ")
                limpar()

            opcoes[comando]()

        limpar()


# Verificação de credencias de login
def login():
    usuarios = dados["usuarios"]
    limpar()
    while True:
        print("---LOGIN---")
        usuario = input("Insira seu email: ")
        senha = getpass("Insira sua senha: ")

        for i in range(len(usuarios)):
            if usuario == usuarios[i]["email"] and bcrypt.checkpw(
                senha.encode("utf-8"), usuarios[i]["senha"].encode("utf-8")
            ):
                limpar()
                biblioteca(i)
        limpar()
        print("Nome ou senha incorreto, por favor tente novamente")


dados = carregar_usuarios("dados.json")


def main():
    login()


if __name__ == "__main__":
    main()
