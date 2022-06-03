#comentarios son lineas que no se ejecutan y son dd uso del programador

#aqui modifique algo
#print('hola')

'''print('hola')print('hola')
print('hola')
print('hola')
print('hola')
print('hola')'''

#contantes tiene informacion que NO cambia 

pie=3.1416

#variables por que la informacion que contiene PUEDE cambiar

fecha=7
fecha=8

#####ejemplo de comentar una liena que no quiero usar ahorita######
#while True
 #fecha=fecha+1

#tipos de datos

#INT o intergers o enteros

entero=456

#FLOAT o floting o foltantes

flotante=456.5

#string o cadenas

ejmplo1="hola k ace"
ejmplo2='nada tomo clase'
ejmplo3="123445344 y letras ejdimdwimwjuqksqoxmjedhbi"

#bool o boolean o boleanos estos evaluan un falso o verdadero

aprobado=True
reprobartodogrupo=False

#comandos

#print(mensaje): es mandar a la CONSOLA informacion del codigo

#print para imprimir datos ya guardados en variable/const
print(ejmplo1)
print(ejmplo2)
print(ejmplo3)
print(fecha)

print('hola k ace')
print(3234)

#print para imprimir algo directamente 
print('hola k ace')
print(32345345)

#print combinado

print('el mensaje enviado fue: ', ejmplo1)
print(fecha, " de Enero")

#input() permite que el USUARIO ingrese informacion al CODIGO, el codigo no avanza hasta que detecte un enter del teclado


nombre=input()
print("hola ", nombre)

apellido=input('ingrese su apellido')
print("su nombre completo es ", nombre, apellido)

#SOLO INGRESA CADENAS (STRINGS)

num=input('ingrese numero')
print('el numero 10 veces es:,(10*num)')

#int() sirve para convertir una STRING en INT 
#float() sirve para convertir una STRING en una FLOAT
num=int(input('ingrese numero'))
print('el numero 10 veces es: ',(10*num))

#while(): es una estructura que permite repetir un codigo practicamente de forma infinita 

#evaluan para falso o verdadero

while True:
  input()
  print("hola")'''

#comparadores 

# == identifico
  # >< mayor o menor 
  #!= diferente 
  # >= o <= mayor o igual menor o igual

  zeta=int(input("numero: "))

  while (zeta>=5):
   print("tu numero es mayor o igual que 5")

  pasw=input("password: "):
  while (pasw!='hola'):
   print("volver a intentar")