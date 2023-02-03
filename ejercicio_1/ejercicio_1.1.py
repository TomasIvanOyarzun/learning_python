

#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

#Diferencias de duracion del curso de dalto contra el mas rapido

# sacar la diferencia porcentaje entre 2 unidades  
diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_con_max = round(100 - curso_dalto / otros_cursos_max * 100 , 2)
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100



# Diferencias de duracion
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10

print(f'el curso de dalto dura {diferencia_con_min}% menos que el curso mas rapido')
print(f'el curso de dalto dura {diferencia_con_max}% menos que el curso mas lento')
print(f'el curso de dalto dura {diferencia_con_promedio}% menos que el curso promedio')
print("------------------------------------------------------")
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"el curso de dalto elimina {tiempo_vacio_dalto}% de tiempo vacio")
print("------------------------------------------------------")
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / curso_dalto * 10 ,  2)} horas de otro cursos")
print(f"Ver 10 horas de otros cursor equivale a ver {curso_dalto / otros_cursos_promedio * 10} horas de este curso")