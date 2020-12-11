import pickle
import os
import platform
from arquivos_gerais import verificar_arquivo, gravar_clientes, pegar_clientes
from limpa_tela import clear

def cadastrar_clientes(clientes):
  continuar = 's'
  while continuar.lower()=='s':
    try:
      print("Preencha as informações de cadastro:")
      cpf = input("Digite o CPF do cliente:")
      if cpf in clientes:
        print("DESCULPE, MAS ESTE CLIENTE JÁ ESTÁ CADASTRADO!")
        continue
      else:
        nome_completo = input("Digite o nome completo do cliente:")
        rua = input("Digite a rua do cliente:")
        bairro = input("Digite o bairro do cliente:")
        idade = input("Digite a idade do cliente:")
        profissao = input("Digite a profissao do cliente:")
        email = input("Digite o email do cliente:")
        
        clientes[cpf] = [nome_completo, email, rua, bairro, idade, profissao]
        gravar_clientes(clientes)
        print("== Cliente cadastrado com sucesso !!")
        continuar = input("Quer continuar na sessão de cadastrar cliente?(s/n):")
    except:
      print("Ocorreu algum problema enquanto estava sendo cadastrado o cliente!")
      print("Cliente não cadastrado!")
      continuar = input("Quer continuar na sessão de cadastrar cliente?(s/n):")  

def listar_clientes(clientes):
  if len(clientes)>0:
    for cliente in clientes:
      print()
      print("===")
      print("Placa:", cliente)
      print("Nome Completo:", clientes[cliente][0])
      print("Email:", clientes[cliente][1])
      print("Rua:", clientes[cliente][2])
      print("Bairro:", clientes[cliente][3])
      print("Idade:", clientes[cliente][4])
      print("Profissão:", clientes[cliente][5])
      print("===")
      print()
  else:
    print("Não existe cliente no sistema!!")

def deletar_cliente(clientes):
  continuar = 's'
  while continuar.lower() == 's':
    cpf = input("Digite o CPF do cliente que quer deletar:")
    if cpf in clientes:
      del clientes[cpf]
      gravar_clientes(clientes)
      print("%s Deletado com sucesso!!"%cpf)
    else:
      print("Desculpe, mas este CPF não existe no sistema!!")
    continuar = input("Quer continuar na sessão de deletar cliente?(s/n):")
def atualizar_cliente(clientes):
  continuar = 's'
  while continuar.lower() == 's':
    try:
      cpf = input("Digite o CPF do cliente no qual você quer atualizar informações:")
      if cpf in clientes:
        print("%s Localizado!"%cpf)
        print("=== Menu ===")
        print("1. Nome Completo")
        print("2. Email")
        print("3. Rua")
        print("4. Bairro")
        print("5. Idade:")
        print("6. Profissão")
        print()
        opcao = input("Digite sua opção:")
        clear()
        if opcao == '1':
          nome_completo = int(input("Digite o novo nome completo do cliente:"))
          clientes[cpf][0] = nome_completo
          gravar_clientes(clientes)
          print("Nome completo Atualizado com sucesso!")
        elif opcao == '2':
          email = input("Digite o novo EMAIL do cliente:") 
          clientes[cpf][1] = email
          gravar_clientes(clientes)
          print("Email Atualizado com sucesso!")
        elif opcao == '3':
          rua = input("Digite a nova RUA do cliente:")
          clientes[cpf][2] = rua
          gravar_clientes(clientes)
          print("Rua Atualizada com sucesso!")
        elif opcao == '4':
          bairro = input("Digite o novo BAIRRO do cliente:")
          clientes[cpf][3] = bairro
          gravar_clientes(clientes)
          print("Bairro Atualizado com sucesso!")
        elif opcao == '5':
          idade = float(input("Digite a nova IDADE do cliente:"))
          clientes[cpf][4] = idade
          gravar_clientes(clientes)
          print("Idade Atualizada com sucesso!")
        elif opcao == '6':
          profissao = float(input("Digite a nova PROFISSÃO do cliente:"))
          clientes[cpf][5] = profissao
          gravar_clientes(clientes)
          print("Profissão Atualizado com sucesso!")
        else:
          print("Respeite o menu!!")
      else:
        print("%s não foi localizado no sistema!"%cpf)
      continuar = input("Quer continuar na sessão de atualizar cliente?(s/n):")
    except:
      print()
      print("Ocorreu algum problema enquanto estava atualizando os dados:")
      print("Cliente não atualizado!")
      print()
      continuar = input("Quer continuar na sessão de atualizar cliente?(s/n):")
def procurar_cliente_especifico(clientes):
  continuar = 's'
  while continuar.lower() == 's':
    cpf = input("Digite o CPF do cliente:")
    if cpf in clientes:
      print("Cliente Encotrado:")
      print()
      print("===")
      print("Cpf:", cpf)
      print("Nome Completo:", clientes[cpf][0])
      print("Email:", clientes[cpf][1])
      print("Rua:", clientes[cpf][2])
      print("Bairro:", clientes[cpf][3])
      print("Idade:", clientes[cpf][4])
      print("Profissão:", clientes[cpf][5])
      print("===")
      print()
    else:
      print("Cliente não encontrado")
    continuar = input("Quer continuar na sessão de procurar cliente específico?(s/n):")

def geral(): 
  clientes = pegar_clientes()
  sair = 'n'
  while sair.lower() == 'n':
    print("===MENU Veiculos===")
    print("1. CADASTRAR CLIENTE")
    print("2. LISTAR CLIENTES")
    print("3. DELETAR CLIENTE")
    print("4. ATUALIZAR CLIENTE")
    print("5. PROCURAR CLIENTE")
    print("===================")
    
    opcao = input("DIGITE SUA OPÇÃO:")
    clear()
    verificar_arquivo("db_clientes.txt")
    if opcao == '1':
     cadastrar_clientes(clientes)
    elif opcao == '2':
      listar_clientes(clientes)
    elif opcao == '3':
      deletar_cliente(clientes)

    elif opcao == '4':
      atualizar_cliente(clientes)
      
    elif opcao == '5':
      procurar_cliente_especifico(clientes)
    else:
      print("Respeite o menu!")
    print()
    sair = input("Quer sair da sessão cliente? (s/n)")
  