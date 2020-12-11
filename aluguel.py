import pickle
import os
import platform
from arquivos_gerais import pegar_emprestimos,verificar_arquivo,pegar_clientes, pegar_veiculos, gravar_emprestimos, gravar_veiculos
from limpa_tela import clear
from datetime import datetime, timedelta
def cadastrar_emprestimo(emprestimos, clientes, veiculos):
  continuar = 's'
  while continuar.lower()=='s':
    try:
      print("Preencha as informações de cadastro:")
      cpf_cliente = input("Digite o cpf do cliente:")
      if not(cpf_cliente in clientes):
        print("Desculpe, mas este cliente não foi cadastrado!")
        print()
        continuar = input("Quer continuar na sessão cadastrar emprestimo?(s/n)")
        continue
      aluguel_de_veiculos = []
      num_veiculos_escolha = int(input("Quantos veiculos o cliente quer alugar?:"))
      cont = 0
      while cont<num_veiculos_escolha:
        placa_veiculo = input("Digite a placa do veiculo a ser alugado:")
        if not(placa_veiculo in veiculos):
          print("Desculpe, mas este veiculo não foi cadastrado!")
          print()
          continuar = input("Quer continuar na sessão cadastrar emprestimo?(s/n)")
          continue
        aluguel_de_veiculos.append(placa_veiculo)
        veiculos[placa_veiculo][0]-=1
        cont+=1
      dias_uso = int(input("Digite quantos dias o cliente vai ficar com o veiculo:"))
      data_vencimento = datetime.now() + timedelta(days=dias_uso)
      
      Esta_vencido = False
      print("O cliente vai pagar agora(1) ou depois(2):")
      escolha_pagar = input("Digite sua opção:")
      if escolha_pagar == '1':
        foi_pago = True
      elif escolha_pagar == '2':
        foi_pago = False
      else:
        print("Respeite o menu!")
        continuar = input("Quer continuar na sessão cadastrar emprestimo?(s/n)")
        continue
      #emprestimos[cpf_cliente] = [aluguel_de_veiculos, dias_uso, Esta_vencido, foi_pago]
      emprestimos[cpf_cliente] = [aluguel_de_veiculos, dias_uso, Esta_vencido, foi_pago, data_vencimento]
      gravar_veiculos(veiculos)
      gravar_emprestimos(emprestimos)
      print("Aluguel cadastrado com sucesso!")
      print()
      continuar = input("Quer continuar na sessão cadastrar emprestimo?(s/n)")
    except:
      print()
      print("Ocorreu algum erro quando você foi preencher o documento!!")
      print("Emprestimo não cadastrado!")
      print()
      continuar = input("Quer continuar na sessão cadastrar emprestimo?(s/n)")

def procurar_emprestimo(emprestimos):
  continuar = 's'
  while continuar.lower() == 's':
    cpf_cliente = input("Digite o CPF do cliente deste Aluguel:")
    if cpf_cliente in emprestimos:
      print()
      print("===")
      print("Cpf do cliente",cpf_cliente)
      print("Veiculos Alugados")
      print("====")
      for veiculo in emprestimos[cpf_cliente][0]:
        print(veiculo)
        print("====")
      print()
      print("Dias de uso :",emprestimos[cpf_cliente][1])
      print("Está vencido?:",emprestimos[cpf_cliente][2])
      print("Foi Pago?:",emprestimos[cpf_cliente][3])

      print("===")
      print()
    else:
      print("Emprestimo não encontrado!")
    continuar = input("Quer contiuar na sessão procurar emprestimo?(s/n)")

def deletar_emprestimo(emprestimos):
  continuar = 's'
  while continuar.lower()=='s':
    cpf_cliente = input("Digite o CPF do cliente deste Aluguel:")
    if cpf_cliente in emprestimos:
      del emprestimos[cpf_cliente]
      gravar_emprestimos(emprestimos)
    else:
      print("Emprestimo não cadastrado no sistema!")
    print()
    continuar = input("Quer continuar na sessão deletar emprestimo?(s/n)")
    
def atualizar_emprestimo(emprestimos):
  continuar = 's'
  while continuar.lower()=='s':
    try:
      cpf_cliente = input("Digite o CPF do cliente:")
      if cpf_cliente in emprestimos:
        print("%s Localizado!"%cpf_cliente)
        print("=== Menu ===")
        print("1. Dias de Uso")
        print("2. Está vencido")
        print()
        opcao = input("Digite sua opção:")
        clear()
        if opcao == '1':
          dias_uso = int(input("Digite os novos dias de uso:"))
          emprestimos[cpf_cliente][1]=dias_uso
          print("Dias de uso atualizado com sucesso!")
        elif opcao == '2':
          emprestimos[cpf_cliente][2] = not(emprestimos[cpf_cliente][2])
          print("Está vencido atualizado com sucesso para %s!"%str(emprestimos[cpf_cliente][2]))
        else:
          print("Respeite o menu!!")
      else:
        print("%s não foi localizado no sistema!"%cpf_cliente)
        print()
        continuar = input("Quer continuar na sessão atualizar emprestimo?(s/n)")
    except:
      print()
      print("Ocorreu algum problema enquanto estava tentando atualizar os dados:")
      print("Emprestimo não atualizado!")
      print()
      continuar = input("Quer continuar na sessão atualizar emprestimo?(s/n)")
def geral():
  emprestimos = pegar_emprestimos()
  clientes = pegar_clientes()
  veiculos = pegar_veiculos()
  continuar = 's'
  while continuar.lower() =='s':
    print("===MENU Veiculos===")
    print("1. CADASTRAR EMPRESTIMO")
    print("2. PROCURAR EMPRESTIMO")
    print("3. DELETAR EMPRESTIMO")
    print("4. ATUALIZAR EMPRESTIMO")
    print("===================")
    opcao = input("DIGITE SUA OPÇÃO:")
    clear()
    if opcao == '1':
      cadastrar_emprestimo(emprestimos, clientes, veiculos)
    elif opcao == '2':
      procurar_emprestimo(emprestimos)
    elif opcao == '3':
      deletar_emprestimo(emprestimos)
    elif opcao == '4':
      atualizar_emprestimo(emprestimos)
    print()
    continuar = input("Quer continuar na sessão de emprestimos?(s/n):")
        