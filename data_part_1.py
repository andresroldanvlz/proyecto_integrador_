import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]
age_array = np.array(data['age'])

# Calculamos la media de la columna 'age'
edad = np.mean(age_array)
print(edad)
