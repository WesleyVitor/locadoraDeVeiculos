import pickle
arquivo = open('db_emprestimos.txt','wb')
pickle.dump({}, arquivo)
