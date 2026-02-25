**Nivel intermedio**
**Ejercicio 1**
Desarrolla un programa que verifique si una contraseña cumple con los requisitos mínimos de seguridad. El programa debe tener en cuenta lo siguiente:

La contraseña debe tener al menos 8 caracteres y contener al menos un número. El programa debe indicar si la contraseña es válida y, en caso contrario, explicar por qué no lo es.

**Ejercicio 2**
Imagina que necesitas verificar si varios servidores responden a una solicitud básica de red (similar a un "ping"). Escribe un programa en Python que:

Defina una lista llamada ips_servidores que contenga algunas direcciones IP de servidores (ejemplos: "192.168.1.10", "10.0.0.5", "192.168.34.2”).
Utiliza un ciclo for para recorrer cada dirección IP en la lista.
Dentro del ciclo, simula una verificación de conectividad. Para simplificar, utiliza una variable booleana llamada respuesta_ping dentro del ciclo y asígnale aleatoriamente los valores True (conectado) o False (no conectado) para cada IP. Para la aleatoriedad revisa la librería random en python.
Utiliza una estructura condicional (if/else) dentro del ciclo para imprimir un mensaje diferente según el valor de respuesta_ping:

Si respuesta_ping es True, imprime: "El servidor {IP} está respondiendo."
Si respuesta_ping es False, imprime: "¡Alerta! El servidor {IP} no responde."
