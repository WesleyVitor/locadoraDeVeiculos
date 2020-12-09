import pickle
arquivo = open('db_quita_divida.txt','wb')
pickle.dump({}, arquivo)
arquivo.close()
arquivo = open('db_clientes.txt','wb')
pickle.dump({}, arquivo)
arquivo.close()
arquivo = open('db_emprestimos.txt','wb')
pickle.dump({}, arquivo)
arquivo.close()
arquivo = open('db_veiculos.txt','wb')
pickle.dump({}, arquivo)
arquivo.close()


