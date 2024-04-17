import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
datos = pd.read_csv('datos_descargados.csv')

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 5))
plt.hist(datos['edad'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Graficar histogramas agrupados por hombre y mujer
hombres = datos[datos['sexo'] == 'Hombre']['edad']
mujeres = datos[datos['sexo'] == 'Mujer']['edad']

plt.figure(figsize=(10, 5))

# Histograma para hombres
plt.hist(hombres, bins=20, alpha=0.5, label='Hombres', color='blue', edgecolor='black')

# Histograma para mujeres
plt.hist(mujeres, bins=20, alpha=0.5, label='Mujeres', color='pink', edgecolor='black')

plt.title('Distribución de Edades por Género')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
