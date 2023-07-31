# Linux para desenvolvedores (Sprint 1)

## Compactação e descompactação de arquivos e diretórios

É possível fazer a compactação e descompactação de arquivos por linha de comando, utilizando o ***tar*** e o ***zip***.

### Tar

* **Compactar arquivos:** 

``` shell
tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
```
c: criar arquivo\
z: comprimir com gzip\
v: mostrar progresso\
f: especificar nome do arquivo

* **Compactar múltiplos diretórios e arquivos:**

``` shell
tar -czvf archive.tar.gz /home/ubuntu/Downloads /usr/local/stuff
/home/ubuntu/Documents/notes.txt
```

* **Descompactar:**

``` shell
tar -xzvf archive.tar.gz
```
Para diretório específico:
``` shell
tar -xzvf archive.tar.gz -C /tmp
```

### Zip

* **Compactar**

``` shell
zip -r nome_do_arquivo.zip diretório_ou_arquivo
```

* **Descompactar**
``` shell
unzip nome_do_arquivo.zip -d destino
```
