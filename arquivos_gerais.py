import pickle
def verificar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'rb')
    arquivo.close()
  except:
    arquivo = open(nome_arquivo,'wb')
    pickle.dump({}, arquivo)
    arquivo.close()

def pegar_quita_divida():
  verificar_arquivo("db_quita_dividas.txt")
  arquivo = open("db_quita_dividas.txt",'rb')
  return pickle.load(arquivo)

def pegar_emprestimos():
  verificar_arquivo("db_emprestimos.txt")
  arquivo = open("db_emprestimos.txt",'rb')
  emprestimos = pickle.load(arquivo)
  arquivo.close()
  return emprestimos

def pegar_clientes():
  verificar_arquivo("db_clientes.txt")
  arquivo = open("db_clientes.txt",'rb')
  clientes = pickle.load(arquivo)
  arquivo.close()
  return clientes

def pegar_veiculos():
  verificar_arquivo("db_veiculos.txt")
  arquivo = open("db_veiculos.txt",'rb')
  veiculos = pickle.load(arquivo)
  arquivo.close()
  return veiculos

def gravar_emprestimos(dados):
  verificar_arquivo("db_emprestimos.txt")
  arquivo = open("db_emprestimos.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def gravar_veiculos(dados):
  verificar_arquivo("db_veiculos.txt")
  arquivo = open("db_veiculos.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def gravar_clientes(dados):
  arquivo = open("db_clientes.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def gravar_quita_divida(dados):
  verificar_arquivo("db_quita_dividas.txt")
  arquivo = open("db_quita_dividas.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()