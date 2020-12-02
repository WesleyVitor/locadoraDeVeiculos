import clientes_metodos as CM  

def geral(opcao):
  if opcao == '1':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM NOVO USUÁRIO NÃO EXISTENTE===")
      nome = input("DIGITE O NOME DO CLIENTE:")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = CM.cadastrar_clientes(cpf, nome)
      if retorno != -1:
        print("USUÁRIO CADASTRADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS JÁ EXISTE ESSE USUÁRIO NO SISTEMA!!")
      sair = input("===ADICINAR NOVAMENTE?(S - N)")
    return None
  elif opcao == '2':
    print("===AQUI VOCÊ PODERÁ LISTAR TODOS OS CLIENTES EXISTENTES NO SISTEMA===")
    clientes = CM.pegaClientes()
    print(clientes)
    for cpf in clientes:
      print()
      print(""" 
        Nome: %s
        CPF: %s
       """%(clientes[cpf], cpf))
      print()
    return None
  elif opcao == '3':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS CLIENTES EXISTENTES NO SISTEMA===")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = CM.deleteCliente(cpf)
      if retorno != -1:
        print("USUÁRIO APAGADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS O USUPARIO NÃO EXISTE NO SISTEMA !!")
      sair = input("===APAGAR NOVAMENTE?(S - N)")
    return None
  elif opcao == '4':
    sair = 'S'
    while sair.upper()!='N':
      print("===AQUI VOCÊ PODERÁ LISTAR O CLIENTE EXISTENTES NO SISTEMA===")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      cliente = CM.showCliente(cpf)
      if cliente != -1:
        print(""" 
        NOME: %s
        """%(cliente))
      else:
        print("DESCULPE, MAS O USUPARIO NÃO EXISTE NO SISTEMA !!")
      sair = input("===ACESSAR OUTRO?(S - N)===")
    return None
  else:
    print("RESPEITE O MENU!!")
    return -1
