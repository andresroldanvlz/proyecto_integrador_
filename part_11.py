import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

# Cargar los datos desde el archivo CSV
df = pd.read_csv('datos_descargados.csv')

# Supongamos que las características (X) están en las columnas 'feature1', 'feature2', etc.
# y la variable objetivo (y) está en la columna 'target'
X = df[['feature1', 'feature2', 'feature3']]
y = df['target']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Crear un clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

# Visualizar el árbol de decisión
fig, ax = plt.subplots(figsize=(12, 12))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=np.unique(y), ax=ax)
plt.show()

