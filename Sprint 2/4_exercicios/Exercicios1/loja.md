## E8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

**Resolução:**

```sql
select vdd.cdvdd, vdd.nmvdd
from tbvendedor as vdd
left join tbvendas as ven
	on vdd.cdvdd = ven.cdvdd
WHEre ven.status = 'Concluído'
GROUP By vdd.cdvdd, vdd.nmvdd
ORDER BY COUNT(ven.cdven) DESC
LIMIT 1
```

## E9
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

**Resolução:**

```sql
select cdpro, nmpro
from tbvendas
WHERE status = 'Concluído'
	AND dtven BETWEEN '2014-02-03'and '2018-02-02'
GROUP BY cdpro, nmpro
ORDER BY COUNT(cdpro) DESC
LIMIT 1
```
## E10
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

**Resolução:**

```sql
SELECT
	vdd.nmvdd as vendedor,
    sum(ven.qtd*ven.vrunt) as valor_total_vendas,
    ROUND(SUM(ven.qtd * ven.vrunt*vdd.perccomissao)/100, 2) AS comissao
from tbvendedor as vdd
left join tbvendas as ven
	on vdd.cdvdd = ven.cdvdd
WHERE ven.status = 'Concluído'
group by vdd.nmvdd
order by comissao DESC
```

## E11
Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

**Resolução:**

```sql
SELECT
	ven.cdcli,
    ven.nmcli,
    SUM(ven.qtd*ven.vrunt) as gasto
FROM tbvendas as ven
WHERE ven.status = 'Concluído'
GROUP by ven.cdcli, ven.nmcli
order by gasto DESC
limit 1
```

## E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

**Resolução:**

```sql
SELECT
	dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    SUM(ven.qtd*ven.vrunt) as valor_total_vendas
From tbdependente as dep
LEFT JOIN tbvendas as ven
	ON dep.cdvdd = ven.cdvdd
WHERE ven.status = 'Concluído'
GROUP BY dep.cddep
ORDER BY valor_total_vendas
LIMIT 1
```

## E13
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

**Resolução:**

```sql
select cdpro, nmcanalvendas, nmpro,
	sum(qtd) as quantidade_vendas
from tbvendas
WHERE status = 'Concluído'
GROUP BY cdpro, nmcanalvendas
ORDER BY quantidade_vendas, nmcanalvendas desc
LIMIT 10
```

## E14
Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.

**Resolução:**

```sql
SELECT
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio DESC
```

## E15
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

**Resolução:**

```sql
SELECT cdven
FROM tbvendas
WHERE deletado = 1
GROUP BY cdven
ORDER BY cdven
```

## E16
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.

**Resolução:**

```sql
SELECT
    estado, nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro
```
## Atalhos
[Voltar para o README.md da raiz](/README.md)