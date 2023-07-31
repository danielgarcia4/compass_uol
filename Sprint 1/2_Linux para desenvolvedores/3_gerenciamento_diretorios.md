# Linux para desenvolvedores

## Gerenciamento de diretórios e arquivos

Existem comandos que auxiliam no gerenciamento de diretórios, como a criação, remoção, copia ou movimentação. Alguns deles são:

* **mkdir**

Criando um diretório: ```mkdir diretorio```

Criando múltiplos diretórios: ```mkdir dir1 dir2 dir3```

Criando diretórios com verbose: ```mkdir -v dir1 dir2 dir3```
Criando uma estrutura de diretórios: ```mkdir -p dir1/dir2/dir3```

* **rm**

Removendo arquivo: ```rm teste.txt```

Removendo vários arquivos: ```rm a1.txt a2.txt a3.txt```

Removendo com interatividade (pergunta se deseja mesmo remover): ```rm -i teste.txt```

Forçando remoção de arquivo: ```rm -f teste.txt```

Removendo um diretório: ```rm -dv dir```

Removendo diretórios e arquivos recursivo: ```rm -rfv dir```

* **rmdir**

Deletando diretório vazio: ```rmdir dir```

Deletando diretórios vazios: ```rmdir -p dir/dir2/dir3```

* **cp**

Copiando um arquivo: ```cp teste.txt teste2.txt```

Copiando um arquivo para outro diretório: ```cp teste.txt dir/teste.txt```

Copiando vários arquivos em um diretório: ```cp 1.txt 2.txt 3.txt dir```

Copiando diretório recursivo: ```cp -r dir1 dir2```

Copiando todos os arquivos de um diretório para outro: ```cp dir1/* dir2```

Copiando todos os arquivos x para um diretório: ```teste* dir```

* **mv**

Movendo um arquivo: ```mv teste.txt teste2.txt```

Movendo um arquivo para um diretório: ```mv teste.txt dir/teste.txt```

Movendo vários arquivos para um diretório: ```mv * dir/```

Para saber exatamente onde está (a estrutura de diretórios): ```pwd```

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)