import pandas as pd
from scipy import stats
import numpy as np
import sys
import requests

def descargar_y_guardar_csv(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open('datos_descargados.csv', 'w') as archivo:
            archivo.write(respuesta.text)
        print("Los datos han sido descargados y guardados en 'datos_descargados.csv'.")
    else:
        print(f"Error al descargar los datos: status code {respuesta.status_code}")
        sys.exit(1)

def procesar_dataframe(df):
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[(np.abs(stats.zscore(df.select_dtypes(include=[np.number]))) < 3).all(axis=1)]
    bins = [0, 12, 19, 39, 59, df['age'].max()]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    df.to_csv('dataframe_procesado.csv', index=False)
    print("El dataframe ha sido procesado y guardado en 'dataframe_procesado.csv'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    descargar_y_guardar_csv(url)
    df = pd.read_csv('datos_descargados.csv')
    procesar_dataframe(df)
