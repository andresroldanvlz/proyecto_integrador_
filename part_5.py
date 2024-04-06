import pandas as pd
from scipy import stats
import numpy as np

def procesar_dataframe(url):
    # Cargar los datos
    df = pd.read_csv(url)

    # Verificar y eliminar valores faltantes
    df.dropna(inplace=True)

    # Verificar y eliminar filas duplicadas
    df.drop_duplicates(inplace=True)

    # Verificar y eliminar valores atípicos (ejemplo simple usando el método Z-score)
    df = df[(np.abs(stats.zscore(df.select_dtypes(include=[np.number]))) < 3).all(axis=1)]

    # Crear una columna que categorice por edades
    bins = [0, 12, 19, 39, 59, df['age'].max()]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

    # Guardar el resultado como csv
    df.to_csv('dataframe_procesado.csv', index=False)

    return df

# Ejemplo de uso de la función con la URL incluida
df_procesado = procesar_dataframe('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
