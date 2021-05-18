
import speech_recognition as sr #Libreria para escuchar
import pyttsx3 #Libreria para hablar
import datetime
import wikipedia as wiki
from textblob import TextBlob #libreria para traducir
import os
import subprocess as sub
#import threading
import time
import pyperclip
#from pynput import keyboard
import random

#######################################################################

def escuchar():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source, phrase_time_limit=3)
            rec = listener.recognize_google(voice, language="es-ES")
            rec = rec.lower()
            return rec
    except:
        return ""
        print("No se logro conectar a la api de google")

def hablar(texto):
    try:
        engine.say(texto)
        engine.runAndWait()
    except:
        pass

def evaluarWiki(texto):
    try:
        info = wiki.summary(texto, sentences=1, auto_suggest=False)
        print(info)
        hablar(info)
    except:
        resultado = wiki.search(texto, results=1, suggestion=True)
        resultado = resultado[0][0]
        hablar("econtre "+resultado+", te sirve?")
        opc = escuchar()
        if "si" in opc or "sí" in opc:
            info = wiki.summary(resultado, sentences=1, auto_suggest=True)
            hablar(info)

def imprimirMenu():
    menu = [
        "1. Iniciar",
        "2. Ejecutar comando por escrito",
        "3. Salir",
        "4. Conversar",
        "5. cargar dialogo",
        "\n"
    ]

    for opcion in menu:
        print(opcion)

def run(texto):
    if "traducir" in texto:
        texto = pyperclip.paste()
        try:
            texto = TextBlob(texto)
            hablar(texto.translate(to="es"))
        except:
            hablar("No se logro traducir")
    elif "leer" in texto:
        texto = pyperclip.paste()
        hablar(texto)
    elif "salir" in texto:
        return False
    elif "hora" in texto:
        texto = datetime.datetime.now().strftime("%I:%M %p")
        hablar("Son las "+ texto)
    elif "qué es" in texto or "que es" in texto or "quién es" in texto:
        texto = texto.replace("que es", "")
        texto = wiki.summary(texto, sentences=1, auto_suggest = True)
        hablar(texto)
    elif "busca" in texto:
        texto = texto.replace("busca", "")
        Ltexto = texto.split()
        busqueda=""
        for i in Ltexto:
            busqueda = busqueda + "+" + i
        youtube = "https://www.youtube.com/results?search_query="+busqueda
        firefox = "https://www.google.com/search?q="+busqueda
        sub.call(f"start firefox.exe {youtube}", shell=True)
        sub.call(f"start firefox.exe {firefox}", shell=True)
        hablar("Esto encontre en internet sobre"+texto)
    elif "abre" in texto:
        programas = {
            "":""
        }
        sitios = {
            "google":"google.com",
            "youtube":"youtube.com",
            "anime":"https://www3.animeflv.net"
        }
        for i in list(sitios.keys()):
            if i in texto:
                sub.call(f"start firefox.exe {sitios[i]}", shell=True)
                hablar(f"abriendo {i}")
    elif "vamos a programar" in texto:
        sub.call("start Atom", shell=True)
        hablar("ok, esta todo listo")

def cargarDialogo():
    archivo = open("dialogos.txt","r",encoding="utf8")
    linea=archivo.readline()
    dialogo = {}
    while linea != "":
        respuestas = []
        if ":" in linea:
            key = linea[0:-2]
            linea=archivo.readline()
            while ":" not in linea and linea != "":
                respuestas.append(linea[0:-1])
                linea=archivo.readline()

            dialogo.update({key:respuestas})
    archivo.close()
    return dialogo

def procesarClase():
    print("procesar")

def compararTexto(texto1, texto2): #Texto de entrada, texto base de datos
    cantidad2 = len(texto2.replace(" ",""))

    lTexto1 = texto1.split()
    lTexto2 = texto2.split()

    contador = 0
    for a in lTexto1:
        letras1 = len(a)
        for b in lTexto2:
            if a == b:
                contador = contador + len(a)
                lTexto2.remove(a)
                break
            else:
                cadena = ""
                for caracter in a:
                    cadena = cadena + caracter
                    if cadena in b and cadena[0:1] == b[0:1]:
                        contador = contador + 1

    porcentaje = (contador/cantidad2)*100
    return porcentaje
#######################################################################

wiki.set_lang("es")

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.setProperty("rate", 140)

dialogos = cargarDialogo()
preguntas = dialogos.keys()
respuesta = ""

iniciar = True
while iniciar:
    imprimirMenu()
    try:
        opc = int(input(""))
    except:
        opc = "nada"
    if opc == 1:
        comando = escuchar()
        print(comando)
        run(comando)
    elif opc == 2:
        comando = input("comando: ")
        run(comando)
    elif opc == 3:
        #hablar("hasta luego")
        iniciar = False
    elif opc == 4:
        entrada = escuchar()
        print(entrada)
        #conversar(entrada)
    elif opc == 5:
        entrada = escuchar()
        print(entrada)
        if entrada in dialogos:
            respuestas = dialogos.get(entrada)
            respuesta = random.choice(respuestas)
            hablar(respuesta)
        else:
            mejorCoincidencia = [0,""]
            for pregunta in preguntas:
                coincidencia = compararTexto(entrada, pregunta)
                if mejorCoincidencia[0] < coincidencia:
                    mejorCoincidencia[0] = coincidencia
                    mejorCoincidencia[1] = pregunta
            print(mejorCoincidencia)
            if mejorCoincidencia[0]>40:
                respuestas = dialogos.get(mejorCoincidencia[1])
                respuesta = random.choice(respuestas)
                hablar(respuesta)
            else:
                hablar("No tengo una respuesta apropiada para eso")
