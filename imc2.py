# Programa para el cálculo del IMC

# Función para el cálculo del IMC
def calculo_imc(masa, estatura):
    return masa / pow(estatura , 2)

def calculo_interpretacion_imc(imc):
    interpretacion_imc = ""
    if imc < 18.5:
       interpretacion_imc = "peso bajo"
    elif imc < 25:
       interpretacion_imc = "peso normal"
    else:
      interpretacion_imc = "sobrepeso"

    return interpretacion_imc

continuar = True
while continuar == True:

    # Entrada

    try:
      masa = float(input("Ingrese la masa: "))
    except:
        print("Por favor, ingrese un número.")
        exit(1)

    try:
      estatura = float(input("Ingrese la estatura:"))
    except:
        print("Por favor, ingrese un número.")
        exit(1)


    # Procesamiento
    imc = calculo_imc(masa, estatura)
    interpretacion_imc = calculo_interpretacion_imc(imc)


    # Salida
    print(f"El IMC tiene un valor de: {imc:.2f}")
    print(f"Este valor de IMC es considerado como: {interpretacion_imc}")

    respuesta_usuario = input("¿Desea calcular el IMC de otra persona? (S/N)")

    if respuesta_usuario == "S":
      continuar = True
    else:
      continuar = False

print("¡Gracias por usar nuestro programa!")
