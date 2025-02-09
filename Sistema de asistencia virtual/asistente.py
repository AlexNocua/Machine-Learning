from gtts import gTTS
import os
import pygame
import speech_recognition as sr
import io
import webbrowser


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Por favor, habla...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        text_to_speech("El texto reconocido es: " + text, "es-ES")
        print("Texto reconocido: ", text)
        return text
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        text_to_speech("No se consiguio Reconocer", "es-ES")
    except sr.RequestError:
        print("Error en la solicitud al servicio de reconocimiento de voz")


def text_to_speech(text, language):

    try:
        tts = gTTS(text=text, lang="es", slow=False)
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_stream, "mp3") 
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error: {e}")


def comandos():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Por favor, habla...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        # text_to_speech("El texto reconocido es: " + text, "es-ES")
        # print("Texto reconocido: ", text)

        if "abre YouTube" in text.lower():
            text_to_speech("Abriendo YouTube", "es-ES")
            webbrowser.open("https://www.youtube.com")

        elif (
            "abre el navegador" in text.lower()
            or "abre el navegador web" in text.lower()
        ):
            text_to_speech("Abriendo el navegador", "es-ES")
            webbrowser.open("https://www.google.com")

        elif "abre el mapa" in text.lower():
            text_to_speech("Abriendo Google Maps", "es-ES")
            webbrowser.open("https://maps.google.com")

        elif "abre Facebook" in text.lower():
            text_to_speech("Abriendo Facebook", "es-ES")
            webbrowser.open("https://www.facebook.com")

        elif "abre Twitter" in text.lower():
            text_to_speech("Abriendo Twitter", "es-ES")
            webbrowser.open("https://www.twitter.com")

        elif "abre WhatsApp" in text.lower() or "abre WhatsApp web" in text.lower():
            text_to_speech("Abriendo WhatsApp Web", "es-ES")
            webbrowser.open("https://web.whatsapp.com")

        elif "abre el bloc de notas" in text.lower():
            text_to_speech("Abriendo el Bloc de Notas", "es-ES")
            os.system("notepad.exe")

        elif "abre la calculadora" in text.lower():
            text_to_speech("Abriendo la calculadora", "es-ES")
            os.system("calc.exe")

        elif "apaga el sistema" in text.lower():
            text_to_speech("Apagando el sistema", "es-ES")
            os.system("shutdown /s /f /t 0")

        elif "reinicia el sistema" in text.lower():
            text_to_speech("Reiniciando el sistema", "es-ES")
            os.system("shutdown /r /f /t 0")

        elif "abre el correo" in text.lower() or "abre Gmail" in text.lower():
            text_to_speech("Abriendo Gmail", "es-ES")
            webbrowser.open("https://mail.google.com")

        elif "abre mi carpeta de documentos" in text.lower():
            text_to_speech("Abriendo la carpeta de documentos", "es-ES")
            os.system("explorer C:\\Users\\TuUsuario\\Documents")
        else:
            text_to_speech("Comando no reconocido", "es-ES")
            return "Comando no reconocido"
        return text
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        text_to_speech("No se consiguió reconocer", "es-ES")
    except sr.RequestError:
        print("Error en la solicitud al servicio de reconocimiento de voz")
