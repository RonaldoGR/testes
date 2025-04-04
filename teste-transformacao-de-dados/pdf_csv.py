import tabula
import pandas as pd
import zipfile
import os

lista_tabelas = tabula.read_pdf("/mnt/d/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", pages="3-179", pandas_options={"header": None})

colunas = ["PROCEDIMENTO", "RN (alteracão)", "VIGÊNCIA", "Seg. Odontológica", 
           "Seg. Ambulatorial", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]

data_frame_combinado = pd.DataFrame()

cabeçalho_real = lista_tabelas[0].iloc[0].tolist()

for i, tabela in enumerate(lista_tabelas):
    tabela = tabela.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    if tabela.iloc[0].tolist() == cabeçalho_real:
        tabela = tabela.iloc[1:]

    data_frame_combinado = pd.concat([data_frame_combinado, tabela], ignore_index=True)

data_frame_combinado.columns = colunas

data_frame_combinado = data_frame_combinado[~data_frame_combinado.apply(lambda row: row.tolist() == colunas, axis=1)]

csv_path = '/mnt/d/pdfs/tabela_combinada.csv'
data_frame_combinado.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')

print("CSV gerado ")

zip_path = '/mnt/d/pdfs/'
zip_filename = os.path.join(zip_path, "Teste_Ronaldo_Rocha.zip")  

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir(zip_path):
        csv = os.path.join(zip_path, file)

        if file == "Teste_Ronaldo.zip":
            continue

        if file.endswith(".csv"):
            zipf.write(csv, file)
            os.remove(csv)

print(f"Arquivo compactado")            