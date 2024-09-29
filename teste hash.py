# Exercicio sobre armazenar, processar e criptografar senhas usando o algoritmo MD5.

import hashlib
import time

arquivo = open("senha1.txt", "w")
arquivo.write("1234")
arquivo.close()

arquivo = open("senha2.txt", "w")
arquivo.write("45362789")
arquivo.close()

arquivo = open("senha3.txt", "w")
arquivo.write ("mengudocampeao")
arquivo.close()

arquivo = open("senha4.txt", "w")
arquivo.write("Gato_desconfiado1060")
arquivo.close()

def criptografar_md5(senha):
    hash_md5 = hashlib.md5()
    hash_md5.update(senha.encode('utf-8'))
    return hash_md5.hexdigest()


start = time.time()

for i in range(4):
    arquivo = open('senha' + str(i+1) + '.txt', 'r')
    senha = arquivo.read()
    hash_md5 = criptografar_md5(senha)
    print("Senha " + str(i+1) + " = " + hash_md5)

end = time.time()

print("Tempo levado: " + str(end - start))
