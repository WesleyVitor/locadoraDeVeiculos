import ast
from clientes_metodos import pegaClientes
import veiculos_metodos as VS

emprestimoModel ="models/emprestimos.txt"


def escreverNoArquivo(dado):
  global emprestimoModel
  arquivo = open(emprestimoModel,'w')
  arquivo.write(str(dado))
  arquivo.close()
  return arquivo

#Verifica se existe os dados corretos em outros arquivos
def possoCadastrar(cliente, veiculo, quantidade):
  if cliente in pegaClientes():
    if veiculo in VS.pega_veiculos():
      veiculos = VS.pega_veiculos()
      if veiculos[veiculo]>=quantidade:
        return True
  return False

def pega_emprestimos():
  return ast.literal_eval(leia_emprestimos())
#-----------------------------------------------------------------

#INDEX 
def leia_emprestimos():
  global emprestimoModel
  emprestimos = open(emprestimoModel)
  return emprestimos.read()

#Create
def cadastrar_emprestimo(cliente, veiculo, quantidade, tempo, valorPorHora, foiPago):
  if possoCadastrar(cliente, veiculo, quantidade):
    emprestimo = pega_emprestimos()
    emprestimo[cliente] = {
      "veiculo":veiculo,
      "quantidade":quantidade,
      "totalAPagar":tempo*valorPorHora,
      "foiPago":foiPago,
    
    }
    escreverNoArquivo(emprestimo)
    VS.update_quantidade_veiculo(veiculo, 'decrementar')
    ###### Escrever no dicionario relatorio 
    return None
  else:
    return -1
#Delete
def deletar_emprestimo(cliente):
  emprestimos = pega_emprestimos()
  if cliente in emprestimos:
    if emprestimos[cliente]['foiPago']:
      del emprestimos[cliente]
      return None
  return -1

#SHOW
#Método para encontrar um emprestimo único
#Método para atualizar o "atributo" foi pago 
# Se chamar este método, apagar o emprestimo
