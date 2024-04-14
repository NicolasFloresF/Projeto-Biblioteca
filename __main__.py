"""
Construção de sistema para automatizar
o gerenciamento de uma biblioteca
● Gerenciamento de usuários (CRUD).
● Gerenciamento de livros (CRUD).
● Registro de empréstimos e devoluções.
"""
#Estaremos trabalhando com JSON ao longo do trabalho 1
import json

def main():

	# Limpa a tela
	def limpar():
		print("\033c", end="")


	#Função para percorrer arquivo JSON e retornar seu conteúdo em uma variavel a ser operada
	def listar_itens(nomeArquivo):
		with open(nomeArquivo, 'r') as arquivo:
			dados = json.load(arquivo)
		return dados

	def excluir_item(nomeArquivo, nomeProcurado):
		cont = 0
		auxIndice = 0
		with open(nomeArquivo, 'r') as arquivo:
			linhas = []
			linhasIndividuais = []
			for aux in arquivo:
				linhas.append(aux)
			for i in range(len(linhas)):
				linhasIndividuais.append(linhas[i].split(','))
			for selecionaLinha in linhasIndividuais:
				for campo in selecionaLinha:
					cont += 1
					if campo  == nomeProcurado:
						auxIndice = cont

			auxIndice = int(((auxIndice+1)/2)-1)
			del linhasIndividuais[auxIndice]



	#Verificação de credencias de login
	def login(dados, quantUsuarios):
			print("---LOGIN---")
			usuario = input("Insira seu nome: ")
			senha = input("Insira sua senha: ")
			for i in range(quantUsuarios):
				if usuario == dados["usuarios"][i]["nome"] and senha == dados["usuarios"][i]["senha"]:
					print(f"SEJA BEM VINDO {usuario}")
					return usuario, dados["usuarios"][i]["admin"]
			print("Nome ou senha incorreto, por favor tente novamente")
			return "0"


#-----------CRUDS USUARIO-----------
	#Insere o novo usuario na variavel dados
	def cadastrarUsuario(dados):
		usuario = input("Insira seu nome: ")
		senha = input("Insira sua senha: ")
		admin = "nao"
		livros_emprestimo = []
		#criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados"
		dicionario = {
			'nome': usuario,
			'senha': senha,
			'admin': "nao",
			'livros_emprestimos': []
		}
		dados["usuarios"].append(dicionario)

		return dados
	def listarUsuarios(dados):
		for i in range(dados['usuarios']):
			nome = dados["usuarios"][i]["nome"]
			livros = dados["usuarios"][i]["livros_emprestimos"]
			print(f"{nome} - {livros}")

# -----------BIBLIOTECA-----------

	#Função principal contendo todos os CRUDS de livros e usuario
	def biblioteca(usuario, dadosUsuario, admin):
		while True:
			print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
			if admin == "nao":
				comando = input("1 - Solicitar livro\n2 - Devolver livro\n3 - Sair\n")
				if comando == "1":
					#solicitarLivro()
				if comando == "2":
					#DevolverLivro()
				if comando == "3":
					break
			if admin == "sim":
				print("---BEM VINDO ADMIN---")
				print("1 - Cadastrar Livro\n2 - Consultar livros\n3 - Editar Livros\n4 - Excluir Livro\n")
				print("5 - Cadastrar usuário\n6 - Consultar usuarios\n7 - Editar Usuario\n8 - Excluir usuário\n9 - Sair")
				comando = input(".: ")
				if comando == "1":
					#CadastrarLivro()
				elif comando == "2":
					#ConsultarLivro()
				elif comando == "3":
					#EditarLivro()
				elif comando == "4":
					#ExcluirLivro()
				elif comando == "5":
					dadosUsuario = cadastrarUsuario(dadosUsuario)
				elif comando == "6":
					#ConsultarUsuarios()
				elif comando == "7":
					#EditarUsuarios()
				elif comando == "8":
					#ExcluirUsuario()
				elif comando == "9":
					break

	def home(dados, quantUsuarios):
		while True:
			print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
			comando = input("1 - Logar\n2 - Cadastrar\n3 - Finalizar programa\n")
			if comando == "1":

				limpar()
				#Caso o login ocorra com sucesso retorna o usuario para utilizar nas operações futuras
				usuario = "0"
				while usuario == "0":
					usuario, admin = login(dados, quantUsuarios)
				limpar()
				#Envia as informações para a parte principal
				biblioteca(usuario, dados, admin)
			if comando == "2":
				limpar()
				#Armazena o novo usuario na variavel dados
				dados = cadastrarUsuario(dados)
				admin = "nao"
				limpar()
				#Envia as informações para a parte principal
				biblioteca(usuario, dados, admin)

			if comando == "3":
				print("Obrigado por utilizar nosso sistema.\nAtt: \n-EdCarvalho\n-NiFlores")
				break

	dados = listar_itens("usuario.json")
	quantUsuarios = len(dados['usuarios'])
	print("------SEJA BEM VINDO A BIBLIOTECA 7000------")
	print(f"-TEMOS {quantUsuarios} USUARIOS CADASTRADOS-")
	home(dados, quantUsuarios)

if __name__ == '__main__':
    main()
