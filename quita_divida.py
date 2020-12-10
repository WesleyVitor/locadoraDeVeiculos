
import random
import pickle

def verificar_arquivo(nome_arquivo):
  try:
    arquivo = open(nome_arquivo, 'rb')
    arquivo.close()
  except:
    arquivo = open(nome_arquivo,'wb')
    pickle.dump({}, arquivo)
    arquivo.close()

def deserializar_emprestimos():
  verificar_arquivo("db_emprestimos.txt")
  arquivo = open("db_emprestimos.txt",'rb')
  return pickle.load(arquivo)
def deserializar_veiculos():
  verificar_arquivo("db_veiculos.txt")
  arquivo = open("db_veiculos.txt",'rb')
  return pickle.load(arquivo)
def deserializar_quita_divida():
  verificar_arquivo("db_quita_dividas.txt")
  arquivo = open("db_quita_dividas.txt",'rb')
  return pickle.load(arquivo)
def serializar_quita_divida(dados):
  verificar_arquivo("db_quita_dividas.txt")
  arquivo = open("db_quita_dividas.txt",'wb')
  pickle.dump(dados, arquivo)
  arquivo.close()

def geral():
  
  sair = 'n'
  while sair == 'n':
    emprestimos = deserializar_emprestimos()
    veiculos = deserializar_veiculos()
    quita_divida = deserializar_quita_divida()
    pagar = 0
    multa = 0
    cpf_cliente = input("Digite o cpf do cliente associado ao emprestimo:")
    
    if not(cpf_cliente in emprestimos):
      print("Não foi encontrado emprestimo associado a este CPF")
      continue
    #[aluguel_de_veiculos, dias_uso, Esta_vencido, foi_pago]
    print()
    print("===")
    print("Cpf do cliente",cpf_cliente)
    print("Veiculos Alugados")
    print("====")
    for placa_veiculo in emprestimos[cpf_cliente][0]:
      print(placa_veiculo)
      
      print("====")
    print()
    print("Dias de uso :",emprestimos[cpf_cliente][1])
    print("Está vencido?:",emprestimos[cpf_cliente][2])
    print("Foi Pago?:",emprestimos[cpf_cliente][3])
    print("===")
    print()
    dias_atraso = int(input("Digite quantos dias foi atrasado até a entrega:"))  
    for placa_veiculo in emprestimos[cpf_cliente][0]:
      pagar += emprestimos[cpf_cliente][1]*veiculos[placa_veiculo][4]
      multa += dias_atraso * veiculos[placa_veiculo][5]
    total_para_pagar = pagar + multa
    print()
    print("==PAGAMENTO==")
    print()
    print("TOTAL A PAGAR:%.2f"%total_para_pagar)
    print("VALOR DE MULTA:%.2f"%multa)
    print()
    if emprestimos[cpf_cliente][3] == False:
      print("VOCÊ QUER PAGAR(s/n) ?")
      opcao = input("Digite sua opção:")
      if opcao.lower() == 's':
        confirmar = input("Cliente pagou(s/n)?")
        if confirmar.lower() == 's':
          emprestimos[cpf_cliente][3] = True
          emprestimos[cpf_cliente][2] = True
          ##RELATORIO
        else:
          print("Caso o cliente não pague a multa, esta vai aumentar!!")
      else:
        print("Caso o cliente não pague a multa, esta vai aumentar!!")
    if emprestimos[cpf_cliente][3]:
      codigo = random.random()  
      quita_divida[codigo] = [cpf_cliente, emprestimos[cpf_cliente], pagar, multa, total_para_pagar]
      serializar_quita_divida(quita_divida)
      del emprestimos[cpf_cliente]
      print("OBRIGADO POR ALUGAR NA NOSSA EMPRESA, VOLTE SEMPRE!!")
    sair = input("Deseja sair da sessão(s/n)?")