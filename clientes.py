import pickle
import os
import platform

def clear():
  if platform.system() == 'Linux':
    return os.system('clear')
  elif platform.system() == 'Windows':
    return os.system('cls')

def serializar(dados):
  arquivo = open("db_clientes.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def deserializar():
  arquivo = open("db_clientes.txt",'rb')
  return pickle.load(arquivo)


def geral(): 
  sair = 'n'
  while sair == 'n':
    print("===MENU Veiculos===")
    print("1. CADASTRAR CLIENTE")
    print("2. LISTAR CLIENTES")
    print("3. DELETAR CLIENTE")
    print("4. ATUALIZAR CLIENTE")
    print("5. PROCURAR VEICULO")
    print("===================")
    opcao = input("DIGITE SUA OPÇÃO:")
    clear()
    if opcao == '1':
      clientes = deserializar()
      print("Preencha as informações de cadastro:")
      cpf = input("Digite o CPF do cliente:")
      if cpf in clientes:
        print("DESCULPE, MAS ESTE CLIENTE JÁ ESTÁ CADASTRADO!")
        continue
      else:
        try:
          nome_completo = input("Digite o nome completo do cliente:")
          rua = input("Digite a rua do cliente:")
          bairro = input("Digite o bairro do cliente:")
          idade = input("Digite a idade do cliente:")
          profissao = input("Digite a profissao do cliente:")
          email = input("Digite o email do cliente:")
          
          clientes[cpf] = [nome_completo, email, rua, bairro, idade, profissao]
          serializar(clientes)
          print("== Cliente cadastrado com sucesso !!")
        except:
          print("Desculpe, mas ocorreu algum problema!!")
        
    elif opcao == '2':
      clientes = deserializar()
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

    elif opcao == '3':
      clientes = deserializar()
      cpf = input("Digite o CPF do cliente que quer deletar:")
      if cpf in clientes:
        del clientes[cpf]
        serializar(clientes)
        print("%s Deletado com sucesso!!"%cpf)
      else:
        print("Desculpe, mas este CPF não existe no sistema!!")

    elif opcao == '4':
      clientes = deserializar()
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
          serializar(clientes)
          print("Nome completo Atualizado com sucesso!")
        elif opcao == '2':
          email = input("Digite o novo EMAIL do cliente:") 
          clientes[cpf][1] = email
          serializar(clientes)
          print("Email Atualizado com sucesso!")
        elif opcao == '3':
          rua = input("Digite a nova RUA do cliente:")
          clientes[cpf][2] = rua
          serializar(clientes)
          print("Rua Atualizada com sucesso!")
        elif opcao == '4':
          bairro = input("Digite o novo BAIRRO do cliente:")
          clientes[cpf][3] = bairro
          serializar(clientes)
          print("Bairro Atualizado com sucesso!")
        elif opcao == '5':
          idade = float(input("Digite a nova IDADE do cliente:"))
          clientes[cpf][4] = idade
          serializar(clientes)
          print("Idade Atualizada com sucesso!")
        elif opcao == '6':
          profissao = float(input("Digite a nova PROFISSÃO do cliente:"))
          clientes[cpf][5] = profissao
          serializar(clientes)
          print("Profissão Atualizado com sucesso!")
        else:
          print("Respeite o menu!!")
      else:
        print("%s não foi localizado no sistema!"%cpf)
    elif opcao == '5':
      clientes = deserializar()
      cpf = input("Digite o CPF do cliente:")
      if cpf in clientes:
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
      print("Respeite o menu!")
    sair = input("Quer sair da sessão (s/n) ?")
    sair = sair.lower()
  