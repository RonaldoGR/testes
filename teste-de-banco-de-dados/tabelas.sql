
-- CRIANDO TABELA DAS OPERADORAS ATIVAS 
CREATE TABLE IF NOT EXISTS operadoras_ativas (   
ID SERIAL PRIMARY KEY,
Registro_ANS INT, 
CNPJ VARCHAR(50),
Razao_Social VARCHAR(150),
Nome_Fantasia VARCHAR(100),
Modalidade VARCHAR(50),
Logradouro VARCHAR(50),
Numero VARCHAR(50),
Complemento VARCHAR(50),
Bairro VARCHAR(50),
Cidade VARCHAR(50), 
UF CHAR(2), 
CEP INT, 
DDD INT, 
Telefone VARCHAR(50), 
Fax VARCHAR(50), 
Endereco_eletronico VARCHAR(50),
Representante VARCHAR(50),
Cargo_Representante VARCHAR(50), 
Regiao_de_Comercializacao INT, 
Data_Registro_ANS DATE 
);



-- CRIANDO TABELA 2023 
CREATE TABLE IF NOT EXISTS tabela_2023 ( 
ID SERIAL PRIMARY KEY,
DATA DATE,
REG_NS INT,
CD_CONTA_CONTABIL INT, 
DESCRICAO VARCHAR (200),
VL_SALDO_INICIAL VARCHAR (50),
VL_SALDO_FINAL VARCHAR (50)
);



-- CRIANDO TABELA 2024 
CREATE TABLE IF NOT EXISTS tabela_2024 ( 
ID SERIAL PRIMARY KEY,
DATA DATE,
REG_NS INT,
CD_CONTA_CONTABIL INT, 
DESCRICAO VARCHAR (200),
VL_SALDO_INICIAL VARCHAR (50),
VL_SALDO_FINAL VARCHAR (50)
);