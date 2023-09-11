import hashlib

while 1:
    entrada = input("Digite a string para transformar em hash: ")
    entrada = entrada.encode('utf-8')

    hash = hashlib.sha1(entrada)
    hash = hash.hexdigest()

    print(hash)
