import pickle
import os
import platform

def clear():
  if platform.system() == 'Linux':
    return os.system('clear')
  elif platform.system() == 'Windows':
    return os.system('cls')

def verificar_arquivo():
  try:
    arquivo = open("db_veiculos.txt", 'rb')
    arquivo.close()
  except:
    arquivo = open('db_veiculos.txt','wb')
    pickle.dump({}, arquivo)
    arquivo.close()


def gravar_veiculos(dados):
  arquivo = open("db_veiculos.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def pegar_veiculos():
  arquivo = open("db_veiculos.txt",'rb')
  veiculos = pickle.load(arquivo)
  arquivo.close()
  return veiculos

def menu():
  print("===MENU Veiculos===")
  print("1. CADASTRAR VEICULO")
  print("2. LISTAR VEICULOS")
  print("3. DELETAR VEICULO")
  print("4. ATUALIZAR VEICULOS")
  print("5. PROCURAR VEICULO")
  print("===================")
  opcao = input("DIGITE SUA OPÇÃO:")
  return opcao

def geral(): 
  sair = 'n'
  while sair == 'n':
    opcao = menu()
    clear()
    verificar_arquivo()
    if opcao == '1':
      veiculos = pegar_veiculos()
      print("Preencha as informações de cadastro:")
      placa = input("Digite a placa do veiculo:")
      if placa in veiculos:
        print("DESCULPE, MAS ESTE VEICULO JÁ ESTÁ CADASTRADO!")
        continue
      else:
        try:
          quantidade = int(input("Digite a quantidade veiculos disponíveis:"))
          marca = input("Digite a marca do veiculo:")
          modelo = input("Digite o modelo do veiculo:")
          ano = input("Digite o ano do veiculo:")
          diaria = float(input("Digite a diária do veiculo:"))
          multa = float(input("Digite a multa por atraso para este veiculo:"))
          veiculos[placa] = [quantidade, marca, modelo, ano, diaria, multa]
          gravar_veiculos(veiculos)
          print("== Veiculo cadastrado com sucesso !!")
        except:
          print("Desculpe, mas ocorreu algum problema!!")
        
    elif opcao == '2':
      veiculos = pegar_veiculos()
      if len(veiculos)>0:
        print("%-11s | %-30s | %-20s | %-25s | %-25s | %-25s | %-25s"%("Placa","Quantidade","Marca","Modelo","Ano","Valor da Diaria","Valor da Multa"))
        print('-'*12, '-'*32, '-'*22, '-'*26)
        for veiculo in veiculos:
          print()

          print("===")
          print("Placa:", veiculo)
          print("Quantidade:", veiculos[veiculo][0])
          print("Marca:", veiculos[veiculo][1])
          print("Modelo:", veiculos[veiculo][2])
          print("Ano:", veiculos[veiculo][3])
          print("Valor da Diaria:", veiculos[veiculo][4])
          print("Valor da Multa:", veiculos[veiculo][5])
          print("===")
          print()
      else:
        print("Não existe veiculos cadastrados!")
    elif opcao == '3':
      veiculos = pegar_veiculos()
      placa = input("Digite a placa do veiculo que quer deletar:")
      if placa in veiculos:
        del veiculos[placa]
        gravar_veiculos(veiculos)
        print("%s Deletada com sucesso!!"%placa)
      else:
        print("Desculpe, mas está placa não existe no sistema!!")
    elif opcao == '4':
      veiculos = pegar_veiculos()
      placa = input("Digite a placa do veiculo no qual você quer atualizar informações:")
      if placa in veiculos:
        print("%s Localizado!"%placa)
        print("=== Menu ===")
        print("1. Quantidade")
        print("2. Marca")
        print("3. Modelo")
        print("4. Ano")
        print("5. Valor da Diaria:")
        print("6. Valor da Multa")
        print()
        opcao = input("Digite sua opção:")
        clear()
        if opcao == '1':
          quantidade = int(input("Digite a nova quantidade de veiculos:"))
          veiculos[placa][0] = quantidade
          gravar_veiculos(veiculos)
          print("Quantidade Atualizada com sucesso!")
        elif opcao == '2':
          marca = input("Digite a nova marca do veiculo:") 
          veiculos[placa][1] = marca
          gravar_veiculos(veiculos)
          print("Marca Atualizada com sucesso!")
        elif opcao == '3':
          modelo = input("Digite o novo modelo do veiculo:")
          veiculos[placa][2] = modelo
          gravar_veiculos(veiculos)
          print("Modelo Atualizada com sucesso!")
        elif opcao == '4':
          ano = input("Digite o novo ano do veiculo:")
          veiculos[placa][3] = ano
          gravar_veiculos(veiculos)
          print("Ano Atualizado com sucesso!")
        elif opcao == '5':
          diaria = float(input("Digite o novo valor da diária do veiculo:"))
          veiculos[placa][4] = diaria
          gravar_veiculos(veiculos)
          print("Valor da Diária Atualizada com sucesso!")
        elif opcao == '6':
          multa = float(input("Digite o novo valor da multa do veiculo:"))
          veiculos[placa][5] = multa
          gravar_veiculos(veiculos)
          print("Valor da multa Atualizada com sucesso!")
        else:
          print("Respeite o menu!!")
      else:
        print("%s não foi localizado no sistema!"%placa)
    elif opcao == '5':
      veiculos = pegar_veiculos()
      placa = input("Digite a placa do veiculo:")
      if placa in veiculos:
        print()
        print("===")
        print("Placa:", placa)
        print("Quantidade:", veiculos[placa][0])
        print("Marca:", veiculos[placa][1])
        print("Modelo:", veiculos[placa][2])
        print("Ano:", veiculos[placa][3])
        print("Valor da Diaria:", veiculos[placa][4])
        print("Valor da Multa:", veiculos[placa][5])
        print("===")
        print()
      else:
        print("Veiculo não encontrado!")
    else:
      print("Respeite o menu!")
    sair = input("Quer sair da sessão (s/n) ?")
    sair = sair.lower()

  