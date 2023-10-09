# Lab AWS S3

## Objetivo

Explorar as capacidades do serviço AWS S3.  Nos passos que seguem, você será guiado pelas configurações necessárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.

## Evidências

### Etapa 1: Criar um bucket

![Criação do Bucket](./img_S3/1.png)

### Etapa 2: Habilitar hospedagem de site estático

* Hospedagem de site estático habilitada

![Hospedagem habilidada](./img_S3/2.png)

* Endpoint

![Endpoint](./img_S3/3.png)

### Etapa 3: editar as configurações do Bloqueio de acesso público

* Opção "Bloquear todo acesso público" desativada

!["Bloquear todo acesso público" desativada](./img_S3/4.png)

### Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível

* Política do bucket editada

!["Política do bucket editada"](./img_S3/5.png)

### Etapa 5: Configurar um documento de índice

* Criando um arquivo local com o nome *index.html*.

![index.html](./img_S3/6.png)

* Upload do index.html e do dados/nomes.csv para o bucket.

![index.html](./img_S3/7.png)

![dados/nomes.csv](./img_S3/8.png)

### Etapa 6: configurar documento de erros

* Upload do documento de erros *404.png* no bucket

![404.html](./img_S3/9.png)

### Etapa 7: testar o endpoint do site

* Teste do endpoint do site no navegador

![endpoint no navegador](./img_S3/10.png)