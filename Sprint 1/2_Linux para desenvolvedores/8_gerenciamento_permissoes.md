# Linux para desenvolvedores (Sprint 1)

## Gerenciamento de permissões

### Entendendo as permissões

As permissões são a parte mais importante do linux, já que ela protege o sistema e os arquivos. É possível alterar 3 propriedades de arquivos e diretórios: **Leitura** (R - read), **Escrita** (W - Write), **E**xecução** (X - execute).

As permissões são separadas da seguinte forma:\
**1 222 333 444**\
1 indica se é diretório ou arquivo (d significa diretório e - significa arquivo);\
222 as permissões para o owner/dono;\
333 as permissões para o grupo;\
444 as permissões para os outros.

**Exemplo:** drw-rw-r– (diretório, dono e grupo com permissão de leitura e escrita, outros com permissão de leitura)

### Alterando as permissões

Existem dois tipos de alteração: **modo numérico** e **modo simbólico**


###  Modo numérico:

```chmod xxx file/dir```

(o x corresponde as permissões, que são os números a seguir)

0: Sem permissão ---\
1: Executar --x\
2: Escrever -w-\
3: Ler e Executar -wx\
4: Ler r--\
5: Ler e executar r-x\
6: Ler e escrever rw-\
7: Ler, escrever e executar rwx

**Exemplo:** ```chmod 764 arquivo```\
 (Dono todas as permissões, grupo pode ler e alterar e
demais só ler)

### Modo simbólico

```chmod args file/dir```\
(args são os argumentos)

\+ : Adiciona permissão a um arquivo ou diretório\
\- : Remove permissão a um arquivo ou diretório\
\= : Determina as permissões, substituindo as anteriores\
u : Dono do arquivo (user/owner)\
g : Grupo (group)\
o : Outros (others)\
a : Todos (all)

**exemplo:** ```chmod a=rwx```\
 (Concedendo todas as permissões a todos)

Comando para **alterar propriedade:** ```chown user file```\
**Alterando usuário e grupo do arquivo/dir:** ```chown user:group file```\
Comando para **alterar grupo:** ```chgrp group file```

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)