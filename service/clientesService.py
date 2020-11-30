import ast

clienteModel ="models/clientes.txt"

def escreverNoArquivo(dado):
  global clienteModel
  arquivo = open(clienteModel,'w')
  arquivo.write(str(dado))
  arquivo.close()
  return arquivo

#Pega os dados que veio do arquivo e transforma para dicionario
def pegaClientes():
  return ast.literal_eval(leituraDeClientes())

#INDEX 
#Ler o arquivo Clientes
def leituraDeClientes():
  global clienteModel
  clientes = open(clienteModel)
  return clientes.read()

#CREATE
#Pega os as informacoes do arquivo em formato de dicionario e verifica se não existe
#um cpf e faz o cadastro de uma nova key(cpf) e manda escrever no arquivo
def cadastrarClientes(cpf, nome):
  clientes = pegaClientes()
  if cpf in clientes:
    return -1
  else:
    clientes[cpf] = nome
    escreverNoArquivo(clientes)
    return None


#SHOW
#Pega as informacoes e verifica se existe um cpf e retorna o expecifico
def showCliente(cpf):
  clientes = pegaClientes()
  if cpf in clientes:
    return clientes[cpf]
  else:
    return -1

#Delete
#Pega as informacoes e verifica se existe um cpf e delete o tal cliente e escreve o novo
#dicionario no arquivo
def deleteCliente(cpf):
  clientes = pegaClientes()
  if cpf in clientes:
    del clientes[cpf]
    escreverNoArquivo(clientes)
    return None
  else:
    return -1
