def main():
#Descrição do problema

#Estaremos trabalhando com JSON ao longo do trabalho 1
	import json
	
	
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
					return usuario
			print("Nome ou senha incorreto, por favor tente novamente")
			return "0"
	#Insere o novo usuario na variavel dados
	def cadastrarUsuario(dados):
		usuario = input("Insira seu nome: ")
		senha = input("Insira sua senha: ")
		admin = "nao"
		livros_emprestimo = []
		#criar algoritmo para juntar os dados acima em um dicionario e adicionar isso na lista "dados" 
		dados["usuarios"].append("receber dicionario")
		
		return dados
		
	
	#Função principal contendo todos os CRUDS de livros e usuario
	def biblioteca(usuario, dadosUsuario):
		print("teste")
			
	def home(dados, quantUsuarios):
		while True:
			print("---SELECIONE UMA DAS OPÇÕES ABAIXO---")
			comando = input("1 - Logar\n2 - Cadastrar\n3 - Finalizar programa\n")
			if comando == "1":
				#Limpa a tela
				print("\033c", end="")
				#Caso o login ocorra com sucesso retorna o usuario para utilizar nas operações futuras
				usuario = "0"
				while usuario == "0":
					usuario = login(dados, quantUsuarios)
				print("\033c", end="")
				#Envia as informações para a parte principal
				biblioteca(usuario, dados)
			if comando == "2":
				#Limpa a tela
				print("\033c", end="")
				#Armazena o novo usuario na variavel dados
				dados = cadastrarUsuario(dados)
				print("\033c", end="")
				#Envia as informações para a parte principal
				#biblioteca(usuario, dados)
				
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
