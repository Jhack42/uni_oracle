import pyttsx3

def decir_en_voz_alta(mensaje):
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()
