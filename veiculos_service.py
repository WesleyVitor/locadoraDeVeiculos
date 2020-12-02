import veiculos_metodos as CV 

def geral(opcao):
  if opcao == '1':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM NOVO VEICULO NÃO EXISTENTE===")
      nome = input("DIGITE O NOME DO VEICULO:")
      quantidade = input("DIGITE A QUANTIDADE DO VEICULO CORRESPONDENTE:")
      retorno = CV.cadastrar_veiculos(nome, quantidade)
      if retorno != -1:
        print("VEICULO CADASTRADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS JÁ EXISTE ESSE VEICULO NO SISTEMA!!")
      sair = input("===ADICINAR NOVAMENTE?(S - N):")
    return None
  elif opcao == '2':
    print("===AQUI VOCÊ PODERÁ LISTAR TODOS OS VEICULOS EXISTENTES NO SISTEMA===")
    veiculos = CV.pega_veiculos()
    
    for nome in veiculos:
      print()
      print(""" 
        Nome: %s
        Quantidade: %s
       """%(nome, veiculos[nome]))
      print()
    return None
  elif opcao == '3':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS VEICULOS EXISTENTES NO SISTEMA===")
      nome = input("DIGITE O NOME DO VEICULO CORRESPONDENTE:")
      retorno = CV.delete_veiculos(nome)
      if retorno != -1:
        print("VEICULO APAGADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS O VEICULO NÃO EXISTE NO SISTEMA !!")
      sair = input("===APAGAR NOVAMENTE?(S - N):")
    return None
  elif opcao == '4':
    sair = 'S'
    while sair.upper()!='N':
      print("===AQUI VOCÊ PODERÁ LISTAR O VEICULO EXISTENTES NO SISTEMA===")
      nome = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      veiculos = CV.show_veiculos(nome)
      if veiculos != -1:
        print(""" 
        NOME: %s
        """%(veiculos))
      else:
        print("DESCULPE, MAS O VEICULO NÃO EXISTE NO SISTEMA !!")
      sair = input("===ACESSAR OUTRO?(S - N)===")
    return None
  else:
    print("RESPEITE O MENU!!")
    return -1
