import veiculos_metodos as CV 
import pickle
VEICULOS_MODEL ="models/veiculos.p"
#INDEX 
#Ler o arquivo Veiculos
def deserializar():
  global VEICULOS_MODEL
  arquivo = open(VEICULOS_MODEL,'rb')
  return pickle.load(arquivo)
def serializar(dado):
  global VEICULOS_MODEL
  arquivo = open(VEICULOS_MODEL,'wb')
  pickle.dump(dado, arquivo)
  

def cadastrar_veiculos(nome,quantidade, valor_por_hora, valor_de_muta_por_hora):
  veiculos = deserializar()
  if nome in veiculos:
    return -1
  else:
    veiculos[nome] = [quantidade, valor_por_hora, valor_de_muta_por_hora]
    serializar(veiculos)
    return None
#Delete
#Pega as informacoes e verifica se existe um cpf e delete o tal cliente e escreve o novo
#dicionario no arquivo
def deletar_veiculos(nome):
  veiculos = deserializar()
  if nome in veiculos:
    del veiculos[nome]
    serializar(veiculos)
    return None
  else:
    return -1
#SHOW
#Pega as informacoes e verifica se existe um cpf e retorna o expecifico
def show_veiculo(nome):
  veiculos = deserializar()
  if nome in veiculos:
    return veiculos[nome]
  else:
    return -1
def geral(opcao):
  if opcao == '1':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM NOVO VEICULO NÃO EXISTENTE===")
      nome_do_veiculo = input("DIGITE O NOME DO VEICULO:")
      quantidade_de_veiculos = input("DIGITE A QUANTIDADE DO VEICULO CORRESPONDENTE:")
      valor_por_hora = float("DIGITE O VALOR A SER COBRADO POR HORA PARA ESTE VEICULO:")
      valor_de_muta_por_hora = float("DIGITE O VALOR DA MUTA POR HORA PARA ESTE VEICULO:")
      retorno = cadastrar_veiculos(nome_do_veiculo, quantidade_de_veiculos, valor_por_hora, valor_de_muta_por_hora)
      if retorno != -1:
        print("VEICULO CADASTRADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS JÁ EXISTE ESSE VEICULO NO SISTEMA!!")
      sair = input("===ADICINAR NOVAMENTE?(S - N):")
    return None
  elif opcao == '2':
    print("===AQUI VOCÊ PODERÁ LISTAR TODOS OS VEICULOS EXISTENTES NO SISTEMA===")
    veiculos = deserializar()
    for nome in veiculos:
      print()
      print(""" 
        Nome: %s
        Quantidade: %s
       """%(nome, veiculos[nome]))
      print()
    return None
  elif opcao == '3':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS VEICULOS EXISTENTES NO SISTEMA===")
      nome = input("DIGITE O NOME DO VEICULO CORRESPONDENTE:")
      retorno = deletar_veiculos(nome)
      if retorno != -1:
        print("VEICULO APAGADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS O VEICULO NÃO EXISTE NO SISTEMA !!")
      sair = input("===APAGAR NOVAMENTE?(S - N):")
    return None
  elif opcao == '4':
    sair = 'S'
    while sair.upper()!='N':
      print("===AQUI VOCÊ PODERÁ LISTAR O VEICULO EXISTENTES NO SISTEMA===")
      nome = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      quantidade = show_veiculo(nome)
      if veiculos != -1:
        print(""" 
        Nome:%s
        Quantidade: %s
        """%(quantidade, nome))
      else:
        print("DESCULPE, MAS O VEICULO NÃO EXISTE NO SISTEMA !!")
      sair = input("===ACESSAR OUTRO?(S - N)===")
    return None
  else:
    print("RESPEITE O MENU!!")
    return -1
