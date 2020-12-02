import view.menu
import config.operacoes_SO
import cliente_service 
while True:
  print(view.menu.inicial())
  opcaoAdmin = input('ESCOLHA UMA OPÇÃO:')
  if opcaoAdmin == '1':
    sairCliente = 'N'
    while sairCliente.upper()=='N':
      config.operacoes_SO.usando_clear()
      sairCadastro = 'N'
      print(view.menu.view_clientes())
      opcao = input("===DIGITE SUA OPÇÃO===")
      cliente_service.geral(opcao)
      print()
      sairCliente = input("===QUE SAIR DA SESSÃO CLIENTE ?(S - N)")


  elif opcaoAdmin == '2':
    config.operacoes_SO.usando_clear()
    print(view.menu.view_veiculos())
  elif opcaoAdmin == '3':
    config.operacoes_SO.usando_clear()
    print(view.menu.view_emprestimos())
  else:
    print("RESPEITE O MENU!!")


# CS.cadastrarClientes('122','Jose')
# VS.cadastrar_veiculos('Chevrolet',30)
# ES.cadastrar_emprestimo('122','Chevrolet',1,4,100,False)


