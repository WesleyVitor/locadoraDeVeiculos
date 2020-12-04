
import pickle
clienteModel ="models/clientes.p"

def serializar(dado):
  global clienteModel
  arquivo = open(clienteModel,'wb')
  pickle.dump(dado, arquivo)
  return None

#INDEX 
#Ler o arquivo Clientes
def deserializar():
  global clienteModel
  clientes = pickle.load(clienteModel)
  return clientes

#CREATE
#Pega os as informacoes do arquivo em formato de dicionario e verifica se não existe
#um cpf e faz o cadastro de uma nova key(cpf) e manda escrever no arquivo
def cadastrar_clientes(cpf, nome):
  clientes = deserializar()
  if cpf in clientes:
    return -1
  else:
    #SALVANDO A QUANTIDADE DE VEZES QUE ELE PEGOU EMPRESTADO 
    clientes[cpf] = [nome, 0]
    serializar(clientes)
    return None

#Delete
#Pega as informacoes e verifica se existe um cpf e delete o tal cliente e escreve o novo
#dicionario no arquivo
def deletar_cliente(cpf):
  clientes = deserializar()
  if cpf in clientes:
    del clientes[cpf]
    serializar(clientes)
    return None
  else:
    return -1

def geral(opcao):
  #CRIAR CLIENTE
  if opcao == '1':
    print()
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM NOVO CLIENTE NÃO EXISTENTE===")
      nome = input("DIGITE O NOME DO CLIENTE:")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = cadastrar_clientes(cpf, nome)
      if retorno != -1:
        print("USUÁRIO CADASTRADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS JÁ EXISTE ESSE USUÁRIO NO SISTEMA!!")
      sair = input("===ADICINAR NOVAMENTE?(S - N)")
    return None
  #LISTAR TODOS OS CLIENTES
  elif opcao == '2':
    print("===AQUI VOCÊ PODERÁ LISTAR TODOS OS CLIENTES EXISTENTES NO SISTEMA===")
    clientes = deserializar()
    print(clientes)
    for cpf in clientes:
      print()
      print(""" 
        Nome: %s
        CPF: %s
       """%(clientes[cpf], cpf))
      print()
    return None
  #APAGAR TODOS OS CLIENTES
  elif opcao == '3':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS CLIENTES EXISTENTES NO SISTEMA===")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = deletar_cliente(cpf)
      if retorno != -1:
        print("USUÁRIO APAGADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS O USUPARIO NÃO EXISTE NO SISTEMA !!")
      sair = input("===APAGAR NOVAMENTE?(S - N)")
    return None
  else:
    print("RESPEITE O MENU!!")
    return -1
