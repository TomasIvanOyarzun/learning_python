import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Basic\\archivos_problemas_graficos\\cripto.csv")

# creando grafico
sns.lineplot(x="fecha", y="crypto", data=df)
crypto = df.loc[df["crypto"] >= 250 , :]


# agregando un punto de referencia
plt.plot(crypto["fecha"],crypto["crypto"],"o")








# mostrando grafico
plt.show()