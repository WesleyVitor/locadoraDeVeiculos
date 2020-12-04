import cliente_service
import veiculos_service
import pickle
emprestimoModel ="models/emprestimos.p"
#Verifica se existe os dados corretos em outros arquivos
def possoCadastrar(cliente, veiculo, quantidade):
  if cliente in cliente_service.deserializar():
    if veiculo in veiculos_service.deserializar():
      veiculos = veiculos_service.deserializar()
      if veiculos[veiculo]>=quantidade:
        return True
  return False
#INDEX 
def deserializar():
  global emprestimoModel
  emprestimos = open(emprestimoModel, 'rb')
  return pickle.load(emprestimos)
def serializar(dado):
  global emprestimoModel
  arquivo = open(emprestimoModel,'wb')
  pickle.dump(dado, arquivo)
  arquivo.close()
  return None
#Atualiza a quantidade de veiculos depois do emprestimo
def update_quantidade_veiculo(nome, opc):
  veiculos = veiculos_service.deserializar()
  if opc == 'incrementar':
    veiculos[nome] = veiculos[nome]+1
  elif opc == 'decrementar':
    veiculos[nome] = veiculos[nome]-1
  veiculos_service.serializar(veiculos)
#Create
def cadastrar_emprestimo(cliente, veiculo, quantidade, tempo, foi_pago):
  clientes = cliente_service.deserializar()
  veiculos = veiculos_service.deserializar()

  if (cliente in clientes) and (veiculo in veiculos) and (veiculos[veiculo][1]>=quantidade):
    emprestimos = deserializar()
    total_a_pagar = veiculos[veiculo][2] * tempo
    emprestimos[cliente] = [veiculo, quantidade, total_a_pagar, foi_pago  ]
    serializar(emprestimos)
    update_quantidade_veiculo(veiculo, 'decrementar')
    ###### Escrever no dicionario relatorio 
    return None
  else:
    return -1
#Delete
def deletar_emprestimo(cliente):
  emprestimos = deserializar()
  if cliente in emprestimos:
    if emprestimos[cliente][3]:
      del emprestimos[cliente]
      return None
  return -1
def geral(opcao):
  if opcao == '1':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ CADASTRAR UM EMPRESTIMO ===")
      cpf_cliente = input("DIGITE O CPF DO CLIENTE:")
      nome_veiculo = input("DIGITE O NOME DO VEICULO:")
      quantidade_de_veiculos = int(input("DIGITE A QUANTIDADE DE VEICULOS:"))
      tempo_uso = float(input("DIGITE QUANTAS HORAS O CLIENTE VAI FICAR USANDO O VEICULO:"))
      print("O USUÁRIO VAI PAGAR AGORA OU DEPOIS?")
      pagamento = input("(1)AGORA ==== (2)DEPOIS")
      if pagamento == '1':
        pagamento = True
        retorno = cadastrar_emprestimo(cpf_cliente, nome_veiculo, quantidade_de_veiculos, tempo_uso,pagamento)
        if retorno != -1:
          print("EMPRESTIMO CADASTRADO COM SUCESSO!!") 
        else:
          print("DESCULPE, MAS ALGUMA COISA DEU ERRADO")
          print("PORFAVOR VERIFIQUE SE EXISTE UM VEICULO NESTE NOME, OU SE TEM QUANTIDADE SUFICIENTE PARA ATENDER O CLIENTE OU SE ESTE CLIENTE JÁ ESTÁ CADASTRADO NO SISTEMA")
      elif pagamento == '2':
        pagamento = False
        retorno = cadastrar_emprestimo(cpf_cliente, nome_veiculo, quantidade_de_veiculos, tempo_uso, pagamento)
        if retorno != -1:
          print("EMPRESTIMO CADASTRADO COM SUCESSO!!") 
        else:
          print("DESCULPE, MAS ALGUMA COISA DEU ERRADO")
          print("PORFAVOR VERIFIQUE SE EXISTE UM VEICULO NESTE NOME,\n OU SE TEM QUANTIDADE SUFICIENTE PARA ATENDER O CLIENTE OU\n SE ESTE CLIENTE JÁ ESTÁ CADASTRADO NO SISTEMA")
      else:
        print("RESPEITE O MENU!!!")
      print()
      sair = input("===SAIR DA SESSÃO DE CADASTRO ?(S - N)")
    return None
  elif opcao == '2':
    sair = 'N'
    while sair=='N':
      print("===AQUI VOCÊ PODERÁ APAGAR OS EMPRESTIMOS EXISTENTES NO SISTEMA===")
      cpf = input("DIGITE O CPF DO CLIENTE CORRESPONDENTE:")
      retorno = deletar_emprestimo(cpf)
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
