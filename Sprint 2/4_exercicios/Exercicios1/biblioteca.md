## E1
Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

**Resolução:**

```sql
select * from livro
where publicacao > '2014-12-31'
order by cod
```

## E2
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

**Resolução:**

```sql
select titulo, valor
from livro
order by valor DESC
limit 10
```

## E3
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

 **Resolução:**

```sql
select DISTINCT count(liv.editora) as quantidade, edi.nome, ende.estado, ende.cidade
from livro as liv
left join editora as edi
	on liv.editora = edi.codeditora
left JOIN endereco as ende
	ON edi.endereco = ende.codendereco
GROUP BY liv.editora
order by count(liv.editora) desc
limit 5
```

## E4
Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

 **Resolução:**

```sql
select 
	aut.nome, 
	aut.codautor,
    aut.nascimento,
    count(liv.cod) AS quantidade
from autor as aut
left join livro as liv
	on aut.codautor = liv.autor
GROUP BY aut.codautor
order by aut.nome
```

## E5
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

 **Resolução:**

```sql
select DISTINCT aut.nome 
FROM autor as aut 
LEFT JOIN livro as liv 
	on aut.codautor = liv.autor
LEFT JOIN editora as edi 
	on liv.editora = edi.codeditora
LEFT JOIN endereco as ende
	on edi.endereco = ende.codendereco
WHERE ende.estado not in ('SANTA CATARINA', 'PARANÁ', 'RIO GRANDE DO SUL')
order by aut.nome
```

## E6
Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

 **Resolução:**

```sql
SELECT
    aut.codautor,
    aut.nome,
    COUNT(liv.cod) AS quantidade_publicacoes
FROM autor as aut
left JOIN livro as liv 
	ON aut.codAutor = liv.autor
GROUP BY
    aut.codAutor, aut.nome
ORDER BY
    quantidade_publicacoes DESC
LIMIT 1
```

## E7
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

 **Resolução:**

```sql
SELECT aut.nome
FROM autor as aut
LEFT JOIN livro as liv
	ON aut.codautor = liv.autor
WHERE liv.cod IS NULL
ORDER BY aut.nome
```

## Atalhos
[Voltar para o README.md da raiz](/README.md)