## Practicing python
<img id="readme-top" width='100%' src="https://github.com/TomasIvanOyarzun/learning_python/blob/main/assets/img/python_desktop.png"/>


## Getting Started

Seeing different topics in python, doing practices, testing built-in python functions,
solving exercises, all the topics were seen by different courses and/or videos.

### some of the topics seen


* list,tuple,dict,set
  ```py
  
   # examples  
   my_list = list()
   # my_list = [23,12,45]
   my_list.append(44)
   
   my_tuple = tuple()
   # my_tuple = (23,12,45)
   my_set = set()
   # my_set = {23,12,45}
   my_Set.add(44)
  ```
* functions,lambda
  ```py
  
   # examples  
   def is_par(num):
       if num % 2 == 0 : True
   
   is_par(2) # True
   
   is_par = lambda x : x % 2
   
   print(is_par(4) # True
   
   
  ```
  
* class (POO)
  ```py
  
   # examples  
   class Pc
      def __init__(self, processor, ram, video_card):
        self.processor = processor
        self.lastname = ram
        self.video_card = video_card
        
      def on_pc():
           print(f"your pc is booting") 
   
   my_pc = Pc("i7 10700k", 16, "rtx 3070")
   
   my_pc.on_pc()
   my_pc.ram = 32
   
   
  ```

* read and write files
  ```py
  
   # examples  
    import pandas as pd
     
    df = pd.read_csv("archivos\\datos.csv")
    name = df["name"]
    df_sort_ascending = df.sort_values("age")
    df_sort_descending = df.sort.value("ages", ascending= False)
    
    # concat dataframe

    df_concat = pd.concat([df,df2])
   
    # getting people under 30 example

    person_menor_30 = df.loc[df["age"] < 30, :]
   
   
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns


   df_2 = pd.read_csv("Basic\\archivos_problemas_graficos\\cofla_ingresos.csv")

   # creando grafico barras
   sns.barplot(x="fuente", y="ingresos", data=df_2)


   total_ingresos = df_2["ingresos"].sum()
   print(f"total ingresos: ${total_ingresos}")

   plt.show()
  ```
  
* see graphics
  ```py
  
   # example 
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns


   df_2 = pd.read_csv("Basic\\archivos_problemas_graficos\\cofla_ingresos.csv")

   # creando grafico barras
   sns.barplot(x="fuente", y="ingresos", data=df_2)


   total_ingresos = df_2["ingresos"].sum()
   print(f"total ingresos: ${total_ingresos}")

   plt.show()
  ```
  <img width='50%' src="https://github.com/TomasIvanOyarzun/learning_python/blob/main/assets/img/python_grafico.png"/>

<!-- USAGE EXAMPLES -->
## Usage

To be able to run all these files it is necessary to install python, the latest version is recommended, and some text editor, in my case I use visual studio code, since it allows me to use different programming languages.

_Donwload python [Documentation](https://www.python.org/downloads/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
