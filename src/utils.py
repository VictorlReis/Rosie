from gtts import gTTS

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save(audio + '.mp3')