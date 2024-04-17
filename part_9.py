import pandas as pd
from sklearn.manifold import TSNE
import plotly.graph_objs as go

# Cargar los datos
datos = pd.read_csv('datos_descargados.csv')

# Eliminar las columnas que no se necesitan
datos_sin_columnas = datos.drop(columns=['DEATH_EVENT', 'categoria_edad'])

# Convertir el DataFrame a un numpy array
X = datos_sin_columnas.values

# Extraer la columna objetivo en un array unidimensional
y = datos['DEATH_EVENT'].values


# Ejecutar TSNE
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)


# Crear un gráfico de dispersión 3D
fig = go.Figure()

# Agregar los puntos al gráfico
fig.add_trace(go.Scatter3d(
    x=X_embedded[y==0, 0],  # x-coordinates para 'vivo'
    y=X_embedded[y==0, 1],  # y-coordinates para 'vivo'
    z=X_embedded[y==0, 2],  # z-coordinates para 'vivo'
    mode='markers',
    marker=dict(
        size=5,
        color='blue',  # color para 'vivo'
        opacity=0.8
    ),
    name='Vivo'
))

fig.add_trace(go.Scatter3d(
    x=X_embedded[y==1, 0],  # x-coordinates para 'muerto'
    y=X_embedded[y==1, 1],  # y-coordinates para 'muerto'
    z=X_embedded[y==1, 2],  # z-coordinates para 'muerto'
    mode='markers',
    marker=dict(
        size=5,
        color='red',  # color para 'muerto'
        opacity=0.8
    ),
    name='Muerto'
))

# Configurar el layout del gráfico
fig.update_layout(
    title='TSNE: Distribución 3D de Vivo vs Muerto',
    scene=dict(
        xaxis_title='Componente 1',
        yaxis_title='Componente 2',
        zaxis_title='Componente 3'
    )
)

# Mostrar el gráfico
fig.show()
