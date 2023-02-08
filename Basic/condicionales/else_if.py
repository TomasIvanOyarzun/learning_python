ingreso_mensual = 400
gasto_mensual = 14000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("ahora si estas bien")
    else:
        print("y esta muy caro vivir")    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual >=500:
    print("estas bien en argentina")    
else:
    print("eres pobre")    

