import speech_recognition as sr
import playsound
import utils

hotword = 'rose'

def monitora_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Say something!")
            audio = recognizer.listen(source)
            try:
                trigger =  recognizer.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('Comando: ', trigger)
                    responde('Espera ai')
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
def responde(mensagem):
    utils.cria_audio(mensagem)
    playsound(mensagem + '.mp3')

monitora_audio()