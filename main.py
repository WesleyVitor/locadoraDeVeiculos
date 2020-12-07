import veiculos
import clientes
import aluguel
import quita_divida
import os 
import platform
import relatorios
def clear():
  if platform.system() == 'Windows':
    return os.system("cls")
  elif platform.system() == 'Linux':
    return os.system("clear")

sair = 'n'
while sair == 'n':
  print("== Menu ===========")
  print("1. Clientes")
  print("2. Veiculos")
  print("3. Alugueis")
  print("4. Quitar Dividas")
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
  else:
    print("Respeite o menu:")
  sair = input("Quer sair do sistema(s/n)?")


##Ainda falta gerar os relatorios