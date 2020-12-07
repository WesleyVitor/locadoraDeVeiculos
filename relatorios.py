import clientes
import veiculos
import aluguel
import quita_divida
import pickle
def deserializar_quita_divida():
  arquivo = open("db_quita_dividas.txt",'rb')
  return pickle.load(arquivo)

dividas = deserializar_quita_divida()
if len(dividas)>0:
  for divida in dividas:
    print("-----------")
    print(dividas[divida])
    print("-----------")
else:
  print("Não existe dividas quitadas!")