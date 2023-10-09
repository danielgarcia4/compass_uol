# Lab AWS Lambda

### Etapa 1: Criar a função do Lambda

![Criação função Lambda](./img_Lambda/1.png)

### Etapa 2: Construir o código

* Alterando o *lambda_function.py*

![lambda_function.py](./img_Lambda/2.png)

* Teste da Lambda com mensagem de erro

![mensagem de erro](./img_Lambda/3.png)

### Etapa3: Criar uma Layer

* Criação do Dockerfile e da imagem do Docker

![dockerfile e imagem](./img_Lambda/4.png)

* Criação das pastas

![criação das pastas](./img_Lambda/5.png)

* Baixar bibliotecas e dependências

![baixando bibliotecas e dependencias](./img_Lambda/6.png)

![verificando as bibliotecas e dependencias](./img_Lambda/7.png)

* Compactando os arquivos em um arquivo chamado *minha-camada-pandas.zip*

```
bash-4.2# cd ..
bash-4.2# zip -r minha-camada-pandas.zip .
```

![execução do comando](./img_Lambda/8.png)

* Copiar o arquivo para a máquina local

![copiando para a máquina local](./img_Lambda/9.png)

* Carregando o arquivo para o bucket S3

![carregando arquivo para o bucket](./img_Lambda/10.png)

* Criação da camada

![criação da camada](./img_Lambda/11.png)

### Etapa 4: Utilizando a Layer

* Camada adicionada

![camada adicionada](./img_Lambda/12.png)

* Execução do teste com erro ainda

![execução com erro](./img_Lambda/13.png)

* Aumentando o tempo limite e o tamanho da memória da Lambda.

![aumentando](./img_Lambda/14.png)

* Execução bem sucedida.

![execução bem sucedida](./img_Lambda/15.png)
