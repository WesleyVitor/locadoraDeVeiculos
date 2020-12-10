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
def verificar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'rb')
    arquivo.close()
  except:
    arquivo = open(nome_arquivo,'wb')
    pickle.dump({}, arquivo)
    arquivo.close()

def gerar_relatorio_veiculos():
  verificar_arquivo("db_veiculos.txt")
  arquivo = open("db_veiculos.txt",'rb')
  lista_veiculos = pickle.load(arquivo)
  arquivo.close()
  for placa in lista_veiculos:
    print("="*32)
    print("Placa:",placa)
    print("Quantidade:",lista_veiculos[placa][0])
    print("Marca:",lista_veiculos[placa][1])
    print("Modelo:",lista_veiculos[placa][2])
    print("Ano:",lista_veiculos[placa][3])
    print("Diária:",lista_veiculos[placa][4])
    print("Multa:",lista_veiculos[placa][5])
  print("==========================================")

def gerar_relatorio_dividas_quitadas():
  verificar_arquivo("db_quita_dividas.txt")
  arquivo = open("db_quita_dividas.txt",'rb')
  dividas = pickle.load(arquivo)
  arquivo.close()
  if len(dividas)>0:
    print("TOTAL DE DIVIDAS QUITADAS:")
    print("## Valor: %d"%len(dividas))
    print("==========================")
    print("FATURAMENTO DA EMPRESA:")
    faturamento=0
    for divida in dividas:
      faturamento += dividas[divida][4]
    print("## Valor:R$ %.3f"%faturamento)
    print("===========================================")
    print("-------------------------------------------")
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
        print("==========================================")
    print("==========================================")
  else:
    print("Não existe dividas quitadas!")

def gerar_relatorio_clientes():
  verificar_arquivo("db_clientes.txt")
  arquivo = open("db_clientes.txt",'rb')
  lista_clientes = pickle.load(arquivo)
  arquivo.close()
  for cpf in lista_clientes:
    print("="*32)
    print("CPF:",cpf)
    print("Nome Completo:",lista_clientes[cpf][0])
    print("Email:",lista_clientes[cpf][1])
    print("Rua:",lista_clientes[cpf][2])
    print("Bairro:",lista_clientes[cpf][3])
    print("Idade:",lista_clientes[cpf][4])
    print("Profissao:",lista_clientes[cpf][5])
  print("==========================================")

def gerar_relatorio_emprestimos_ativos():
  verificar_arquivo("db_emprestimos.txt")
  arquivo = open("db_emprestimos.txt",'rb')
  lista_emprestimos_ativos = pickle.load(arquivo)
  arquivo.close()
  for cpf in lista_emprestimos_ativos:
    print("="*32)
    print("CPF:",cpf)
    for veiculo in lista_emprestimos_ativos[cpf][0]:
      print("##",veiculo)
    print("Dias alugados:",lista_emprestimos_ativos[cpf][1])
    print("Foi pago?:",lista_emprestimos_ativos[cpf][3])
  print("==========================================")
def gerar_relatorio():
  sair='s'
  while sair.lower()=='s':
    print("==============================")
    print("=== RELATÓRIO DA LOCADORA ====")
    print("======== PyRent-a-Car ========")
    print("==============================")
    print("==============================")
    print("1. Dividas quitadas")
    print("2. Clientes")
    print("3. Veiculos")
    print("4. Emprestimos")
    opcao = input("Digite sua opção:")
    if opcao == '1':
      gerar_relatorio_dividas_quitadas()
    elif opcao == '2':
      gerar_relatorio_clientes()
    elif opcao == '3':
      gerar_relatorio_veiculos()
    elif opcao == '4':
      gerar_relatorio_emprestimos_ativos()
    else:
      print("Opção inválida!")
    sair = input("Quer continuar na sessão de relatórios(s/n):")
    

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
