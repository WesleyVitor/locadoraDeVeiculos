import emprestimos_metodos as EM  

def geral(opcao):
  if opcao == '1':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM EMPRESTIMO ===")
      cpf_cliente = input("DIGITE O CPF DO CLIENTE:")
      veiculo = input("DIGITE O NOME DO VEICULO:")
      quantidade_de_veiculos = int(input("DIGITE A QUANTIDADE DE VEICULOS:"))
      tempo = float(input("DIGITE QUANTAS HORAS O CLIENTE VAI FICAR USANDO O VEICULO:"))
      valorPorHora = float(input("DIGITE O PREÇO POR HORA PARA ESTE VEICULO"))
      print("O USUÁRIO VAI PAGAR AGORA OU DEPOIS?")
      pagamento = input("(1)AGORA ==== (2)DEPOIS")
      if pagamento == '1':
        pagamento = True
        retorno = EM.cadastrar_emprestimo(cpf_cliente, veiculo, quantidade_de_veiculos, tempo, valorPorHora, pagamento)
        if retorno != -1:
          print("USUÁRIO CADASTRADO COM SUCESSO!!") 
        else:
          print("DESCULPE, MAS JÁ NÃO EXISTE ESSE USUÁRIO NO SISTEMA!!")
      elif pagamento == '2':
        pagamento = False
        retorno = EM.cadastrar_emprestimo(cpf_cliente, veiculo, quantidade_de_veiculos, tempo, valorPorHora, pagamento)
        if retorno != -1:
          print("EMPRESTIMO CADASTRADO COM SUCESSO!!") 
        else:
          print("DESCULPE, MAS NÃO EXISTE ESSE USUÁRIO NO SISTEMA!!")
      else:
        print("RESPEITE O MENU!!!")
      
      sair = input("===SAIR DA SESSÃO DE CADASTRO ?(S - N)")
    return None
  elif opcao == '2':
    print("===AQUI VOCÊ PODERÁ LISTAR TODOS OS EMPRESTIMOS EXISTENTES NO SISTEMA===")
    emprestimos = EM.pega_emprestimos()
    
    for cpf_cliente in emprestimos:
      print()
      
      print(""" 
        CPF Do cliente: %s
        Veiculo: %s
        Quantidade: %d
        Total A Pagar: %.2f
        Foi pago? : %s

       """%(cpf_cliente,emprestimos[cpf_cliente]['veiculo'], emprestimos[cpf_cliente]['quantidade'],emprestimos[cpf_cliente]['totalAPagar'], str(emprestimos[cpf_cliente]['foiPago']) ))
      print()
    return None
  elif opcao == '3':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS EMPRESTIMOS EXISTENTES NO SISTEMA===")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = EM.deletar_emprestimo(cpf)
      if retorno != -1:
        print("USUÁRIO APAGADO COM SUCESSO!!") 
      else:
        print("DESCULPE, MAS VOCÊ NÃO PODE APAGAR ESTE EMPRÉSTIMO !!")
        print("POSSÍVEIS CAUSAS:")
        print("1 - EMPRESTIMO NÃO EXISTE NO SISTEMA")
        print("2 - EMPRESTIMO NÃO PAGO")
      sair = input("===APAGAR NOVAMENTE?(S - N)")
    return None
  
  else:
    print("RESPEITE O MENU!!")
    return -1
