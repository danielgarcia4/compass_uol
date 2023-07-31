# Git e GitHub (Sprint 1)

## Administração de repositórios

Alguns comandos auxiliam na administração do repositório, aumentando assim seu desempenho.

### Comandos importantes

* **Limpando arquivos untracked**

```git clean``` | Limpa os arquivos que ainda não foram trackeados (que não usou o git add ou arquivos gerados automaticamente)

* **Otimizando repositório**

```git gc``` | (garbage collector) identifica arquivos que não são mais necessários e os exclui, otimizando o repositório em questão de performance

* **Checando integridade de arquivos**

```git fsck``` | (File System Check) verifica a integridade de arquivos e sua conectividade, possíveis corrupções em arquivos

* **Reflog**

```git reflog``` | mapear todos os seus passos no repositório, até uma mudança de branch é inserida neste log. O reflog expira com o tempo (default 30 dias)

```git reset --hard <hash>``` | avançar ou retroceder nas branches do reflog

* **Transformando o repo para arquivo**

```git archive --format zip --output main_files.zip main``` | transforma o repo em um arquivo compacto (main vai estar zipada no arquivo **main_files.zip**)

## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 1](/Sprint%201/README.md)