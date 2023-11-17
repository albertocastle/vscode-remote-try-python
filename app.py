#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

""" Crea un minijuego de consola teniendo como referencia el juego de piedar papel o tijera"""
from random import randint
from time import sleep
opciones = ["piedra", "papel", "tijera"]
mensaje = {
  "empate": "Empate",
  "ganaste": "Ganaste",
  "perdiste": "Perdiste"
}


victorias_usuario=0
victorias_computadora =0 
rondas =0

def decidir_ganador(usuario, computadora):
    global rondas, victorias_usuario, victorias_computadora 
    print("Tu eleccion es: %s" % usuario)
    print("La eleccion de la computadora es: %s" % computadora)
    usuario = usuario.lower()
    rondas = rondas + 1

    if usuario == computadora:
        print(mensaje["empate"])
    elif usuario == opciones[0] and computadora == opciones[2]:
        print(mensaje["ganaste"])
        victorias_usuario = victorias_usuario + 1
    elif usuario == opciones[1] and computadora == opciones[0]:
        print(mensaje["ganaste"])
        victorias_usuario = victorias_usuario + 1
    elif usuario == opciones[2] and computadora == opciones[1]:
        print(mensaje["ganaste"])
        victorias_usuario = victorias_usuario + 1
    elif usuario not in opciones:
        print("Opcion invalida")
    else:
        print(mensaje["perdiste"])
        victorias_computadora = victorias_computadora + 1

def mostrar_puntuacion(victorias_usuario, victorias_computadora, rondas):
    print("Rondas: %s" % rondas)
    print("Usuario: %s" % victorias_usuario)
    print("Computadora: %s" % victorias_computadora)


def jugar():
    usuario = input("Elige una opcion: piedra, papel o tijera: ")
    computadora = opciones[randint(0,2)]
    decidir_ganador(usuario, computadora)

repetir = True 
while repetir:
    jugar()
    respuesta = input("¿Quieres jugar de nuevo? SI / NO: ")
    if respuesta.lower() == "si":
        repetir = True
    elif respuesta.lower() == "no":
        repetir = False
    else:
        print("Opcion invalida")
        repetir = False

mostrar_puntuacion(victorias_usuario, victorias_computadora, rondas)
print("Gracias por jugar")





