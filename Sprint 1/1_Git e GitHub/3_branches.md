# Git e GitHub (Sprint 1)

## Branches

**Branch** é uma ramificação do projeto, separando assim as versões da aplicação. Ao criar um novo projeto ele inicia na branch ***main***, que é a principal. Após as atualizações das branches, elas são todas unidas para o código principal.

### Comandos importantes

Para **visualizar os branchs disponíveis**: ```git branch```

Para **criar um branch**: ```git branch <nome>```

Para **deletar uma branch** usamos a flag ```-d``` ou ```–delete```: ```git branch -d <nome>```

Para **mudar de branch**: ```git checkout -b <nome>```\
**CUIDADO:** Ao alterar de branch sem commitar as alterações antes, elas são levadas juntas para a outra branch.

Para **unir branches**: ```git merge <nome>```

Para **salvar as modificações atuais sem commit**, podemos usar o **stash**. É como se as alterações fossem para a ‘lixeira’, podendo ser restaurado depois.

O comando do **stash** é: ```git stash```\
Para **verificar as stashes**: ```git stash list```\
Para **recuperar uma stash**: ```git stash <nome>```\
Para **deletar todas as stashes**: ```git stash clear```\
Para **deletar uma stash específica**: ```git stash drop <nome>```

## Tags

**Tag** é um checkpoint de uma branch. Ou seja, são marcos no desenvolvimento, possibilitando ir voltando e avançando nas tags. Diferente do stash, ele realmente salva o conteúdo.

### Comandos importantes

Para **criar tags**: ```git tag -a <nome> -m “<msg>”```

Para **verificar uma tag**: ```git show <nome>```

Para **trocar de tag**: ```git checkout <nome>```

Para **enviar uma tag específica** ao repositório remoto: ```git push origin <nome>```

Para **enviar todas as tags** ao repositório remoto: ```git push origin --tags```

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)