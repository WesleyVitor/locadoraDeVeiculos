'''
Procurar o cliente em que o emprestimo está associado
se encontrar
  mostrar o emprestimo
  verificar quantos dias de uso do aluguel
  pedir quantos dias de atraso

  pagar = dias de uso * diaria_veiculo1 + ..... +
  multa = dias de atraso * multa_veiculo 1+ .....+
  total = pagar + multa

  apagar o emprestimo se elemento 'foi pago' for True
'''
import pickle
def deserializar_emprestimos():
  arquivo = open("db_emprestimos.txt",'rb')
  return pickle.load(arquivo)
def deserializar_veiculos():
  arquivo = open("db_veiculos.txt",'rb')
  return pickle.load(arquivo)

def geral():
  sair = 'n'
  while sair == 'n':
    emprestimos = deserializar_emprestimos()
    veiculos = deserializar_veiculos()
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
          del emprestimos[cpf_cliente]
          ##RELATORIO
          print("OBRIGADO POR ALUGAR NA NOSSA EMPRESA, VOLTE SEMPRE!!")
        else:
          print("Caso o cliente não pague a multa vai rolar!!")
      else:
        print("Caso o cliente não pague a multa vai rolar!!")