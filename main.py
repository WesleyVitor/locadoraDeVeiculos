import view.menu
import config.operacoes_SO
import cliente_service 
import veiculos_service
import emprestimos_service
while True:
  print(view.menu.inicial())
  opcaoAdmin = input('ESCOLHA UMA OPÇÃO:')
  if opcaoAdmin == '1':
    sairCliente = 'N'
    while sairCliente.upper()=='N':
      config.operacoes_SO.usando_clear()
      #sairCadastro = 'N'
      print(view.menu.view_clientes())
      opcao = input("===DIGITE SUA OPÇÃO===")
      #
      cliente_service.geral(opcao)
      #
      print()
      sairCliente = input("===QUE SAIR DA SESSÃO CLIENTE ?(S - N)")

  elif opcaoAdmin == '2':
    sair_veiculo = 'N'
    while sair_veiculo.upper()=='N':
      config.operacoes_SO.usando_clear()
      #sairCadastro = 'N'
      print(view.menu.view_veiculos())
      opcao = input("===DIGITE SUA OPÇÃO===")
      #
      veiculos_service.geral(opcao)
      #
      print()
      sair_veiculo = input("===QUE SAIR DA SESSÃO VEICULOS ?(S - N)")

  elif opcaoAdmin == '3':
    sair_emprestimo = 'N'
    while sair_emprestimo.upper()=='N':
      config.operacoes_SO.usando_clear()
      print(view.menu.view_emprestimos())
      
      opcao = input("===DIGITE SUA OPÇÃO===")
      #
      emprestimos_service.geral(opcao)
      #
      print()
      sair_emprestimo = input("===QUE SAIR DA SESSÃO EMPRESTIMOS ?(S - N)")
    
  else:
    print("RESPEITE O MENU!!")


