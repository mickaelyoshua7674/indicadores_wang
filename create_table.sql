DROP TABLE IF EXISTS dbo.valores_finbra;
CREATE TABLE dbo.valores_finbra (
    Ano INT,
    Tipo VARCHAR(50),
    Instituição VARCHAR(74),
    IBGE INT,
    UF VARCHAR(3),
    População INT,
    Coluna VARCHAR(96),
    Conta VARCHAR(160),
    Descrição Conta VARCHAR(213),
    Identificador da Conta VARCHAR(86),
    Valor FLOAT
);