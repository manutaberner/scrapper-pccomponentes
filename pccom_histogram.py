import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('/Users/manutaberner/Google Drive/UOC/Tipologia y ciclos/PRAC1/scrapper-pccomponentes/pccom-componentes.csv')

dataset.head()

# Plots #
    # Plot histogram
graph = dataset.Category.value_counts().plot(kind = "bar")

# X #
graph.set_xlabel("Componentes")

# Y #
graph.set_ylabel("Cantidad")

# Overall #
graph.set_title("Cantidad de productos por Categoría")

plt.show()