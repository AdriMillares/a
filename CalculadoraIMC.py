# Tarea IMC

# Libreria para el tiempo
import time 

# Declaramos la lista con sus valores
datos = ['Oscar', 'Andrade', 18, 65, 1.68]
# Hacemos el calculo del IMC con la formula masa/altura^2
imc = datos[3]/(datos[4]*datos[4])
# Comenzamos con los comandos de salida para la interfas del programa.
print("Calculadora de IMC")
# Imprimimos el nombre y apellido(s)
print("¡Hola,", datos[0],datos[1],"!")
# Imprimimos el peso
print("Tu peso registrado es de:",datos[3],"kg")
# Imprimimos la altura
print("Tu altura registrada es de:",datos[4],"mts")
# Imprimimos el IMC, con unicamente dos decimales
print("De acuerdo con estos datos tu IMC es de:","{:.2f}".format(imc), "y indica: ")
# Ponemos las condiciones para ver en que rango de peso esta la persona
if imc < 18.5:
    print("Peso bajo")
elif (imc >= 18.5 and imc < 25):
    print("Peso normal")
elif (imc >= 25 and imc < 30):
    print("Sobrepeso")
else:
    print("Obesidad")
# Damos una explicacion de como interpretar los resultados
print("Como leer los resultados.")
print("Niveles de peso deacuerdo al IMC:")
print("IMC por debajo de 18.5: Peso bajo")
print("IMC entre 18.5 - 24.9: Peso normal")
print("IMC entre 25 - 29.9: Sobrepeso")
print("IMC de mas de 30: Obesidad")
print("Creado el:")
# Comandos para mostrar la fecha y hora
print("Fecha:",time.strftime("%d/%m/%y"))
print("Hora:",time.strftime("%H:%M:%S"))
# Imprimimos el nombre del creador del programa
print("Por: Oscar Andrade")