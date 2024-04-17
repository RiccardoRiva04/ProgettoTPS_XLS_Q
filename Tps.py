import os
import pandas as pd
import sqlite3
import json

def leggi_tabella_excel(file_excel):

    download_path = os.path.join(os.path.expanduser("~"), "Downloads")

    file_path = os.path.join(download_path, file_excel)

    if os.path.exists(file_path):

        df = pd.read_excel(file_path)
        return df
    else:
        print("Il file specificato non esiste nella cartella 'Download'.")
        return None

def salva_su_json(df, output_json):

    df.to_json(output_json, orient='records')

def leggi_da_json(file_json):

    with open(file_json, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

def salva_su_sqlite(df, output_sqlite):

    conn = sqlite3.connect(output_sqlite)

    df.to_sql('voti', conn, if_exists='replace', index=False)

    conn.close()


file_excel = "1Sin.xls"
output_json = "tabella_voti_output.json"
output_sqlite = "voti.db"

df = leggi_tabella_excel(file_excel)

if df is not None:

    salva_su_json(df, output_json)


    df_from_json = leggi_da_json(output_json)


    salva_su_sqlite(df_from_json, output_sqlite)

    print("Dati salvati correttamente da Excel a JSON e da JSON a SQLite.")
