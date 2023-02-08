# falto el profe y los alumno va a armar la clase

# pedir el nombre y la edad de los partners que vinieron a clase


def get_cant_partners(cant):
    students = []
    for i in range(cant):
      name = input("ingrese el nombre del estudiante: ")
      age = int(input("ingrese la edad: "))
      
      students.append((name, age))
    students.sort(key= lambda x:x[1])
    asistente = students[0][0]
    teacher = students[-1][0]  

    return teacher,asistente


teacher,asistente = get_cant_partners(3)

print(f"el profesor es {teacher}, y el asistente es : {asistente}")




