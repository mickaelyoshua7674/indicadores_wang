DROP TABLE IF EXISTS SICONFI.dbo.valores_finbra;
CREATE TABLE SICONFI.dbo.valores_finbra (
    Ano INT,
    Tipo VARCHAR(50),
    Instituicao VARCHAR(74),
    IBGE INT,
    UF VARCHAR(3),
    Populacao INT,
    Coluna VARCHAR(96),
    Conta VARCHAR(160),
    Descricao_Conta VARCHAR(213),
    Identificador_Conta VARCHAR(86),
    Valor FLOAT
);