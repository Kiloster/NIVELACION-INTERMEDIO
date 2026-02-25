import random #libreria para generar un valor random

#Defina una lista llamada ips_servidores que contenga algunas direcciones IP
ips_servidores=["192.168.1.10", "10.0.0.5", "192.168.34.2"] 

#Recorremos la lista 
for ip in ips_servidores:
    #asignamos a una variable booleana los valores randoms True o False
    respuesta_ping= random.choice([True, False])
    #relacionamos los valores randoms a cada valor ip para verificar True (conectado)/False (no conectado) 
    if respuesta_ping == True:
        print(f"El servidor {ip} está respondiendo.")
    else:
        print(f"¡Alerta! El servidor {ip} no responde.")
