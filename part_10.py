import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('datos_descargados.csv')

# Eliminar las columnas no deseadas
df.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'], inplace=True)

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop(columns=['age'])  # Todas las columnas excepto 'age'
y = df['age']  # Columna 'age'

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar el modelo de regresión lineal
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predicción en el conjunto de prueba
y_pred = regression.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)
