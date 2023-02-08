from datetime import datetime, date, time, timedelta

now : datetime = datetime.now()
# instancio una fecha, (tambien recibe por parametro la hora , minuto y segundo)
dates = datetime(2023,6,23)


# obtengo la fecha actual

print(datetime.today())
print(datetime.now())
print(f"soy date --> {dates}")

# puedo manipular cada informacion de la fecha

def time_all(date : datetime):
    print(date.hour)
    print(date.minute)
    print(date.second)


# ejecuto la funcion donde le paso un datatime.now()
# dentro de la funcion obtengo el valor individual de la hora , minuto y segundo
time_all(datetime.now())

def print_date(date: datetime):
    print(f"{date.day}/{date.month}/{date.year}")


print_date(dates)


print(dates.timestamp())


# instancio e encapsulo un time 
current_time = time(hour=4, minute=31,second=29)

print(current_time)


# instancio un Date 
another_date = date(2024,6,23)

# date actual
current_date = date.today()


print(current_date)


# diferencia , obteniendo la fecha  de la diferencia de 2 fechas

diff = dates - now

diff_2 = dates.date() - current_date
print(f"soy time {dates.time()}")
print(f"soy diff2 {diff_2}")

# time delta , apra trabajar con rango de fechas

start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)

print(end_timedelta - start_timedelta)