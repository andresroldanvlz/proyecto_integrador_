import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
datos = pd.read_csv('datos_descargados.csv')

# Crear una figura y un conjunto de subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Gráfica de torta para anémicos
axs[0, 0].pie(datos['anémico'].value_counts(), labels=datos['anémico'].unique(), autopct='%1.1f%%', startangle=140)
axs[0, 0].set_title('Distribución de Anémicos')

# Gráfica de torta para diabéticos
axs[0, 1].pie(datos['diabético'].value_counts(), labels=datos['diabético'].unique(), autopct='%1.1f%%', startangle=140)
axs[0, 1].set_title('Distribución de Diabéticos')

# Gráfica de torta para fumadores
axs[1, 0].pie(datos['fumador'].value_counts(), labels=datos['fumador'].unique(), autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Distribución de Fumadores')

# Gráfica de torta para muertos
axs[1, 1].pie(datos['muerto'].value_counts(), labels=datos['muerto'].unique(), autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Distribución de Muertos')

# Ajustar el layout para evitar solapamientos
plt.tight_layout()
plt.show()
