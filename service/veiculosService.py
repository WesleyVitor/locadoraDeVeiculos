import ast

VEICULOS_MODEL ="models/veiculos.txt"

def escreverNoArquivo(dado):
  global VEICULOS_MODEL
  arquivo = open(VEICULOS_MODEL,'w')
  arquivo.write(str(dado))
  arquivo.close()
  return arquivo
#Pega os dados que veio do arquivo e transforma para dicionario
def pega_veiculos():
  return ast.literal_eval(leitura_veiculos())

#INDEX 
#Ler o arquivo Veiculos
def leitura_veiculos():
  global VEICULOS_MODEL
  veiculos = open(VEICULOS_MODEL)
  return veiculos.read()

#CREATE
#Pega os as informacoes do arquivo em formato de dicionario e verifica se não existe
#um nome(veiculo) e faz o cadastro de uma nova key(nome) e manda escrever no arquivo a sua quantidade
def cadastrar_veiculos(nome,quantidade):
  veiculos = pega_veiculos()
  if nome in veiculos:
    return -1
  else:
    veiculos[nome] = quantidade
    escreverNoArquivo(veiculos)
    return None

#Atualiza a quantidade de veiculos depois do emprestimo
def update_veiculo(nome, opc):
  veiculos = pega_veiculos()
  if nome in veiculos:
    if opc == 'incrementar':
      veiculos[nome] = veiculos[nome]+1
    elif opc == 'decrementar':
      veiculos[nome] = veiculos[nome]-1
    escreverNoArquivo(veiculos)
    return veiculos[nome]
  else:
    return -1

#SHOW
#Pega as informacoes e verifica se existe um cpf e retorna o expecifico
def show_veiculos(nome):
  veiculos = pega_veiculos()
  if nome in veiculos:
    return veiculos[nome]
  else:
    return -1

#Delete
#Pega as informacoes e verifica se existe um cpf e delete o tal cliente e escreve o novo
#dicionario no arquivo
def delete_veiculos(nome):
  veiculos = pega_veiculos()
  if nome in veiculos:
    del veiculos[nome]
    escreverNoArquivo(veiculos)
    return None
  else:
    return -1
