import emprestimos_metodos  as EM
import clientes_metodos as CM
import veiculos_metodos as VM 
import view.menu
import config.operacoes_SO
print(view.menu.inicial())
opcaoAdmin = input('ESCOLHA UMA OPÇÃO:')
if opcaoAdmin == '1':
  config.operacoes_SO.usando_clear()
  print(view.menu.view_clientes())
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


