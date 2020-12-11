import random
import pickle
from arquivos_gerais import verificar_arquivo, pegar_emprestimos, pegar_veiculos, pegar_quita_divida, gravar_quita_divida

def geral():
  sair = 'n'
  while sair == 'n':
    emprestimos = pegar_emprestimos()
    veiculos = pegar_veiculos()
    quita_divida = pegar_quita_divida()
    pagar = 0
    multa = 0
    cpf_cliente = input("Digite o cpf do cliente associado ao emprestimo:")
    
    if not(cpf_cliente in emprestimos):
      print("Não foi encontrado emprestimo associado a este CPF")
      print()
      sair = input("Deseja sair da sessão de quitar dividas?(s/n)?")
      continue
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
      gravar_quita_divida(quita_divida)
      del emprestimos[cpf_cliente]
      print("OBRIGADO POR ALUGAR NA NOSSA EMPRESA, VOLTE SEMPRE!!")
    print()
    sair = input("Deseja sair da sessão(s/n)?")