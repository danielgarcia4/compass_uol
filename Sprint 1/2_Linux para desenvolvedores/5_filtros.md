# Linux para desenvolvedores (Sprint 1)

## Filtro e buscas em arquivos e diretórios

É possível aplicar filtros na leitura de arquivos, busca por palavras, localização de arquivos e muito mais. Os principais códigos são:

* **head**

Ler o topo de um arquivo: ```head file```\
Ler o topo de vários arquivos: ```head file1 file2```\
Ler um determinado número de linhas: ```head -n15 file```\
Resultado do head em um arquivo: ```head file > file2```

* **tail** - é muito utilizado para debug de logs

Ler o final de um arquivo: ```tail file```\
Ler o final de vários arquivos: ```tail file1 file2```\
Ler um determinado número de linhas: ```tail -n15 file```\
Resultado do tail em um arquivo: ```tail file > file2```\
Resultado em tempo real de um arquivo: ```tail -f file```

* **grep**

Encontrando palavra: ```grep ‘word’ file```\
Ignorando case sensitive: ```grep -i ‘word’ file```\
Busca recursiva: ```grep -r ‘word’ file```\
Contar ocorrência da palavra: ```grep -c ‘word’ file```

* **find**

Encontrar arquivos pelo nome: ```find . -name ‘teste*’```\
Ignorando case sensitive: ```find . -iname ‘TESTE.txt’```\
Procurando arquivos vazios: ```find . -empty```\
Procurando por tipo (arquivo): ```find . -type f```\
Procurando por tipo (diretório): ```find . -type d```

* **Locate** - Basicamente igual ao find, mas com maior performance, porque os dados
ficam armazenados em um banco de dados. 

Localizando um arquivo: ```locate file```\
Localizando arquivo com máximo de itens: ```locate .html -n 10```\
Ver os status do banco de dados: ```locate -S```

*Dica:* ```!!``` executa o último comando novamente\
Dica: ```which comand``` - serve para ver onde os comandos são executados
