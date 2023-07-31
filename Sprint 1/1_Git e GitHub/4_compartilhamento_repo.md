# Git e GitHub (Sprint 1)

## Compartilhamento e atualização de repositórios

Utilizando o git e os conceitos de branch, torna-se extremamente importante o compartilhamento e atualização dos repositórios.

### Comandos importantes

* **Encontrando branches**

```git fetch -a``` | você é atualizado de todos os branches e tags que ainda não estão reconhecidos por você

**OBS:** pra o branch passar a ser seu, você precisa acessar ele (usando o ***checkout***)

* **Recebendo atualizações**

```git pull``` | Recebe atualizações do repositório remoto

* **Enviando alterações**

```git push``` | Envia atualizações para o repositório remoto

(não esquecer de dar o ***add*** para os novos arquivos, e ***commit*** antes do ***push***)

* **Utilizando o remote**

```git remote -v``` | Verifica as origens

```git remote rm origin``` | Remove as origens

```git remote add origin <link do repositório>``` | Adiciona origem

* **Conhecendo os submodules**

**Submódulo** é a maneira que temos de possuir dois ou mais projetos em um só repositório.

```git submodule``` | Lista os submodules
```git submodule add <link do repositório>``` | Cria submodulo

* **Atualizando os submodules**

(Para atualizar um submódulo primeiro devemos commitar as mudanças)

```git push --recurse-submodules=on-demand``` | Enviar para o repo do submódulo