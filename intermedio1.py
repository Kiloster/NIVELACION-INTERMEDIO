password=input("Ingrese su contraseña para verificar requisitos de seguridad: ")
Longitud = len(password)
tiene_letras = any(c.isalpha() for c in password)
tiene_numeros = any(c.isdigit() for c in password)

if Longitud >= 8 and tiene_letras == True and tiene_numeros== True:
    print("Su contraseña es valida")
elif Longitud <= 8:
    print("Su contraseña no tiene 8 caracteres")
elif Longitud >= 8 and tiene_numeros== False:
    print("su contraseña no contiene al menos un numero")