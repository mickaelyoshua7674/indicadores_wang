from sqlalchemy.engine import create_engine
from sqlalchemy import text, URL
from datetime import datetime
import os, json, time
import pandas as pd

hour = 18
print(f"Waiting until {hour}hrs...")
while datetime.now().hour < hour:
    time.sleep(30*60)
print(f"Lets start...\n\n")

with open("./secrets.txt", "r") as f:
    driver, username, password, host, port, database = f.read().split(",")
    url = URL.create(drivername=driver, username=username, password=password, host=host, port=port, database=database)
    engine = create_engine(url)

with open("create_table.sql", "r") as f:
    create_table_script = f.read()

with open("file_field.json", "r", encoding="utf-8") as f:
    file_field = json.load(f)

to_float = lambda x: x.replace(",", ".")

def get_conta(x:str) -> str:
    sx = x.split(" - ")
    if len(sx) == 1:
        return "Sem Numero"
    return sx[0]

def get_des_conta(x:str) -> str:
    sx = x.split(" - ")
    if len(sx) == 1:
        return x
    return sx[1]

DATA_PATH = "data"
COLUMNS_ORDER = ["Ano","Tipo","Instituicao","IBGE","UF","Populacao","Coluna","Conta","Descricao_Conta","Identificador_Conta","Valor"]
def read_and_format_df(year:str, file_name:str) -> pd.DataFrame:
    file_path = os.path.join(DATA_PATH,year,file_name)
    df = pd.read_csv(file_path, sep=";", encoding="latin-1", skiprows=3)
    df["Valor"] = df["Valor"].apply(to_float)
    df["Valor"] = df["Valor"].astype(float)
    df["Descrição Conta"] = df["Conta"].apply(get_des_conta)
    df["Conta"] = df["Conta"].apply(get_conta)
    df["Ano"] = int(year)
    df["Tipo"] = file_field[file_name]
    df = df.rename(columns={"Cod.IBGE":"IBGE",
                            "Instituição":"Instituicao",
                            "População":"Populacao",
                            "Descrição Conta":"Descricao_Conta",
                            "Identificador da Conta":"Identificador_Conta"})
    return df[COLUMNS_ORDER]

with engine.begin() as conn:
    conn.execute(text(create_table_script))

YEARS = ["2022","2021","2020","2019","2018","2017","2016","2015","2014","2013"]
start = time.time()
with engine.connect() as conn:
        for year in YEARS:
            print(f"Inserting year {year}...")
            files_names = os.listdir(os.path.join(DATA_PATH,year))
            full_df = pd.concat([read_and_format_df(year,file_name) for file_name in files_names])
            full_df.to_sql(name="valores_finbra", con=conn, if_exists="append", index=False)
            conn.commit()
exec_time = time.time()-start
print(f"Execution time {round(exec_time,2)}s / {round((exec_time)/60,2)}min / {round(((exec_time)/60)/60,2)}hr")