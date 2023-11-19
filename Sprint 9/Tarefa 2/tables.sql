-- CRIAÇÃO DAS TABELAS

CREATE TABLE tb_dim_carro (
		idCarro INT PRIMARY KEY,
		classiCarro VARCHAR(50),
		marcaCarro VARCHAR(80),
		modeloCarro VARCHAR(80),
		anoCarro INT,
		idCombustivel INT,
		tipoCombustivel VARCHAR(20)
);


CREATE TABLE tb_dim_cliente (
		idCliente INT PRIMARY KEY,
		nomeCliente VARCHAR(100),
 		cidadeCliente VARCHAR(40),
		estadoCliente VARCHAR(40),
		paisCliente VARCHAR(40)
);


CREATE TABLE tb_dim_vendedor (
		idVendedor INT PRIMARY KEY,
		nomeVendedor VARCHAR(15),
		sexoVendedor SMALLINT,
		estadoVendedor VARCHAR(40)
);


CREATE TABLE tb_dim_tempo (
	dataLocacao DATETIME PRIMARY KEY,
	anoLocacao INT,
	mesLocacao INT,
	diaLocacao INT,
	horaLocacao TIME,
	dataEntrega DATETIME,
	anoEntrega INT,
	mesEntrega INT,
	diaEntrega INT,
	horaEntrega TIME
);

CREATE TABLE tb_fato_locacao (
		idLocacao INT PRIMARY KEY,
		idCliente INT,
		idCarro INT,
		idVendedor INT,
		dataLocacao DATETIME,
		horaLocacao TIME,
		qtdDiaria INT,
		vlrDiaria DECIMAL(18,2),
		kmCarro INT,
		dataEntrega DATE,
		horaEntrega TIME,
		FOREIGN KEY(idCliente) REFERENCES tb_dim_cliente(idCliente),
		FOREIGN KEY(idCarro) REFERENCES tb_dim_carro(idCarro),
		FOREIGN KEY(idVendedor) REFERENCES tb_dim_vendedor(idVendedor),
		FOREIGN KEY(dataLocacao) REFERENCES tb_dim_tempo
);


-- INSERÇÃO DOS DADOS

INSERT INTO tb_dim_carro(idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel
FROM dim_carro;


INSERT INTO tb_dim_cliente(idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM dim_cliente;


INSERT INTO tb_dim_vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM dim_vendedor;

	
INSERT INTO tb_dim_tempo(dataLocacao, anoLocacao, mesLocacao, diaLocacao, horaLocacao, dataEntrega, 
						anoEntrega, mesEntrega, diaEntrega, horaEntrega)
SELECT DISTINCT dataLocacao, anoLocacao, mesLocacao, diaLocacao, horaLocacao, dataEntrega, 
				anoEntrega, mesEntrega, diaEntrega, horaEntrega
FROM dim_tempo;

	
INSERT INTO tb_fato_locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao,
			qtdDiaria, vlrDiaria, kmCarro, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao,
				qtdDiaria, vlrDiaria, kmCarro, dataEntrega, horaEntrega
FROM fato_locacao;


-- CONSULTA DAS DIM E FATO CRIADAS

SELECT * FROM tb_dim_carro;
SELECT * FROM tb_dim_cliente;
SELECT * FROM tb_dim_vendedor;
SELECT * FROM tb_dim_tempo;
SELECT * FROM tb_fato_locacao;