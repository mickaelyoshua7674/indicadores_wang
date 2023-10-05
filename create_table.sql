DROP TABLE IF EXISTS dbo.valores_finbra;
CREATE TABLE dbo.valores_finbra (
    Ano INT,
    Tipo VARCHAR(300),
    Instituição VARCHAR(300),
    IBGE INT,
    UF VARCHAR(300),
    População INT,
    Coluna DATE,
    Conta VARCHAR(300),
    Descrição Conta VARCHAR(300),
    Identificador da Conta VARCHAR(300),
    Valor FLOAT
);