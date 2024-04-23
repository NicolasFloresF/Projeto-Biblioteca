"""
Construção de sistema para automatizar
o gerenciamento de uma biblioteca
● Gerenciamento de usuários (CRUD).
● Gerenciamento de livros (CRUD).
● Registro de empréstimos e devoluções.
"""

# TO DO:
# gerenciar varios livros (sistema de estoque e empréstimos)
# crud de empréstimos (nova lista no json)
# relatórios

# Estaremos trabalhando com JSON ao longo do trabalho 1
import json
import bcrypt
from getpass import getpass
from tabulate import tabulate
import datetime
import copy


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


# -----------CRUDS USUARIO ADMIN-----------


# Insere o novo usuario na variavel dados
def cadastrarUsuario():
    usuarios = dados["usuarios"]
    
    print("===== Cadastro de Usuario =====")
    id = dados["usuarios"][-1]["id"] + 1
    nome = input("Insira seu nome: ")

    while True:
        email = input("Insira seu email: ")

        if list(filter(lambda i: i["email"] == email, usuarios)) == []:
            break
        else:
            print("Email já registrado no sistema!")

    while True:
        senha = getpass("Insira sua senha: ")
        confirma = getpass("Confirme sua senha: ")
        if senha == "":
            print("Senha não pode ser vazia, tente novamente")
        elif senha != confirma:
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

    while True:
        print("===== Edição de Usuario =====")
        flag = False
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
                    novaSenha = getpass("Digite a nova senha.: ")
                    usuario["senha"] = bcrypt.hashpw(
                        novaSenha.encode("utf8"), bcrypt.gensalt()
                    ).decode("utf-8")
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


# Exclui o usuário a partir do seu id
def excluirUsuario():
    usuarios = dados["usuarios"]

    while True:
        print("===== Exclusão de Usuario =====")
        flag = False
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
                    f"Deseja mesmo excluir {usuarios[i]['nome']}? [Sim/Nao].: "
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
    print("Cadastro de Livros =====")
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
    while True:
        print("===== Edição de Livros =====")
        flag = False
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
    while True:
        print("===== Exclusão de livros =====")
        flag = False
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


# -----------GERENCIAMENTO DE CONTA DO USUARIO -----------


# Permite a edição da conta pelo usuário
def editaConta(id):
    usuarios = dados["usuarios"]
    while True:
        print("===== Edição de conta =====")
        print(f"1 - nome: {usuarios[id]['nome']}\n2 - senha")
        comando = input("Digite o que deseja alterar ou tecle enter para sair.: ")
        limpar()
        if comando == "1":
            usuarios[id]["nome"] = input("Digite o novo nome.: ")
            limpar()
        elif comando == "2":
            while True:
                senha = getpass("Insira sua senha atual: ")
                if bcrypt.checkpw(
                    senha.encode("utf-8"), usuarios[id]["senha"].encode("utf-8")
                ):
                    novaSenha = getpass("Digite a nova senha.: ")
                    usuarios[id]["senha"] = bcrypt.hashpw(
                        novaSenha.encode("utf8"), bcrypt.gensalt()
                    ).decode("utf-8")
                    limpar()
                    break
                else:
                    limpar()
                    print("senha incorreta, tente novamente!")
        elif comando == "":
            limpar()
            break


# Exibe ao usuário os livros emprestados
def meusLivros(id, waitInp=True):
    usuarios = dados["usuarios"]
    livros = dados["livros"]
    emprestimos = copy.deepcopy(dados["emprestimos"])
    usuario = usuarios[id]

    # como printar apenas as informações necessárias para o usuario?
    print("===== Meus Livros =====")
    # sem dar update
    emprestimos = list(filter(lambda i: i["usuario"] == id, emprestimos))
    emprestimos = list(filter(lambda i: i["devolucao"] == "", emprestimos))

    for emprestimo in emprestimos:
        livroPorId = list(filter(lambda i: i["id"] == emprestimo["livro"], livros))
        if len(livroPorId) > 0:
            emprestimo["livro"] = livroPorId[0]["titulo"]

    print(tabulate(emprestimos, headers="keys"))

    if waitInp:
        input("\nTecle Enter para sair.: ")
        limpar()


# Requisita o livro por seu id e adciona um novo empréstimo
def solicitarLivro(id):
    usuarios = dados["usuarios"]
    livros = dados["livros"]
    usuario = usuarios[id]

    while True:
        print("===== Livros Disponíveis =====")
        flag = False
        livros = list(filter(lambda i: i["estoque"] > 0, livros))
        print(tabulate(livros, tablefmt="github"))

        livroId = input("Insira o ID do livro ou Tecle Enter para sair.: ")

        if livroId == "":
            break

        for i in range(len(livros)):
            if str(livros[i]["id"]) == livroId:
                flag = True
                break

        if flag:
            if livros[i]["estoque"] > 0:
                livros[i]["estoque"] -= 1
                hoje = datetime.date.today()
                if len(dados["emprestimos"]) == 0:
                    emprestimoId = 1
                else:
                    emprestimoId = dados["emprestimos"][-1]["id"] + 1
                emprestimo = {
                    "id": emprestimoId,
                    "livro": int(livroId),
                    "usuario": id,
                    "data_emprestimo": hoje.strftime("%d/%m/%Y"),
                    "prazo": (hoje + datetime.timedelta(days=7)).strftime("%d/%m/%Y"),
                    "devolucao": "",
                }

                dados["emprestimos"].append(emprestimo)

                limpar()
                print(
                    f"Solicitação do livro {livros[i]['titulo']} realizada com sucesso sucesso"
                )
            else:
                limpar()
                print("Livro não disponivel")
        else:
            limpar()
            print("ID inválido, tente novamente")


# devolve um livro do usuario
def devolverLivro(id):
    usuarios = dados["usuarios"]
    livros = dados["livros"]
    emprestimos = dados["emprestimos"]
    usuario = usuarios[id]
    
    while True:
        print("===== Devolução de livros =====")
        emprestimos = list(filter(lambda i: i["usuario"] == id, emprestimos))
        flag = False
        meusLivros(id, False)
        emprestimoId = input("\nInsira o ID do livro ou Tecle Enter para sair.: ")
        limpar()

        if emprestimoId == "":
            break

        for i in range(len(emprestimos)):
            if str(emprestimos[i]["id"]) == emprestimoId:
                flag = True
                break

        if flag:
            for j in range(len(livros)):
                if livros[j]["id"] == emprestimos[i]["livro"]:
                    livros[j]["estoque"] += 1

            emprestimos[i]["devolucao"] = datetime.date.today().strftime("%d/%m/%Y")
        else:
            limpar()
            print("ID inválido, tente novamente")


# -----------RELATÓRIOS-----------

def formataEmprestimos():
    usuarios = dados["usuarios"]
    livros = dados["livros"]
    emprestimos = copy.deepcopy(dados["emprestimos"])

    for emprestimo in emprestimos:
        livroPorId = list(filter(lambda i: i["id"] == emprestimo["livro"], livros))
        usuarioPorId = list(filter(lambda i: i["id"] == emprestimo["usuario"], usuarios))

        if len(livroPorId) > 0 and len(usuarioPorId) > 0:
            emprestimo["livro"] = livroPorId[0]["titulo"]
            emprestimo["usuario"] = usuarioPorId[0]["nome"]
    
    return emprestimos


def consultarEmprestimos():
    emprestimos = formataEmprestimos()
    print("===== Lista de empréstimos =====")
    print(tabulate(emprestimos, headers="keys"))
    input("\nTecle Enter para sair.: ")
    limpar()


def devolucoesAtrasadas():
    emprestimos = formataEmprestimos()
    print("===== Lista de devoluções atrasadas =====")
    hoje = datetime.date.today().strftime("%d/%m/%Y")
    emprestimos = list(filter(lambda i: datetime.datetime.strptime(i["prazo"],"%d/%m/%Y") < datetime.datetime.strptime(hoje,"%d/%m/%Y") and i["devolucao"] == "", emprestimos))
    print(tabulate(emprestimos, headers="keys"))
    input("\nTecle Enter para sair.: ")
    limpar()


def devolucoes():
    emprestimos = formataEmprestimos()
    print("===== Lista de livros a serem entregues =====")
    emprestimos = list(filter(lambda i: i["devolucao"] != "", emprestimos))
    print(tabulate(emprestimos, headers="keys"))
    input("\nTecle Enter para sair.: ")
    limpar()


def paraDevolucao():
    emprestimos = formataEmprestimos()
    emprestimos = list(filter(lambda i: i["devolucao"] == "", emprestimos))
    print("===== Lista de livros que já foram entregues =====")
    print(tabulate(emprestimos, headers="keys"))
    input("\nTecle Enter para sair.: ")
    limpar()


# -----------BIBLIOTECA-----------
# -----------ADMIN-----------
def gerenciarUsuarios():
    opcoes = {
        "1": cadastrarUsuario,
        "2": consultarUsuarios,
        "3": editarUsuarios,
        "4": excluirUsuario,
        "5": "sair",
    }

    while True:
        comando = None
        while comando not in opcoes.keys():
            print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
            print(
                "1 - Cadastrar usuario\n2 - Consultar usuarios\n3 - Editar usuarios\n4 - Excluir usuario\n5 - Voltar"
            )

            comando = input(".: ")
            limpar()

        if comando == "5":
            break

        opcoes[comando]()
        limpar()


def gerenciarLivros():
    opcoes = {
        "1": cadastrarLivro,
        "2": consultarLivro,
        "3": editarLivro,
        "4": excluirLivro,
        "5": "sair",
    }

    while True:
        comando = None
        while comando not in opcoes.keys():
            print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
            print(
                "1 - Cadastrar Livro\n2 - Consultar livros\n3 - Editar Livros\n4 - Excluir Livro\n5 - Voltar"
            )

            comando = input(".: ")
            limpar()

        if comando == "5":
            break
        
        opcoes[comando]()
        limpar()


def relatorios():
    opcoes = {
        "1": consultarEmprestimos,
        "2": devolucoes,
        "3": devolucoesAtrasadas,
        "4": paraDevolucao,
        "5": "sair",
    }

    while True:
        comando = None
        while comando not in opcoes.keys():
            print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
            print(
                "1 - Listar emprestimos\n2 - Listar Devoluções\n3 - Listar Devoluções atrasadas\n4 - Listar para devolução\n5 - Voltar"
            )

            comando = input(".: ")
            limpar()

        if comando == "5":
            break
        
        opcoes[comando]()
        limpar()


# Função principal contendo todos os CRUDS de livros e usuario
def biblioteca(sessionId):
    usuarios = dados["usuarios"]
    print(f"SEJA BEM VINDO {usuarios[sessionId]['nome']}")

    while True:
        comando = None

        if usuarios[sessionId]["admin"] == "nao":
            opcoes = {
                "1": solicitarLivro,
                "2": devolverLivro,
                "3": editaConta,
                "4": meusLivros,
            }

            while comando not in opcoes.keys():
                print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
                print(
                    "1 - Solicitar livro\n2 - Devolver livro\n3 - Editar conta\n4 - Meus livros\n5 - Sair"
                )

                comando = input(".: ")

                if comando == "5":
                    guardarDados("dados.json")
                    exit()
                limpar()

            opcoes[comando](sessionId)

        if usuarios[sessionId]["admin"] == "sim":
            opcoes = {
                "1": gerenciarUsuarios,
                "2": gerenciarLivros,
                "3": relatorios,
            }

            while comando not in opcoes.keys():
                print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
                print(
                    "1 - Gerenciamento de usuarios\n2 - Gerenciamento de livros\n3 - relatorios\n4 - Salvar e sair"
                )

                comando = input(".: ")

                if comando == "4":
                    guardarDados("dados.json")
                    exit()
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
