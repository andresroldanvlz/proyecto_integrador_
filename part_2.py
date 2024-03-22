import pandas as pd
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")


data = pd.DataFrame(dataset["train"])


fallecidos = data[data['is_dead'] == 1]
sobrevivientes = data[data['is_dead'] == 0]


promedio_edad_fallecidos = fallecidos['age'].mean()
promedio_edad_sobrevivientes = sobrevivientes['age'].mean()


print(f"Promedio de edad de fallecidos: {promedio_edad_fallecidos}")
print(f"Promedio de edad de sobrevivientes: {promedio_edad_sobrevivientes}")
