hora = int(input("Hora de inicio (horas): "))
minut = int(input("Minut de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
minut = minut + dura 
hora = hora + minut // 60
minut = minut % 60
hora = hora %24
print(hora, ":", minut, sep='')
