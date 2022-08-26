from gtts import gTTS
# from subprocess import call
from playsound import playsound


def cria_audio(audio, nomeArquivo):
    tts = gTTS(audio, lang='pt-br')
    tts.save(nomeArquivo)

    playsound(nomeArquivo)  # Windows
    # call(['afplay', 'audios/hello.mp3'])  # OSX
    # call(['aplay', 'audios/hello.mp3'])  # Linux


cria_audio('Oi, eu sou a rose', 'audios/teste_novo.mp3')
