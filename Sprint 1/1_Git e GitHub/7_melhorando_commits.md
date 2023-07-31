# Git e GitHub (Sprint 1)

## Melhorando os commits do projeto

Commits sem sentido atrapalham o projeto. Precisamos padronizar os commits, para que o projeto cresça de forma saudável também no versionamento. Isso ajuda no review do pull request, melhoria do log e na manutenção do projeto.

### Private branches

São branches que não serão compartilhados no repositório, então podemos colocar qualquer commit. Ao final da solução do problema fazemos um ***rebase***.

```git rebase <atual> <funcionalidade> -i``` | é como um merge que altera o histórico. Comandos para navegar no rebase: “i” (para inserir)  “:x!” (Salva o arquivo do rebase)

Escolhemos os branches para excluir (***squash***) e renomear com (***reword***);

### Boas mensagens de commit

É muito bom deixar boas mensagens no commit para agilizar os processos. É importante separar o assunto do corpo da mensagem. Podemos padronizar, por exemplo, com o assunto com no máximo 50 caracteres e letra inicial maiúscula; Corpo com no máximo 72 caracteres.\
Explicar o **por que e como do commit**, e não como o código foi escrito. Um bom exemplo de commit com boa mensagem:

```
Criada função de adição do produto
   
a função foi criada para os novos clientes, não cadastrados, conseguirem adicionar produtos ao carrinho antes do login.
```

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)