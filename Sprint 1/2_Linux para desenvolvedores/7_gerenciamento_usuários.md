# Linux para desenvolvedores (Sprint 1)

## Gerenciamento de usuários e grupos

É possível fazer o gerenciamento de usuários e grupos, na criação de usuários, adição de usuários em grupos, etc.

### Comandos para gerenciamento de usuários

* **Criar usuário:** ```adduser user```
* **Deletar usuário:** ```userdel --remove user```
* **Modificando nome do usuário:** ```usermod -c ‘newname’ oldname```
* **Desabilitar usuário:** ```usermod -L user```
* **Habilitar usuário:** ```usermod -U user```

Um **grupo no Linux** contém vários usuários, auxiliando no gerenciamento de permissões. Por default, quando um usuário é criado ele é adicionado a um grupo com seu nome.

### Comandos para gerenciamento de grupos

* **Ver grupos:** ```getent group```
* **Criar grupo:** ```groupadd group```
* **Criar grupo definindo o id:** ```sudo groupadd -g id group```
* **Deletar grupo:** ```groupdel group```
* **Mudando usuário de grupo:** ```sudo usermod -a -G group user```
* **Remover usuário de um grupo:** ```sudo gpasswd -d user group```

**Dica:** para se tornar superusuário basta inserir o comando ```sudo su```\
**Dica:** para mudar a senha, o comando é ```passwd```