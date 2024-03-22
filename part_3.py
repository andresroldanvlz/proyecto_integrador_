import pandas as pd
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")


data = pd.DataFrame(dataset["train"])
print(data.dtypes)


hombres_fumadores = data[(data['is_male'] == 1) & (data['is_smoker'] == 1)].shape[0]


mujeres_fumadoras = data[(data['is_male'] == 0) & (data['is_smoker'] == 1)].shape[0]


print(f"Hombres fumadores: {hombres_fumadores}")
print(f"Mujeres fumadoras: {mujeres_fumadoras}")
