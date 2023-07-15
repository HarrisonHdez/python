# and, or, not

# gas = True
# encendido = True

# if gas and encendido:
#     print("Puedes Avanzar")

# gas = True
# encendido = False

# if gas or encendido:
#     print("Puedes Avanzar")


# gas = False
# encendido = True
# edad = 18

# if not gas and (encendido or edad > 17):
#     print("Puedes Avanzar")


# Operaciones de corto-circuito


# En python al usar and todo tiene que dar true para que se ejecute y si el valor de la izquierda es false entonces python no va ejecuar el valor de la derecha
# gas = False
# encendido = True
# edad = 18

# if not gas and encendido and edad > 17:
#     print("Puedes Avanzar")

# En python al usar or una de las dos tiene que ser true y basta con que la primera sea true, en caso de que sea false y la segunda sea true entonces se va a evaluar la segunda

gas = False
encendido = True
edad = 18

if not gas or encendido or edad > 17:
    print("Puedes Avanzar")
