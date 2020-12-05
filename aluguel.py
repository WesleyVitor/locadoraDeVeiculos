import pickle
import os
import platform

def clear():
  if platform.system() == 'Linux':
    return os.system('clear')
  elif platform.system() == 'Windows':
    return os.system('cls')
def deserializar_emprestimos():
  arquivo = open("db_emprestimos.txt",'rb')
  return pickle.load(arquivo)
def deserializar_clientes():
  arquivo = open("db_clientes.txt",'rb')
  return pickle.load(arquivo)
def deserializar_veiculos():
  arquivo = open("db_veiculos.txt",'rb')
  return pickle.load(arquivo)
def serializar(dados):
  arquivo = open("db_emprestimos.txt",'wb')
  pickle.dump(dados, arquivo)
def serializar_veiculo(dados):
  arquivo = open("db_veiculos.txt",'wb')
  pickle.dump(dados, arquivo)

def geral():
  emprestimos = deserializar_emprestimos()
  clientes = deserializar_clientes()
  veiculos = deserializar_veiculos()
  sair = 'n'
  while sair =='n':
    print("===MENU Veiculos===")
    print("1. CADASTRAR EMPRESTIMO")
    print("2. PROCURAR EMPRESTIMO")
    print("3. DELETAR EMPRESTIMO")
    print("4. ATUALIZAR EMPRESTIMO")
    print("===================")
    opcao = input("DIGITE SUA OPÇÃO:")
    clear()
    if opcao == '1':
      print("Preencha as informações de cadastro:")
      cpf_cliente = input("Digite o cpf do cliente:")
      if not(cpf_cliente in clientes):
        print("Desculpe, mas este cliente não foi cadastrado!")
        continue
      
      #SESSÃO PARA ALUGAR MAIS DE 1 VEICULO
      aluguel_de_veiculos = []
      num_veiculos_escolha = int(input("Quantos veiculos o cliente quer alugar?:"))
      cont = 0
      while cont<num_veiculos_escolha:
        placa_veiculo = input("Digite a placa do veiculo a ser alugado:")
        if not(placa_veiculo in veiculos):
          print("Desculpe, mas este veiculo não foi cadastrado!")
          continue
        aluguel_de_veiculos.append(placa_veiculo)
        veiculos[placa_veiculo][0]+=1
        cont+=1
      dias_uso = int(input("Digite quantos dias o cliente vai ficar com o veiculo:"))
      Esta_vencido = False
      print("O cliente vai pagar agora(1) ou depois(2):")
      escolha_pagar = input("Digite sua opção:")
      if escolha_pagar == '1':
        foi_pago = True
      elif escolha_pagar == '2':
        foi_pago = False
      else:
        print("Respeite o menu!")
        continue
      emprestimos[cpf_cliente] = [aluguel_de_veiculos, dias_uso, Esta_vencido, foi_pago]
      serializar_veiculo(veiculos)
      serializar(emprestimos)
      print("Aluguel cadastrado com sucesso!")
    elif opcao == '2':
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
        print("Veiculo não encontrado!")
    elif opcao == '3':
      cpf_cliente = input("Digite o CPF do cliente deste Aluguel:")
      if cpf_cliente in emprestimos:
        del emprestimos[cpf_cliente]
        serializar(emprestimos)
      else:
        print("Emprestimo não cadastrado no sistema!")

    elif opcao == '4':
      cpf_cliente = input("Digite o CPF do cliente:")
      if cpf_cliente in emprestimos:
        
        print("%s Localizado!"%cpf_cliente)
        print("=== Menu ===")
        
        print("1. Dia do vencimento")
        print("2. Mês do vencimento")
        print("3. Está vencido")
        print()
        opcao = input("Digite sua opção:")
        clear()
        if opcao == '1':
          dia_vencimento = int(input("Digite o novo dia do vencimento:"))
          emprestimos[cpf_cliente][1]=dia_vencimento
          print("Dia do vencimento atualizado com sucesso!")
        elif opcao == '2':
          mes_vencimento = int(input("Digite o novo mês do vencimento:"))
          emprestimos[cpf_cliente][2] = mes_vencimento
          print("Mês do vencimento atualizado com sucesso!")
        elif opcao == '3':
          Esta_vencido = input("O aluguel está vencido(s/n)?:")
          emprestimos[cpf_cliente][3] = not(emprestimos[cpf_cliente][3])
          print("Está vencido atualizado com sucesso!")
        else:
          print("Respeite o menu!!")
      else:
        print("%s não foi localizado no sistema!"%cpf_cliente)
        
