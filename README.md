
# AsistenteVirtual
A.L.I.C.E (Artificial Loli, it is complex and efficient)
Alicia es una asistente virtual escrita principalmente en python, actualmente cuenta con funciones muy básicas.

## Comandos:
- Leer (Lee un texto que tengas copiado en el portapapeles)
- Traducir (Traduce un texto copiado en el portapapeles del ingles al español y luego lo lee)
- Salir (Cierra la ejecución del programa)
- Hora (Te dice la hora xD)
- Que es (Busca en wikipedia y te lee la primera definición que encuentra)
- Busca (Abre youtube y abre el navegador con los resultados de tu busqueda)
- Abre (Abre programas y paginas web)
- Vamos a programar (Inicia el ide de programacion Atom, si no tienes atom dará una exepcion asi que mejor no usar este comando)

## Chat de voz:
Al hablarle comparará lo que dices con alguna respuesta de la base de datos y buscara la mejor coincidencia, si la respuesta que te da no te gusta puedes agregarla en el archivo dialogos.txt con el siguiente formato.

### pregunta o lo que tu vas a decir:
### respues1
### respuesta2
### respuesta3

Puedes agregar las respuestas que quieras, el asistente virtual eligirá una respuesta de forma aleatoria.

# Requisitos
- python 3.8.0
- speech_recognition
- pyttsx3
- datetime
- wikipedia
- TextBlob
- os
- subprocess
- time
- pyperclip
- random

Muchas de estas librerías se pueden instalar facilmente con el comando ($ pip install nombreLibrería) en la CMD.
Otras como datetime, os, subprocess, time y random vienen por defecto en la packeteria de python.

# Finalmente
Aún falta agregarle un montón de cosas y pulir mejor el código, ya se corregirá con el tiempo, tengan paciencia.
La idea es implementar POO para un mejor mantenimiento para próximas versiones.
