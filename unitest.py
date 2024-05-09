import unittest
import os
import pandas as pd
import sqlite3
import json

class TestExcelJsonSQLite(unittest.TestCase):

    def setUp(self):
        # Crea un DataFrame fittizio per i test
        self.test_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    def test_leggi_tabella_excel(self):
        # Testa se legge correttamente un file Excel
        file_excel = "test_excel.xls"
        self.test_df.to_excel(file_excel, index=False)
        df = leggi_tabella_excel(file_excel)
        os.remove(file_excel)  # Rimuovi il file temporaneo creato per il test
        self.assertTrue(df.equals(self.test_df))

    def test_salva_su_json(self):
        # Testa se salva correttamente su file JSON
        output_json = "test_output.json"
        salva_su_json(self.test_df, output_json)
        df_from_json = leggi_da_json(output_json)
        os.remove(output_json)  # Rimuovi il file temporaneo creato per il test
        self.assertTrue(self.test_df.equals(df_from_json))

    def test_salva_su_sqlite(self):
        # Testa se salva correttamente su database SQLite
        output_sqlite = "test_output.db"
        salva_su_sqlite(self.test_df, output_sqlite)
        conn = sqlite3.connect(output_sqlite)
        df_from_sqlite = pd.read_sql_query("SELECT * FROM voti", conn)
        conn.close()
        os.remove(output_sqlite)  # Rimuovi il file temporaneo creato per il test
        self.assertTrue(self.test_df.equals(df_from_sqlite))


if __name__ == '__main__':
    unittest.main()