#EJERCICIO N°1 "CAJA DE KISCO"

nombre_cliente = input("Ingrese su nombre: ") 
while not nombre_cliente.isalpha(): #Validar nombre
    nombre_cliente = input("Solo se permiten letras. Intente otra vez: ")
nombre_cliente = str(nombre_cliente)
cant_productos = input("Ingrese cantidad de productos: ") 
while not cant_productos.isdigit() or int(cant_productos) <= 0: #Validar cantidad de productos
    cant_productos = input("Cantidad de productos no valido. Intente otra vez: ")
cant_productos = int(cant_productos)
total_sin_descuento = 0
total_con_descuento = 0 
for i in range(1,cant_productos+1): 
    precio = input(f"Ingrese el precio del producto N°{i}: ") #Pedir precio de cada prod
    while not precio.isdigit() or int(precio) <= 0: #Validar
        precio = input(f"Precio no valido. Intente otra vez: ")
    precio = int(precio)
    preg_descuento = input("Tiene descuento (S/N): ").lower() #Preguntar descuento
    while not preg_descuento.isalpha() or preg_descuento != "s" and preg_descuento != "n":
        preg_descuento = input("Accion no valida intentelo otra vez: ").lower()
    preg_descuento = str(preg_descuento)
    total_sin_descuento = total_sin_descuento + precio
    if preg_descuento.lower() == "s": #Aplicar descuento
        descuento = precio * 0.10
        precio_final = precio - descuento
    else:
        precio_final = precio
    total_con_descuento = total_con_descuento + precio_final
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cant_productos
print(F"Cliente: {nombre_cliente}") #Mostrar resultado al cliente
print(f"Total sin descuento: ${total_sin_descuento}") 
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"promedio por producto: ${promedio:.2f}")

#EJERCICIO N°2 "ACCESO AL CAMPUS Y MENU SEGURO"

usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False
separar_menu = "===================="
estado_inscripcion = "Inscripto"
pedir_usuario = input("Ingrese el nombre del usuario: ") #Pedir usuario
if pedir_usuario == usuario_correcto:
    acceso = True
elif pedir_usuario != usuario_correcto:
    for i in range(1,3+1):
        pedir_usuario = input(f"Nombre incorrecto. Intente otra vez ({i}): ")
        if pedir_usuario == usuario_correcto:
            acceso = True
            break
    if acceso == False: #Salir si es falso
        acceso = False
        print("Demaciados intentos. Cuenta Bloqueada")
if acceso == True:
    pedir_clave = input("Ingrese su clave: ") #Pedir clave
    if pedir_clave == clave_correcta:
        acceso = True
    elif pedir_clave != clave_correcta:
        for i in range(1,3+1):
            pedir_clave = input(f"Clave incorrecta. Intente otra vez ({i}): ")
            if pedir_clave == clave_correcta:
                acceso = True
                break
            elif pedir_clave != clave_correcta:
                acceso = False
        if acceso == False: #Salir si es falso
            acceso = False
            print("Demaciados intentos. Cuenta Bloqueada")
if acceso == True: #Si paso el logeo
    while 1 == 1: #Menu repetitivo
        print(separar_menu)
        print("1°_Ver estado de incripcion")
        print("2°_Cambiar clave")
        print("3°_Mostrar mensaje motivacional")
        print("4°_Salir")
        print(separar_menu)
        elegir = input("Eliga opcion: ")
        while not elegir.isdigit() or int(elegir) <= 0 and int(elegir) >= 5: #Validar opcion
            elegir = input("Opcion no valida. Intente otra vez: ")
        elegir = int(elegir)
        if elegir == 4: #Cerrar menu
            print(separar_menu)
            print("Has salido")
            break
        if elegir == 1: #Estado 
            print(separar_menu)
            print(f"Estado de inscripcion: {estado_inscripcion}")
        if elegir == 2: #Cambiar clave
            print(separar_menu)
            cambiar_clave = input("Ingrese su Nueva clave: ")
            while len(cambiar_clave) < 6:
                cambiar_clave = input("La clave minimo debe tener 6 caracteres: ")
            print(separar_menu)
            repetir_clave = input("Repita la contraseña nueva: ")
            if repetir_clave != cambiar_clave : #Verificar si es la misma clave
                while 1 == 1:
                    repetir_clave = input("La clave es diferente. Intente otra vez: ")
                    if repetir_clave == cambiar_clave:
                        break
        if elegir == 3: #Mensaje motivacional
            print(separar_menu)
            print("El secreto para salir adelante es comenzar.")

#EJERCICIO N°3 "AGENDA DE TURNO CON NOMBRES"

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
separar_menu = "===================="
nombre_ope = input("Ingrese su nombre: ") #Nombre del operador y verificacion
while not nombre_ope.isalpha():
    nombre_ope = input("Nombre no valido. Intente otra vez: ")
nombre_ope = str(nombre_ope)
while 1 == 1:
    print(separar_menu) #MENU REPETITIVO
    print("1°_Reservar Turno")
    print("2°_Cancelar Turno")
    print("3°_Ver Agenda del Dia")
    print("4°_Ver Resumen General")
    print("5°_Cerrar Sistema")
    print("")
    elegir = input("Eliga opcion: ") #Elejir opcion
    while not elegir.isdigit() or int(elegir) <= 0 or int(elegir) > 5: #Validar opcion
        elegir = input("Opcion no valida. Intente otra vez: ")
    elegir = int(elegir)
    if elegir == 5: #SALIR DEL SISTEMA
        print(separar_menu)
        print("Has cerrado el sistema")
        break
    if elegir == 1: #AGENDAR TURNO
        agendado = "Has Agendado turno correctamente"
        print(separar_menu)
        elegir_dia = input("Eliga el dia para agendar turno (Lunes:1/Marte:2): ")
        while not elegir_dia.isdigit() or int(elegir_dia) <= 0 or int(elegir_dia) > 2: #Validar opcion
                elegir_dia = input("Opcion no valida. Intente otra vez (Lunes:1/Marte:2): ")
        elegir_dia = int(elegir_dia)
        print(separar_menu)
        nombre_paciente = input("Ingrese el nombre del paciente: ") #Nombre del paciente y verificacion
        while not nombre_paciente.isalpha():
            nombre_paciente= input("Nombre no valido. Intente otra vez: ")
        nombre_paciente = str(nombre_paciente)
        if elegir == 1: #Si eligio Lunes
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print(separar_menu)
                print("El paciente ya tiene turno ese dia")
            elif lunes1 == "":
                lunes1 = nombre_paciente
                print(separar_menu)
                print(agendado)
            elif lunes2 == "":
                lunes2 = nombre_paciente
                print(separar_menu)
                print(agendado)
            elif lunes3 == "":
                lunes3 = nombre_paciente
                print(separar_menu)
                print(agendado)
            elif lunes4 == "":
                lunes4 = nombre_paciente
                print(separar_menu)
                print(agendado)
            else:
                print(separar_menu)
                print("No hay turnos este dia")
        if elegir == 2: #Si elegio Martes
            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print(separar_menu)
                print("El paciente ya tiene turno ese dia")
            elif martes1 == "":
                print(separar_menu)
                print(agendado)
                martes1 = nombre_paciente
            elif martes2 == "":
                print(separar_menu)
                print(agendado)
                martes2 = nombre_paciente
            elif martes3 == "":
                print(separar_menu)
                print(agendado)
                martes3 = nombre_paciente
            else:
                print(separar_menu)
                print("No hay turno este dia")
    if elegir == 2: #CANCELAR TURNO
        cancelar = "Has Cancelado el turno correctamente"
        print(separar_menu)
        elegir_dia = input("Eliga el dia para cancelar turno (Lunes:1/Marte:2): ")
        while not elegir_dia.isdigit() or int(elegir_dia) <= 0 or int(elegir_dia) > 2: #Validar opcion
                elegir_dia = input("Opcion no valida. Intente otra vez (Lunes:1/Marte:2): ")
        elegir_dia = int(elegir_dia)
        print(separar_menu)
        nombre_paciente = input("Ingrese el nombre del paciente: ") #Nombre del paciente y verificacion
        while not nombre_paciente.isalpha():
            nombre_paciente= input("Nombre no valido. Intente otra vez: ")
        nombre_paciente = str(nombre_paciente)
        if elegir_dia == 1: #LUNES
            if nombre_paciente == lunes1:
                lunes1 = ""
                print(separar_menu)
                print(cancelar)
            elif nombre_paciente == lunes2:
                lunes2 = ""
                print(separar_menu)
                print(cancelar)
            elif nombre_paciente == lunes3:
                lunes3 = ""
                print(separar_menu)
                print(cancelar)
            elif nombre_paciente == lunes4:
                lunes4 = ""
                print(separar_menu)
                print(cancelar)
            else:
                print(separar_menu)
                print("No se encontro paciente este dia")
        if elegir_dia == 2: #MARTES
            if nombre_paciente == martes1:
                martes1 = ""
                print(separar_menu)
                print(cancelar)
            if nombre_paciente == martes2:
                martes2 = ""
                print(separar_menu)
                print(cancelar)
            if nombre_paciente == martes3:
                martes3 = ""
                print(separar_menu)
                print(cancelar)
    if elegir == 3: #AGENDAS DEL DIA
        print(separar_menu)
        print("== Agenda del Lunes ==")  #Lunes
        if lunes1 == "":
            print("Turno 1°: Libre")
        else:
            print(f"Turno 1°: {lunes1}")
        if lunes2 == "":
            print("Turno 2°: Libre")
        else:
            print(f"Turno 2°: {lunes2}")
        if lunes3 == "":
            print("Turno 3°: Libre")
        else:
            print(f"Turno 4°: {lunes4}")
        if lunes4 == "":
            print("Turno 4°: Libre")
        else:
            print(f"Turno 4°: {lunes4}")
        print("== Agenda del Martes ==") #Martes
        if martes1 == "":
            print("Turno 1°: Libre")
        else:
            print(f"Turno 1°: {martes1}")
        if martes2 == "":
            print("Turno 2°: Libre")
        else:
            print(f"Turno 2°: {martes2}")
        if martes3 == "":
            print("Turno 3°: Libre")
        else:
            print(f"Turno 3°: {martes3}")
    if elegir == 4: #RESUMEN GENERAL
        ocupados_lunes = 0
        ocupados_martes = 0
        if lunes1 != "": #Lunes
            ocupados_lunes = ocupados_lunes + 1
        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1
        if martes1 != "": #Martes
            ocupados_martes = ocupados_martes + 1
        if martes2 != "":
            ocupados_martes = ocupados_martes + 1
        if martes3 != "":
            ocupados_martes = ocupados_martes + 1
        libres_lunes = 4 - ocupados_lunes #Resumen general
        libres_martes = 3 - ocupados_martes
        print("== Resumen general ==") 
        print(f"Lunes: ocupados={ocupados_lunes}  libres={libres_lunes}")
        print(f"Martes: ocupados={ocupados_martes}  libres={libres_martes}")
        if ocupados_lunes > ocupados_martes: #Dia con mas truno
            print("Dia con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con más turnos ocupados: Martes")
        else:
            print("Dia con más turnos ocupados: Empate")

#EJERCICIO N°4 "ESCAPE ROOM LA BOVEDA"

energia = 100
tiempo = 12
cerradura_abierta = 0
alarma = False
codigo_parcial = ""
separar_menu = "===================="
forzar = 0
bloqueo_alarma = False
nombre = input("Hola agente. Ingrese su nombre: ")
while not nombre.isalpha(): #Validar nombre
    nombre = input("Solo se permiten letras. Intente otra vez: ")
nombre = str(nombre)
while 1 == 1:
    if energia > 0 and tiempo > 0 and cerradura_abierta < 3:
        print(separar_menu)
        print("1°_Forzar Cerradura")
        print("2°_Hackear Panel")
        print("3°_Descansar")
        print("")
        elegir = input("Eliga opcion: ") #Elejir opcion
        while not elegir.isdigit() or int(elegir) <= 0 or int(elegir) > 3: #Validar opcion
            print(separar_menu)
            elegir = input("Opcion no valida. Intente otra vez: ")
        elegir = int(elegir)
        if elegir == 1: #FORZAR
            if energia >= 40: #Si tiene energia normal
                print(separar_menu)
                print("Has forzado la cerradura exitosamente")
                forzar = forzar + 1
                energia = energia - 20
                tiempo = tiempo -2
                cerradura_abierta = cerradura_abierta + 1
            if energia < 40: #Si tiene energia para activar alarma
                print(separar_menu)
                energia = energia - 20
                tiempo = tiempo -2
                forzar = forzar + 1
                print("Hay Riegos de activar la alarma")
                riesgo_alarma = input("Ingrese un numero del 1 al 3: ")
                while not riesgo_alarma.isdigit() or int(riesgo_alarma) <= 0 or int(riesgo_alarma) > 3: #Validar opcion
                    print(separar_menu)
                    riesgo_alarma = input("Opcion no valida. Intente otra vez: ")
                riesgo_alarma = int(riesgo_alarma)
                if riesgo_alarma == 1 or riesgo_alarma == 2: #Si adivina
                    print(separar_menu)
                    print("Has forzado la cerradura exitosamente")
                    cerradura_abierta = cerradura_abierta + 1
                elif riesgo_alarma == 3:
                    print(separar_menu)
                    print("No has podido adivinar correctamente y has ACTIVADO LA ALARMA!")
                    alarma = True
            if forzar == 3: #Si forza 3 veces seguidas 
                energia = energia - 20
                tiempo = tiempo -2
                print(separar_menu)
                print("la cerradura se travo y has ACTIVADO LA ALARMA")
        if elegir == 2: #HACKEAR PANEL
            forzar = forzar - 1
            energia = energia - 10
            tiempo = tiempo - 3
            print(separar_menu)
            for i in range(1,4+1):
                if i == 1:
                    print("Hackeando ....")
                print(f"Completando {i}/4")
                codigo_parcial = codigo_parcial + "A"
            codigo_parcial = input("Ingrese alguna letra: ")
            while not codigo_parcial.isalpha(): #Validar codigo
                codigo_parcial = input("Solo se permiten letras. Intente otra vez: ")
            codigo_parcial = str(codigo_parcial)
            if len(codigo_parcial) < 8: #Si todavia no logra 8 "A"
                print("")
                print("Has logrado completar una parte del codigo")
            if len(codigo_parcial) >= 8: #Una vez logrado abre uan cerradura
                print("")
                print("Has logrado completar el codigo")
                cerradura_abierta = cerradura_abierta + 1
        if elegir == 3: #DESCANSAR
            forzar = forzar - 1
            print(separar_menu)
            if alarma == False: #Si la alarma esta pagada
                tiempo = tiempo - 1
                if energia < 100: #Se pude descansar
                    energia = energia + 15
                    if energia > 100: 
                        energia = 100
                elif energia >= 100: #Ya tiene toda la energia
                    print("Ya tener la energia completa")
            if alarma == True:
                energia = energia - 10
                print("La alarma esta activada. Perdes 10 de energia")
        if alarma == True and tiempo <= 3: #BLOQUEO
            bloqueo_alarma = True
    if cerradura_abierta == 3: #VICTORIA
        print(separar_menu)
        print("¡VICTORIA!")
        break
    if energia <= 0 or tiempo <= 0: #DERROTA
        print(separar_menu)
        print("¡DERROTA!")
        break
    if bloqueo_alarma == True:
        print(separar_menu)
        print("Se ha bloquedo la boveda")
        print("¡DERROTA!")

#EEJERCICIO N°5 "BATALLA DE GLADIADOR"

vida_gladiador = 100
vida_enemigo = 100
posiones = 3
danio_base = 15
danio_enemigo = 12
turno_gladiador = True
separar_menu = "--------------------"
print("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Bienvenido Gladiador. Ingrese su nombre: ")
while not nombre_gladiador.isalpha(): #Validar nombre
    nombre_gladiador = input("Solo se permiten letras. Intente otra vez: ")
nombre_gladiador = str(nombre_gladiador)
print("=== INICIO DEL COMBATE ===")
while 1 == 1:
    if vida_gladiador > 0 and vida_enemigo > 0:
        if turno_gladiador == True: #MENU REPETITIVO
            print("=== NUEVO TURNO === ")
            print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {posiones} ")
            print("")
            print("1°_Ataque Pesado")
            print("2°_Rafaga Veloz")
            print("3°_Curarse")
            print("")
            elegir = input("Eliga opcion: ") #Elejir opcion
            while not elegir.isdigit() or int(elegir) <= 0 or int(elegir) > 3: #Validar opcion
                print(separar_menu)
                elegir = input("Opcion no valida. Intente otra vez: ")
            elegir = int(elegir)
        if elegir == 1: #ATAQUE PESADO
            print(separar_menu)
            turno_gladiador = False
            print(">> Lanzas un Ataque Pesado")
            if vida_enemigo < 20: #Golpe critico
                danio = danio_base * 1.5
                danio = float(danio)
                print("> ¡Golpe critico!")
            else: #Golpe normal
                danio = danio_base 
            vida_enemigo = vida_enemigo - danio
            print(f"> Atacaste al enemigo por {danio} puntos de vida")
            if turno_gladiador == False: #Turno del enemigo
                if vida_gladiador > 0:
                    vida_gladiador = vida_gladiador - danio_enemigo
                    print(f">> El enemigo te ataca por {danio_enemigo}")
                turno_gladiador = True
        if elegir == 2: #ATAUE DE RAFAGA
            print(separar_menu)
            turno_gladiador = False
            print(">> Lanzas una Rafaga de Ataque Veloz")
            for i in range(3):
                print("> Golpe conectado por 5 de daño")
                vida_enemigo = vida_enemigo - 5
            if turno_gladiador == False: #Turno del enemigo
                if vida_gladiador > 0:
                    vida_gladiador = vida_gladiador - danio_enemigo
                    print(f">> El enemigo te ataca por {danio_enemigo}")
                turno_gladiador = True
        if elegir == 3: #CURARSE
            print(separar_menu)
            turno_gladiador = False
            if posiones > 0: #SI TIENE POCIONES
                print(">> Has tomado una pocion (+30 HP)")
                posiones = posiones - 1
            else: #NO TIENE POCIONES
                print(">> No tiene pociones")
                if turno_gladiador == False: #Turno del enemigo
                    if vida_gladiador > 0:
                        vida_gladiador = vida_gladiador - danio_enemigo
                        print(f">> El enemigo te ataca por {danio_enemigo}")
                    turno_gladiador = True
    if vida_enemigo <= 0: #GANAS
        print(separar_menu)
        print(f"¡VICTORIA! .{nombre_gladiador} ha ganado la batalla")
        break
    if vida_gladiador <= 0: #PERDES
        print(separar_menu)
        print(f"¡DERROTA! .Has caigo en batalla")
        break