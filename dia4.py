numero_secreto = 7
adivino = False
while adivino == False:
    apuesta = input ("adivina el numero secreto del 1 al 10")

    if int(apuesta) == numero_secreto:
        print ("Ganaste")
        adivino = True
    else:
        print("segui participante nde arruinado")
#######
#ej. crear un juego de adivinar el num7ero como el de arriba y
# darle pistas al usuario si el numero que ingreso es mayor o menor
# al numero a adivinar
# pista usar elif


from random import randint 

numero_adivinar = randint(0,10)
adivinaste = False

while adivinaste == False:
    numero_apostado = input("ingresa el numero secreto del juego ")
    if int(numero_apostado) == numero_adivinar:
        print("Ganaste, 100.000")
        adivinaste = True
    elif int(numero_apostado) < numero_adivinar:
        print("ingrese un numero mas grande")
    elif int(numero_apostado) > numero_adivinar:
        print("ingrese un numero mas pequeno")

# Ej. Buscar como generar un numero aleatorio para numero_secreto










# buscar como generr un numero aleatoio para numero_secreto