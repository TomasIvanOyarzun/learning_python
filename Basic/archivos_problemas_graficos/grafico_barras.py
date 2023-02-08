import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_2 = pd.read_csv("Basic\\archivos_problemas_graficos\\cofla_ingresos.csv")

# creando grafico barras
sns.barplot(x="fuente", y="ingresos", data=df_2)


total_ingresos = df_2["ingresos"].sum()
print(f"total ingresos: ${total_ingresos}")

plt.show()