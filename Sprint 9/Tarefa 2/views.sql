-- CONSULTAS

SELECT * FROM carro ca;

SELECT * FROM cliente cl;

SELECT * FROM combustivel co;

SELECT * FROM locacao l;

SELECT * FROM vendedor v;

-- CRIANDO VIEWS

CREATE VIEW dim_carro AS
SELECT	ca.idCarro,
		ca.classiCarro,
		ca.marcaCarro,
		ca.modeloCarro,
		ca.anoCarro,
		ca.idCombustivel,
		co.tipoCombustivel 
FROM carro ca
JOIN combustivel co ON ca.idCombustivel = co.idCombustivel;


CREATE VIEW dim_cliente AS
SELECT	idCliente,
		nomeCliente,
 		cidadeCliente,
		estadoCliente,
		paisCliente
FROM cliente cl;

CREATE VIEW dim_vendedor AS
SELECT	idVendedor,
		nomeVendedor,
		sexoVendedor,
		estadoVendedor
FROM vendedor v;	

CREATE VIEW dim_tempo AS
SELECT DISTINCT
	dataLocacao,
	strftime('%Y', dataLocacao) as anoLocacao,
	strftime('%m', dataLocacao) as mesLocacao,
	strftime('%d', dataLocacao) as diaLocacao,
	horaLocacao,
	dataEntrega,
	strftime('%Y', dataEntrega) as anoEntrega,
	strftime('%m', dataEntrega) as mesEntrega,
	strftime('%d', dataEntrega) as diaEntrega,
	horaEntrega
FROM locacao l;
	

CREATE VIEW fato_locacao AS
SELECT	idLocacao,
		idCliente,
		idCarro,
		idVendedor,
		dataLocacao,
		horaLocacao,
		qtdDiaria,
		vlrDiaria,
		kmCarro,
		dataEntrega,
		horaEntrega
FROM locacao;
	

-- CONSULTA DAS DIM E FATO CRIADAS
SELECT * FROM dim_carro;
SELECT * FROM dim_cliente;
SELECT * FROM dim_vendedor;
SELECT * FROM dim_tempo;
SELECT * FROM fato_locacao;
