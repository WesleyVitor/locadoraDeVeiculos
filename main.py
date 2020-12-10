import veiculos
import clientes
import aluguel
import quita_divida
import os 
import platform
import pickle
def clear():
  if platform.system() == 'Windows':
    return os.system("cls")
  elif platform.system() == 'Linux':
    return os.system("clear")
def deserializar_quita_divida():
  arquivo = open("db_quita_dividas.txt",'rb')
  return pickle.load(arquivo)
def gerar_relatorio():
  dividas = deserializar_quita_divida()
  if len(dividas)>0:
    print("==============================")
    print("=== RELATÓRIO DA LOCADORA ====")
    print("======== PyRent-a-Car ========")
    print("==============================")
    print("TOTAL DE DIVIDAS QUITADAS:")
    print("## Valor: %d"%len(dividas))
    print("==========================")
    print("FATURAMENTO DA EMPRESA:")
    faturamento=0
    for divida in dividas:
      faturamento += dividas[divida][4]
    print("## Valor:R$ %.3f"%faturamento)
    print("===========================================")
    for divida in dividas:
      print("-----------")
      print("# Cliente Associado:",dividas[divida][0])
      print("# Veiculos Alugados:")
      veiculos_alugados = dividas[divida][1][0]
      for veiculo in veiculos_alugados:
        print("##",veiculo)
      print("# Dias de aluguel:",dividas[divida][1][1])
      print("# Total a pago:R$ %.2f"%dividas[divida][4])
      print("# Multa por atraso: R$ %.2f"%dividas[divida][3])
      print("-----------")
  else:
    print("Não existe dividas quitadas!")


def geral():
  sair = 'n'
  while sair == 'n':
    print("== Menu ===========")
    print("|")
    print("| 1. Clientes")
    print("| 2. Veiculos")
    print("| 3. Alugueis")
    print("| 4. Quitar Dividas")
    print("| 5. Relatório")
    print("|-----------------")
    opcao = input("Digite a sua opção:")
    clear()
    if opcao == '1':
      clientes.geral()
    elif opcao == '2':
      veiculos.geral()
    elif opcao == '3':
      aluguel.geral()
    elif opcao == '4':
      quita_divida.geral()
    elif opcao == '5':
      gerar_relatorio()
    else:
      print("Respeite o menu:")
    sair = input("Quer sair do sistema(s/n)?")
clear()
geral()
