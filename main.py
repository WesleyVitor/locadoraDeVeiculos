import veiculos
import clientes
import aluguel
import quita_divida
from limpa_tela import clear
from relatorios_gerais import gerar_relatorio

sair = 'n'
while sair == 'n':
  print("====== Menu =========")
  print("|")
  print("| 1. Clientes       |")
  print("| 2. Veiculos       |")
  print("| 3. Alugueis       |")
  print("| 4. Quitar Dividas |")
  print("| 5. Relatório      |")
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

