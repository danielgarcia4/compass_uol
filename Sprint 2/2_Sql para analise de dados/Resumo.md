# Sprint 2

### SQL para análise de dados

## Comandos básicos de SQL

* **Select:** Serve para selecionar colunas de tabelas.

**Exemplo:** 

``` sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```


* **Distinct:** Serve para mostrar apenas as linhas distintas, removendo as repetidas.

**Exemplo:**
``` sql
select distinct coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```

* **Where:** Serve para filtrar a seleção de acordo com uma condição

**Exemplo:**
``` sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x
```

* **Order by:** Serve para ordenar a seleção baseada em uma regra definida.

**Exemplo:**

``` sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true
order by coluna_1
```

**OBS:** Por default, o comando ordena na ordem crescente. Usando o comando ```DESC```, ordena em ordem decrescente.


* **Limit:** serve para limitar o número de linhas da consulta

**Exemplo:**

``` sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
limit N
```

## Operadores

### Operadores Aritméticos

Os **operadores aritméticos** servem para executar operações matemáticas. São muito utilizados para criar colunas calculadas. Utilizamos o comando “as” para adicionar pseudônimos a essas colunas calculadas.

**+** (soma)\
**-** (subtração)\
__*__ (multiplicação)\
**/** (divisão)\
**^** (exponencial)\
**%** (módulo)\
**||** (soma de strings)

**Exemplo:**

``` sql
select
	email,
	birth_date,
	(current_date - birth_date) / 365 as idade_do_cliente
from sales.customers
```

### Operadores de Comparação

Os **Operadores de Comparação** servem para comparar dois valores retornando **TRUE** ou **FALSE**. É muito utilizado com o comando ```WHERE``` para filtrar linhas de uma seleção.

**=** (igual à)\
**>** (maior que)\
**<** (menor que)\
**>=** (maior ou igual que)\
**<=** (menor ou igual que)\
**<>** (diferente de)

**Exemplo:**

``` sql
select
    customer_id,
first_name,
    professional_status,
	(professional_status = 'clt') as cliente_clt
from sales.customers
```

### Operadores Lógicos

Os **operadores lógicos** são usados para unir expressões simples em uma composta.

**AND:** Verifica se duas comparações são simultaneamente verdadeiras

**OR:** Verifica se pelo menos uma das comparações é verdadeira

**BETWEEN:** Verifica quais valores estão dentro do intervalo definido

**IN:** Verifica se um dos itens da lista é verdadeiro. Funciona como vários ORs

**LIKE:** Compara textos. É sempre utilizado com o operador %, que indica que qualquer texto pode aparecer no lugar do campo.

**ILIKE:** É como o Like, mas ignora se o campo tem letras maiúsculas ou minúsculas na comparação.

**IS NULL:** Verifica se o campo é nulo

**Exemplos:**

``` sql
select *
from sales.products
where price between 100000 and 200000
```

```sql
select distinct first_name
from sales.customers
where first_name ilike 'ana%'
```

## Funções agregadas

As funções agregadas servem para executar operações aritméticas nos registros de uma coluna. Funções agregadas não computam células vazias como zero.

**COUNT()** (serve para contar)

**SUM()** (serve para fazer operações)

**MIN()** (serve para pegar o valor mínimo)

**MAX()** (serve para pegar o valor máximo)

**AVG()** (serve para pegar o valor médio)

**Exemplos:**

``` sql
select count(*)
from sales.funnel
```
```sql
select min(price), max(price), avg(price)
from sales.products
```

```Group by``` serve para agrupar registros semelhantes de uma coluna, muito utilizado com as funções agregadas. Pode-se referenciar a coluna a ser agrupada pela sua posição ordinal.

**Exemplo:**

``` sql
-- Calcule o nº de clientes da tabela customers por estado
select state, count(*) as contagem
from sales.customers
group by state
order by contagem desc
```

```Having``` serve para filtrar linhas da seleção por uma coluna agrupada. Tem a mesma função do WHERE mas pode ser usado para filtrar os resultados das funções agregadas.

**Exemplo:**

``` sql
-- Calcule o nº de clientes por estado filtrando apenas estados acima de 100 clientes
select 
    state, 
    count(*)
from sales.customers
group by state
having count(*) > 100
```

## JOINS

Os joins servem para combinar tabelas com base em colunas relacionadas.

O ```INNER JOIN``` retorna apenas as linhas que têm valores correspondentes em ambas as tabelas.

Já o ```FULL JOIN``` retorna todas as linhas das duas tabelas.

O ```RIGHT JOIN``` retorna todas as linhas da tabela à direita mais as linhas correspondentes da tabela à esquerda. 

Já o ```LEFT JOIN``` retorna todas as linhas da tabela à esquerda mais as linhas correspondentes da tabela à direita.  Esse é o join mais utilizado.

**Exemplo:**

``` sql
-- temp_tables.tabela_1 e temp_tables.tabela_2
-- select * from temp_tables.tabela_1
-- select * from temp_tables.tabela_2

select t1.cpf, t1.name, t2.state
from temp_tables.tabela_1 as t1 
left join temp_tables.tabela_2 as t2
	on t1.cpf = t2.cpf
```

## UNIONS

Serve para colar uma tabela sobre a outra. Devem ser do mesmo tipo e mesmo numero de colunas. 

```union``` - União de duas tabelas, eliminando repetições
```union all``` - União simples de duas tabelas

**Exemplo:**

``` sql
--  União simples de duas tabelas
-- Una a tabela sales.products com a tabela temp_tables.products_2

select * from sales.products
union all
select * from temp_tables.products_2
```

## SUBQUERIES

Servem para consultar dados de outras consultas.

É possiver fazer subquery no ```WHERE```, com ```WITH```, no ```FROM``` e no ```SELECT```.


**Exemplos:**

``` sql
-- Subquery no WHERE
-- Informe qual é o veículo mais barato da tabela products

select *
from sales.products
where price = (select min(price) from sales.products)
```

``` sql
-- Subquery no SELECT
-- Na tabela sales.funnel crie uma coluna que informe o nº de visitas acumuladas 
-- que a loja visitada recebeu até o momento

select
	fun.visit_id,
	fun.visit_page_date,
	sto.store_name,
	(
		select count(*)
		from sales.funnel as fun2
		where fun2.visit_page_date <= fun.visit_page_date
			and fun2.store_id = fun.store_id
	) as visitas_acumuladas
from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
order by sto.store_name, fun.visit_page_date
```

## Tratamento de dados

### Conversão de Unidades

É possível converter um dado para alguma unidade específica. Existem dois operadores: O **::** e o **CAST()**. O mais utilizado é o ::, no entanto muitas vezes ele não funciona, tornando necessária a utilização da função CAST().

**Exemplos:**

``` sql
select '2021-10-01'::date - '2021-02-01'::date
```
``` sql
select nome_coluna::date
from nome_tabela
```
``` sql
select cast('2021-10-01' as date) - cast('2021-02-01' as date)
```

### Unidades mais utilizadas:

**int** (inteiro)

**numeric** (numérico preciso)

**float** (numérico com casas decimais)

**money** (valor em moeda)

**date** (data)

**timestamp** (data e hora)

**text** (texto)

### Tratamento Geral

Para o tratamento geral existem os comandos ```CASE WHEN``` e ```COALESCE()```.

O ```CASE WHEN``` é utilizado para criar respostas específicas para condições diferentes. Muito utilizado para fazer agrupamento de dados.

Exemplo: 

```
-- Calcule o nº de clientes que ganham abaixo de 5k, entre 5k e 10k, entre 10k e 
-- 15k e acima de 15k

with faixa_de_renda as (
	select
		income,
		case
			when income < 5000 then '0-5000'
			when income >= 5000 and income < 10000 then '5000-10000'
			when income >= 10000 and income < 15000 then '10000-15000'
			else '15000+'
			end as faixa_renda
	from sales.customers
)

select faixa_renda, count(*)
from faixa_de_renda
group by faixa_renda
```

O ```COALESCE``` serve para preencher campos nulos com o primeiro valor não nulo de uma sequência de valores.

**Exemplo:**

``` sql
select
	*,
	coalesce(population, (select avg(population) from temp_tables.regions)) as populacao_ajustada
	
from temp_tables.regions
```

### Tratamento de texto

Para o tratamento de texto existem algumas funções. São elas:

```LOWER()```: transforma o texto todo em letras minúsculas\
Exemplo: ```select lower('São Paulo')```

```UPPER()```: transforma o texto todo em letras maiúsculas\
Exemplo: ```select upper('São Paulo')```

```TRIM()```: remove os espaços das extremidades do texto\
Exemplo: ```select trim('SÃO PAULO     ')```

```REPLACE ()```: substitui uma string por outra string\
Exemplo: ```select replace('SAO PAULO', 'SAO', 'SÃO')```

### Tratamento de datas

Para o tratamento de datas existem algumas opções.

```INTERVAL```: é utilizado para somar datas na unidade desejada.

**Exemplo:**

``` sql
-- Calcule a data de hoje mais 10 unidades (dias, semanas, meses, horas)
select current_date + 10
select (current_date + interval '10 weeks')::date
select (current_date + interval '10 months')::date
select current_date + interval '10 hours'
```

```DATE_TRUN```: serve para truncar uma data no início do período. (Se você tiver qualquer data do mês, será associada a ela o primeiro dia desse mês)

**Exemplo:**

``` sql
-- Calcule quantas visitas ocorreram por mês no site da empresa

select visit_page_date, count(*)
from sales.funnel
group by visit_page_date
order by visit_page_date desc

select
	date_trunc('month', visit_page_date)::date as visit_page_month,
	count(*)
from sales.funnel
group by visit_page_month
order by visit_page_month desc
```

```EXTRACT```: é utilizado para extrair unidades de uma data/timestamp

**Exemplo:**

``` sql
-- Calcule qual é o dia da semana que mais recebe visitas ao site

select
	extract('dow' from visit_page_date) as dia_da_semana,
	count(*)
from sales.funnel
group by dia_da_semana
order by dia_da_semana

```
``` sql
-- Diferença entre datas com operador de subtração (-) 
-- Calcule a diferença entre hoje e '2018-06-01', em dias, semanas, meses e anos.

select (current_date - '2018-06-01')
select (current_date - '2018-06-01')/7
select (current_date - '2018-06-01')/30
select (current_date - '2018-06-01')/365

select datediff('weeks', '2018-06-01', current_date)
```

**Lista de Unidades de dia**

```day```: Retorna o dia do mês. Vai de 1 à 31

```month```: Retorna o mês do ano. Vai de 1 à 12

```week```: Retorna a semana do ano. Vai de 1 à 53

```year```: Retorna o ano da data

```dow```: sigla para "day of week". Vai de 0 (domingo) e vai a 6 (sábado)

## Funções

### Criar funções

Para **criar funções** no ***PostgreSQL***, o comando é ```CREATE FUNCTION```.

A sintaxe é a seguinte:

``` sql
create function nome_da_funcao(var1 tipo_var1, var2 tipo_var2)
returns tipo_return
language linguagem

as
$$

script da função

$$
```

Exemplo:

``` sql
-- (Exemplo 1) Crie uma função chamada DATEDIFF para calcular a diferença entre
-- duas datas em dias, semanas, meses, anos

create function datediff(unidade varchar, data_inicial date, data_final date)
returns integer
language sql

as

$$

	select
		case
			when unidade in ('d', 'day', 'days') then (data_final - data_inicial)
			when unidade in ('w', 'week', 'weeks') then (data_final - data_inicial)/7
			when unidade in ('m', 'month', 'months') then (data_final - data_inicial)/30
			when unidade in ('y', 'year', 'years') then (data_final - data_inicial)/365
			end as diferenca

$$

select datediff('years', '2021-02-04', current_date)

```

### Deletar uma função
Para **deletar uma função**, o comando é ```DROP FUNCTION```.
Exemplo: ```drop function datediff```

## Manipulação de tabelas

### Criação e deleção de tabelas

É possível **criar uma tabela a partir de uma query**. Para isso, basta escrever a query e colocar comando ```INTO``` antes do ```FROM``` informando o schema e o nome da nova tabela.

**Exemplo:**

``` sql
-- Crie uma tabela chamada customers_age com o id e a idade dos clientes. 
-- Chame-a de temp_tables.customers_age

select
	customer_id,
	datediff('years', birth_date, current_date) idade_cliente
	into temp_tables.customers_age
from sales.customers
```

Também é possível **criar uma tabela do zero**.

Para isso, utilizamos os seguintes comandos:

```CREATE TABLE``` - para criar tabela vazia

```INSERT INTO``` - para informar quais valores serão inseridos

```VALUES``` - para inserir os valores em forma de lista

**Exemplo:**

```sql
-- Crie uma tabela com a tradução dos status profissionais dos clientes. 
-- Chame-a de temp_tables.profissoes

select distinct professional_status
from sales.customers

create table temp_tables.profissoes (
	professional_status varchar,
	status_profissional varchar
)

insert into temp_tables.profissoes
(professional_status, status_profissional)

values
('freelancer', 'freelancer'),
('retired', 'aposentado(a)'),
('clt', 'clt'),
('self_employed', 'autônomo(a)'),
('other', 'outro'),
('businessman', 'empresário(a)'),
('civil_servant', 'funcionário público(a)'),
('student', 'estudante')
```

Para **deletar uma tabela**, basta utilizar o comando ```DROP TABLE```. 

**Exemplo:** ```drop table temp_tables.profissoes```

## Inserção, atualização e deleção de linhas

### Inserir linha em uma tabela

Para **inserir linhas em uma tabela**, devemos usar:

```INSERT INTO``` - para informar o nome da tabela e o nome das colunas onde os dados serão inseridos.

```VALUES``` - para inserir os valores manualmente em forma de lista.

**Exemplo:**

```sql
-- Insira os status 'desempregado(a)' e 'estagiário(a)' na temp_table.profissoes

insert into temp_tables.profissoes
(professional_status, status_profissional)

values
('unemployed', 'desempregado(a)'),
('trainee', 'estagiario(a)')
```

### Atualizar linhas em uma tabela

Para **atualizar linhas em uma tabela**, devemos usar:

```UPDATE``` - para informar qual tabela será atualizada.

```SET``` - para informar qual é o novo valor.

```WHERE``` - para delimitar qual linha será modificada

**Exemplo:** 

``` sql
-- Corrija a tradução de 'estagiário(a)' de 'trainee' para 'intern' 

update temp_tables.profissoes
set professional_status = 'intern'
where status_profissional = 'estagiario(a)'
```

### Deletar linhas em uma tabela

Para **deletar linhas em uma tabela** usamos os comandos:

```DELETE FROM``` - para informar de qual tabela as linhas serão deletadas.

```WHERE``` - para delimitar qual linha será deletada.

**Exemplo:** 

```sql
-- Delete as linhas dos status 'desempregado(a)' e 'estagiário(a)'

delete from temp_tables.profissoes
where status_profissional = 'desempregado(a)'
or status_profissional = 'estagiario(a)'
```

## Inserção, atualização e deleção de colunas

Para **inserir novas colunas**, usamos o comando ```ADD```. Para qualquer **modificação nas colunas** utilizamos o comando ```ALTER TABLE```.

Exemplo:
```sql
-- Insira uma coluna na tabela sales.customers com a idade do cliente
alter table sales.customers
add customer_age int

update sales.customers
set customer_age = datediff('years', birth_date, current_date)
where true
```

Para **mudar o tipo de unidade de uma coluna**, utilizamos o comando ```ALTER COLUMN```.

**Exemplo:**

```sql
-- Altere o tipo da coluna customer_age de inteiro para varchar
alter table sales.customers
alter column customer_age type varchar
```

Para **renomear uma coluna** utilizamos o comando ```RENAME COLUMN```.

**Exemplo:**

```sql
-- Renomeie o nome da coluna "customer_age" para "age"
alter table sales.customers
rename column customer_age to age
```

Para **deletar** uma coluna utilizamos o comando ```DROP COLUMN```.

**Exemplo:**

```sql
-- Delete a coluna "age"

alter table sales.customers
drop column age
```
## Atalhos
[Voltar para o README.md da raiz](/README.md)\
[Voltar para o README.md da Sprint 2](/Sprint%202/README.md)
