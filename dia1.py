print(7+3) # todo lo que sea py es extesion de python
print(2*2) # abrir simpre parentesis para ejecutar algo
print(2+2) # no usar espacio, sirve para sumar numeros
print("Hola Mundo!!!") # usar comillas en este caso sirve para imprimir el contenido que esta entre comillas
print("Hola Mundo penguin")
print("hola " * 10) # multiplica 10 veces la palabra hola, en este caso deja un espacio antes de la ultima comilla
print("hola como estas") # print es una funcion para imprimir en pantalla
# variables: es un lugar donde guardas un valor, es un espacio, un valor
# como crear una variable en python  a= 2*8
a= 5
b= 3
c= 10
d= 2
print(a)#imprime al valor de la variable a que es 5
print(b)# imprime el valor de la variable b que es 3
print(c)
#print(d)
#print(a+b)
print(a+b+c+d)#suma el valor de cada una de las variables
#print("hola" + 2) #no puede sumar numeros mas letras str +int
print("hola", 2, "Chau", 10)
#Ejericicio. Crear una variable nombre  y una variable edad
# con sus nombres y edades y despues imprimir:
# hola, me llamo ---- y tengo --- a
nombre="Fatima" # el resultado de la variable va ir dentro de comillas
edad="34" # edad en este caso es una variable
#hijos="2 hijos" #sirve en este caso pero no anda para sumar variables
hijos="2" + " hijos" # el resultado es 2 hijos
# para imprimir distintos valores separamos con coma, y luego ejecutar
# todo lo que va entre comillas va imprimir en la pantalla con el print
domicilio="Blas Garay" 
print("hola me llamo",nombre,"tengo",edad,"anhos",)# no usar espacio, si da error mirar en que linea da el error
print("hola me llamo",nombre,"tengo",edad,"anhos","vivo en",domicilio,)
print("hola me llamo",nombre,"tengo",edad,"anhos","vivo en",domicilio,"tengo",hijos,)
# variables... cajas donde guardamos las cosas..
#########
#listas Corchete en python [] 
# la lista es para guardar varios valores. las listas funcionan por posicion
#todo arranca con cero
#nombre=
datos=["Marce"]
print(datos)
alumnos=["Jose","Ramocito", nombre, "Maria"] #lista de alumos
#nro_alumno=3
print(alumnos[2],alumnos[0])

#Ej. Crear una lista datos que en el primer lugar este tu nombre y
# y en la segunda posicion este tu edad
#Imprimir "HHola me llamo ---, y tengo --- anhos"

datos=["Fatima","34"] # lista["Fatima","34"]
print("hola yo me llamo",datos[0],"y tengo",datos[1],"anhos")

#Ejercicios
cajero=["Noelia","Maria","Jose","Ruben","Kim"]
print("Hola le atendio",cajero)
print("Hola le atendio",cajero[3])
print("Hola le atendio",cajero[1])

datos[1]=45# ak accedo a la edad de fatima, era 34 ahora le asigno 45 
print("hola yo me llamo",datos[0],"y tengo",datos[1],"anhos")

cajero[4]="Zulma"
print(cajero[4])

print("Hola le atendio",cajero[4])# cajero de la lista numero 3

#datos.append = agrega al final, enn el ultimo elemento

print(datos)
datos.append("Pastelera")
print(datos) # imprimimos la lista datos que tiee 2 elementos
#agregamos con.append() el string "pastelera" a la lista

#Ejercicio Agregar una profesion y un hobby a la lista datos
#previamente creada (usar append)
# #imprimir la lista)

datos.append("Cocinera") #agrega a la lista de datos cocinera en ultimo lugar
print(datos)

datos.append("Cantante")
print(datos) #imprime catante al final de la variable datos

datos.append("dibujante")# datos.append agrega, abrir parentesis comilla escribir el dato cerrar comilla y parentesis

print(datos)# se puede agregar todo e imprimir solo una vey

datos.pop()# datos.pop elimina el ultimo en la lista....
print(datos)# palabra reservada print
datos.pop()
datos.pop()
datos.pop(1)

datos.append("Campametista")
datos.append("Jornadista")
####
#Funcion len() = Lenght obtiene la longuitud de cualquier cosa. la cantidad de caracteres
dimension_de_datos=len(datos)
print(dimension_de_datos)
print(datos)
print(len(datos))
saludo="Hola, que tal"
print(saludo)
print(len(saludo))

#ejercicio. obtener la dimension de la lista datos e imprimir
#la lista datos tiene --- elemetos

print(len(datos))
print(datos)
print(len(datos))
print(datos)
print(len(datos[0]))
print(len(datos[1]))
print(len(datos))
print("la lista datos 1 tiene",len(datos[1]),"elementos")
#la lista datos de la ubicacion 1 tiene 9 elementos Pasteleria

#Imprimir el ultimo elemento de la lista sin saber cuantos elemetos tiene

print(len(datos)-1)# nos da el ultimo elemento
print(datos[len(datos)-1]) #indice del ultimo elemento
 
indice_ultimo = len(datos)-1
print(datos[indice_ultimo]) #identacion. error de tabulacion, espacio al pricipio

#############################
#### Bucles / loops / ciclos / Iteraciones
# despues de dos puntos es un bloque de codigo. tabulado, sangria,espaciado
lista_temas=["variables","listas","tipos de datos"]
for concepto in lista_temas:# el for termina en dos puntos
    print("hoy aprendi", concepto) # concepto es una variable temporal de for
    print("que gusto")
print("esto es lo que apredi hoy")

for variable_for in lista_temas:
    #bloque de codigo
    print("esto se repite")
print("esto no se repite")

## recorrer una lista con for e imprimir en cada ciclo
# el valor del elemento con 3 signos de admiracion y al final 
#fuera del bucle FIN
# Ej: variables
datos.append("profesora")
datos.append("catequista")
datos.append("viajera")

for concepto in datos:   # CONCEPTO ES EL NOMBRE DE LA VARIABLE TEMPORAL
    print("soy", concepto,"!!!")
    print("!!!")
    print("lo estoy logrando")
print("FIN!!!")

print(len(datos))# para contar cuantos valores tiene datos,,, es 7 ahora

#crear una lista 
lista_corta= ["linda", "genial", "amable", "buena"]

for significa in lista_corta:
    print ("soy", lista_corta)
    print ("!!!")
print("FIN")

 #eJERCICIO Imprimir los numeros del 01 al 100 usando for y range
for x in range(10):
    print("numero",x)

for x in range(1,11): # para impri mir del 1 al 10 se usa coma y usar del 1 al 11
    print("numero",x) # numero se va imprimir antes de cada numero

for x in range(1,101): # parametros del 1 al 100 va imprimir
    print(x)

#desafio
#ejercicio2, imprimir el resutado de la suma de los numeros
# del 1 al 10 usando range 1+2+3+4+5+7+8+9+10
print("------------------------------")
desafio=[1,2,3,4,5,6,7,8,9,10]#creo una variable de base
a=0
for x in desafio:
    a=a+x
print(a)
print("-------------------")#suma el resultado total 55

for significa in lista_corta:
    print (significa,("!!!"))
print("FIN")

print(lista_corta)
lista_corta.append("divina")
print(lista_corta)

#######
def suma(num1, num2):
    resultado=num1+num2
    return resultado

#equivalente al de arriba
def suma2(num1, num2):
    return num1 + num2

print (suma(5,10))
resul=suma(5,8)
print(result)

# crear una funcion

#def resta(res1,res2):
 #   resul_resta=res1-res2
    return resul_resta


#def restaa(rest1,rest2):
 #   return rest1-rest2




print(lista_corta)#imprimos el contenido de lista corta
dim_lista=len(lista_corta)# le passamos a dimlista la dimension de lista corta
print(lista_corta)#imprimos la dimension de la lista
ultimo_lista=dim_lista-1#
print(ultimo_lista)#aca imprimimos el numero de elementos
print(lista_corta[ultimo_lista])# aca imprimimos el ultimo


print(lista_corta)
print(len(lista_corta))
print(len(lista_corta)-1)


# todo esto anda super bien, es un buen ejemplo.....

