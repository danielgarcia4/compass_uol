# Lab AWS Athena

### Etapa 1: Configurar Athena

* Análise do arquivo *nomes.csv*.

![nomes.csv](./img_Athena/1.png)

Nome e tipo de dado das colunas:

nome STRING,\
sexo STRING,\
total INT,\
ano INT

* Criação da pasta *queries*.

![Pasta queries](./img_Athena/2.png)

* Configuração do local para os resultados de consultas no Amazon S3.

![Configuração local para resultados das consultas](./img_Athena/3.png)

### Etapa 2: Criar um banco de dados

* Criação do banco de dados *meubanco*.

![Criação meubanco](./img_Athena/4.png)

### Etapa 3: Criar uma tabela

* Elaboração da *query* para a criação da tabela e execução.

![Criação tabela](./img_Athena/5.png)

* Teste dos dados com a query apresentada.

![query](./img_Athena/6.png)

![resultado](./img_Athena/7.png)

* Criação da consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

![query](./img_Athena/8.png)

![resultado](./img_Athena/9.png)