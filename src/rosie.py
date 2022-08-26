import speech_recognition as sr

def monitora_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        print("Google Speech Recognition thinks you said: " + recognizer.recognize_google(audio, language='pt-BR'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


monitora_audio()