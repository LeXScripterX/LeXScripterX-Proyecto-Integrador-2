import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]


edades = data["age"]

edades_np = np.array(edades)

promedioEdad = edades_np.mean()
promedioEdad_int = round(promedioEdad)


print(f"lista de edades: {edades}", "\n")
print(f"Arreglo de Numpy: {edades_np}","\n")
print(f"El promedio de edad es: {promedioEdad_int} años" )