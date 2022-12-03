
#NOTAS: Me disculpo por la entrega tardia, tuve algunos problemas de ultimo momento 😥😥

# Librerias utilizadas
import string, random
import time
import pandas as pd
import numpy as np


def Bienvenida():
  #Explica las reglas de juego y como jugar
  print('<---------BIENVENIDO--------->')
  print('***....Vamos a jugar STOP....***')
  print(" ")
  print(" ")
  print("COMO SE JUEGA")
  print("")
  print("1. Ingresas el número de partidas que quieres jugar")
  print(
    "2. Se te dara una letra aleatoriamente por cada nueva partida y tú deberas ingresar una serie de datos que te pide el programa, que inicien con dicha letra"
  )
  print(
    "3. Debes ingresar la palabra en MAYUSCULA, de lo contrario no te dara puntos"
  )
  print(
    "4. Una vez termines de ingresar los datos para cada categoria, el programa evaluara que las palabras comiencen con la letra indicada"
  )
  print(" ")
  print(" ")
  print('***....MANEJO DE PUNTAJE....***')
  print("Si inicia con la letra correcta:               +100 puntos")
  print("Si inicia con la letra diferente a la indicada: 0 puntos")
  print(" ")
  print(" ")


def decisionUsuario():
  print("¿Quieres jugar?")
  print("")
  ready = str(input("Digita (S) para Si o (N) para No "))
  print("")
  print("")
  if ready.upper() == "S" or ready.upper() == "SI":
    print("Excelente decisión ¡VAMOS A JUGAR!")
    print("")
    return True

    letra = Aleatorio()

  elif ready.upper() == "N" or ready.upper() == "NO":
    print("La próxima tal vez seas más valiente ¯\_(ツ)_/¯")

  else:
    print("Digitaste una opción no valida")


#Generar letra aleatoria
def Aleatorio():
  letra = random.choice(string.ascii_letters)
  return letra.upper()


#Funcion principal
def Juego():
  #Se crean los arrays
  Nombre = []
  Apellido = []
  Ciudad = []
  Fruta = []
  Cosa = []
  Color = []
  Animal = []
  puntajeFinalPartida = []
  Tiempotrans = []
  

  #Creando los contadores
  puntajefinal = 0
  tiempofinal = 0
  puntaje = 0

  for i in range(partidas):
    letra = Aleatorio()
    print("Juegas con la letra " + letra)
    #Reinicia el contador (para la nueva partida)
    puntajepartida = 0
    tiempo = 0

    

    inicio = time.time()
    Nombre.append(str(input("Nombre con " + "  " + letra.upper() + "  ")))

    for i in range(len(Nombre)):
      inicio = time.time()
      if Nombre[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Apellido.append(str(input("Apellido con " + letra.upper() + "  ")))
    
    for i in range(len(Apellido)):
      if Apellido[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Ciudad.append(str(input("Ciudad con " + letra.upper() + "  ")))
    
    for i in range(len(Ciudad)):
      if Ciudad[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Fruta.append(str(input("Fruta con " + letra.upper() + "  ")))
    
    for i in range(len(Fruta)):
      if Fruta[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Cosa.append(str(input("Cosa con " + letra.upper() + "  ")))
    
    for i in range(len(Cosa)):
      if Cosa[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Color.append(str(input("Color con " + letra.upper() + "  ")))
    
    for i in range(len(Color)):
      if Color[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    Animal.append(str(input("Animal con " + letra.upper() + "  ")))
    
    for i in range(len(Animal)):
      if Animal[i][0] == letra:
        puntaje = 100
        puntajepartida = puntaje + puntajepartida
      else:
        puntaje = 0

    tiempo = time.time() - inicio
    #Redondear el tiempo
    tiemporedondo = int(tiempo)

    #Calculos
    Tiempotrans.append(tiemporedondo)
    puntajeFinalPartida.append((puntajepartida))
    puntajefinal = puntajepartida + puntajefinal
    tiempofinal = tiemporedondo + tiempofinal
    print("Tu puntaje en la partida", (i + 1), "fue de: ",
          puntajeFinalPartida[i])
    print("Tu tiempo en esta partida fue de: ", Tiempotrans[i], "Seg")
    #Creando la tabla
    numpartida= i+1
    
    
    print("")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    tablaPartida = pd.DataFrame()
    tablaPartida["Letra"] = letra[i-1]
    tablaPartida["Nombre"] = Nombre
    tablaPartida["Apellido"] = Apellido
    tablaPartida["Ciudad"] = Ciudad
    tablaPartida["Fruta"] = Fruta
    tablaPartida["Cosa"] = Cosa
    tablaPartida["Color"] = Color
    tablaPartida["Animal"] = Animal
    tablaPartida["Puntaje"] = puntajeFinalPartida[i]
    tablaPartida["Tiempo"] = Tiempotrans[i]
    print(tablaPartida)

    tablaFinal = pd.DataFrame()
    tablaFinal["Letra"] = letra[i-1]
    tablaFinal["Nombre"] = Nombre
    tablaFinal["Apellido"] = Apellido
    tablaFinal["Ciudad"] = Ciudad
    tablaFinal["Fruta"] = Fruta
    tablaFinal["Cosa"] = Cosa
    tablaFinal["Color"] = Color
    tablaFinal["Animal"] = Animal
    tablaPartida["Puntaje"] = puntajeFinalPartida[i]
    tablaPartida["Tiempo"] = Tiempotrans[i]
    tablaFinal["Puntaje Final"] = puntajefinal
    tablaFinal["Tiempo Total"] = tiempofinal
    
    
  print("")
  print("--------------------------------------------------------------")
  print("--------------------------------------------------------------")


    
  print("")
  print("--------------------------------------------------------------")
  print("--------------------------------------------------------------")
  print("Mira tus respuestas 👀")
  print("--------------------------------------------------------------")
  print("--------------------------------------------------------------")
  print("")

    
  
  print(tablaFinal)


def Despedida():
  print("------------------------------------")
  print("------------------------------------")
  print("")
  print("GAME OVER 🤗")
  print("")
  print("------------------------------------")
  print("------------------------------------")
  print("")
  print(nombre.upper(), " GRACIAS POR JUGAR, HASTA LA PROXIMA!")
  print("")
  print("------------------------------------")
  print("------------------------------------")


#Donde llamamos las funciones y se ejecuta todo correctamente
ingresar = Bienvenida()
ready = decisionUsuario()
if ready == True:
  nombre = str(input("Para comenzar, ingresa tu nombre: "))
  partidas = int(input("¿Cuántas partidas estás dispuesto a jugar? "))
  Jugar = Juego()
  salir = Despedida()
else:
  print("GAME OVER ☠")
