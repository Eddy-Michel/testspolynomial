import pandas as pd
import matplotlib.pyplot as plt

# Lire les fichiers CSV
df1 = pd.read_csv("data_group_1__42.csv", sep=";")
df2 = pd.read_csv("data_group_2__404.csv", sep=";")


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Graphique 1
axes[0].plot(df1["x"], df1["y"])
axes[0].set_title("Fichier 1")
axes[0].grid()

# Graphique 2
axes[1].plot(df2["x"], df2["y"])
axes[1].set_title("Fichier 2")
axes[1].grid()

plt.tight_layout()
plt.show()