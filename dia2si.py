

def suma(sum1, sum2):#definir la funcion suma
    resultado_sum=sum1+sum2#hacer el calculo aqui
    return resultado_sum# le decimos que retorne el resultado

print (suma(3,8))# le pedimos que imprima el resultado de 3 y 8

def multiplica(mul1, mul2):
    resultado_mul=mul1 * mul2
    return resultado_mul

print (multiplica(6,8))

def porcent(valor, porcentaje):# defino  la funcion que es porncent
    resultado= valor * porcentaje/100#hago el calculo del porcentaje
    return resultado# devolver el resultado
print(porcent(10000,30))#ak imprime el porcentaje, para eso se carga los numeros, total y porcentaje

def porcenta(valor1, porcentaje1):
    resultado_porc= valor1 * porcentaje1/100
    return resultado_porc
print (porcenta(50000,40))


#crear una funcion saludo2 que reciba como parametro nombre y edad
#e imprima "Hola soy---y tengo----anos"
#llamar varias veces a la funcion con distintos valores
#nota: retornar algo es opcional

def saludo2(nombre, edad):
    print("hola me llamo",nombre,"y tengo",edad,"anhos")

saludo2("fatima",34)

 #Ejercicio. crear una funcion suma_lista que reciba como argumento
 #una lista de numeros  y retorne la suma de sus elementos
 #Pista: Usar for y una variable acumular

listita=[1,2,3,4,5]
def suma_lista(listita):
    a=0
    for x in listita:
        a=a+x# el resultado se acumula en a y se suma a mas x, x es lo que hay en la listita
    print(a)

suma_lista(listita)

#ej2 Lista al cuadrado
# crear una funcion que reciba una lista de numeros como parametro
# y retorne una lista con los numeros al cuadrado
#lista_cuadrado (listita) [1,4,9,16,25]

print("----------------------------")

listin= [1,4,9,16,25]
def lista_cuadrado(lista):
    lista_cuadrados=[]
    for x in lista:
        a=x*x
        lista_cuadrados.append(a)
    print (lista_cuadrados)
lista_cuadrado(listin)



print("----------------------------")
def lista_cuadra(listajeyma):
    a=[]
    for jeyma in listajeyma:
        a.append(jeyma*jeyma)
    return a
otravez= [1,4,9,16,25]
resultado_cuad=lista_cuadrado(otravez)
print(resultado_cuad)

print("_______________________________")




vaso=["agua","gaseosa","leche"]
def botella(envase):
    for x in envase:
        print ("vaso de",x)
botella(vaso)   

#########
print("---------------------------")
grupo5=["N","F1","f2","A"]
for j in range(len(grupo5)):
    grupo5.pop()
print("despues",grupo5)
grupo5.append("p")
print(grupo5)
print("---------------------------")

# crear una funcion suma_cuadrado que reciba una lista de numeros
#y retorne el valor de la suma de cada numero al cuadrado
#[1,2,3,4]------1+4+9+16


print("----------------------------")



#########################
# es otra forma de resolver el problema anterior
suma_lista(lista_cuadrado([1,2,3,4]))

list_numeros=[1,2,3,4]
def suma_cuadrado(lista_n):
    suma=0
    for p in lista_n:
        suma=suma +(p*p)
    return suma
print (suma_cuadrado(list_numeros))








    

 



    



print("-------------------")#suma el resultado total 





