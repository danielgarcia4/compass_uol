# Linux para desenvolvedores (Sprint 1)

## Linux Fundamental

**Terminal** é uma tela através da qual você insere comandos para interagir com o computador, e o **Shell** é quem interpreta e executa esses comandos. O terminal recebe os comandos e os transmite para o shell, que interpreta cada comando e retorna a resposta para o terminal.

Os comandos normalmente seguem o seguinte padrão: COMANDO -OPÇÃO ARQUIVOS/DIRETÓRIOS

### Conhecendo os principais diretórios

* **bin** - contém os arquivos binários que são necessários para executar determinadas ações. 

* **boot** - arquivos que auxiliam na inicialização do sistema

* **dev** - arquivos que representam todos os dispositivos de entrada e saída do sistema.

* **etc** - arquivos de configuração

* **home** - diretório dos usuários

* **lib** - contém arquivos de bibliotecas essenciais que são compartilhados entre outros aplicativos

* **media** - apresenta as pastas dos dispositivos montados no pc

* **opt** - arquivos de aplicações que não são oficiais do sistema

* **sbin** - arquivos binários de inicialização do sistema

* **tmp** - arquivos usados pelo sistema e aplicativos do usuário para armazenar dados necessários por um curto período de tempo

* **usr** - contém arquivos que são utilizados apenas no modo leitura

* **var** - arquivos de dados variáveis, como arquivos de log

### Principais comandos

Para mudar de diretório: ```cd```

Mudança direta entre diretórios: ```cd /etc/```

Mudança entre diretórios próximos: ```cd ssh (dentro de /etc/)```

Voltar para o diretório anterior: ```cd --```

Voltar um diretório: ```cd ..```

Voltar dois diretórios: ```cd ../../```

Mostrar último diretório antes do atual: ```cd -```

Mover para a home do usuário atual: ```cd ~```

Voltar e avançar em um outro diretório: ```cd ../var/``` (dentro de etc)

Utilizar **tab** para completar diretório alvo

Mudar de diretório e utilizar outro comando: ```cd ../ && ls```

listar arquivos e diretórios: ```ls```

Mostrar detalhes dos arquivos e diretórios: ```ls -l```

Mostrar arquivos ocultos: ```ls -a```

Mostrar tamanho dos arquivos human readable: ```ls -lh```

Mostrar data da última modificação: ```ls -ltr```

Listando arquivos em outro diretório: ```ls -l /etc```

Mostrar arquivos em ordem reversa: ```ls -r```

Mostrar sub-diretórios: ```ls -R```

Ordenar por tamanho do arquivo: ```ls -lS ou ls -lSh```

Listar os arquivos separados por vírgula: ```ls -m```

Mais infos: ```ls --help```

limpar a tela do terminal: ```clear```

mostrar o conteúdo de um arquivo: ```cat```

Ver o conteúdo de múltiplos arquivos: ```cat file1 file2```

Criar arquivo com o cat: ```cat > file.txt```

Mostrar o número de linhas com cat: ```cat -n file```

Mostrando $ em todo final de linha: ```cat -e file```

Criar um arquivo por meio de outro: ```cat file1 > file2```

Adicionar conteúdo a um arquivo a partir de outro: ```cat file1 >> file2```

Adicionando conteúdo de múltiplos arquivos em um: ```cat file1 file2 > file3```

Mudar a data de acesso de um arquivo ou cria um arquivo: ```touch```

Alterando data ou criando arquivo com touch: ```touch file```

Criando vários arquivos com touch: ```touch a.txt b.txt c.txt```

O manual do sistema operacionaml para entender os comandos: ```man``` (ex: man ls)

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)