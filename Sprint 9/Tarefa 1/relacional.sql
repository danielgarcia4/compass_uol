-- Criação das tabelas

CREATE TABLE cliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40)
);

CREATE TABLE vendedor (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(15),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(40)
);

CREATE TABLE combustivel (
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(20)
);

CREATE TABLE carro (
	idCarro INT PRIMARY KEY,
	classiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INT,
	idCombustivel INT,
	FOREIGN KEY(idCombustivel) REFERENCES combustivel(idCombustivel)	
);

CREATE TABLE locacao (
	idLocacao INT PRIMARY KEY,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	dataLocacao DATETIME,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL(18,2),
  	kmcarro INT,
	dataEntrega DATE,
	horaEntrega TIME,
	FOREIGN KEY(idCliente) REFERENCES cliente(idCliente),
	FOREIGN KEY(idCarro) REFERENCES carro(idCarro),
	FOREIGN KEY(idVendedor) REFERENCES vendedor(idVendedor)
);

-- Inserção dos dados

INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao


INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

INSERT INTO combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao

INSERT INTO carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao


INSERT INTO locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao,
					qtdDiaria, vlrDiaria, kmcarro, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao,
				qtdDiaria, vlrDiaria, kmcarro, dataEntrega, horaEntrega
FROM tb_locacao