import os
import time
import random
import urllib # manipular URLs
import audiofile # manipular arquivos de audio e ler https://audeering.github.io/audiofile/usage.html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import speech_recognition as sr # converte audio em texto
from variable_global import *
from funcoes.login_portal import *

def reCaptcha_solver():
    # Verificar todos os iframes disponíveis
    iframes = driver.find_elements(By.TAG_NAME, "iframe")

    # Localizar o iframe que contém o reCAPTCHA
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            # Verificar se está no iframe do reCAPTCHA
            botao_audio = driver.find_element(By.ID, "recaptcha-audio-button")
            break
        except:
            driver.switch_to.default_content()
    else:
        raise Exception("Iframe reCAPTCHA não encontrado!")

    # Clicar no botão de áudio
    botao_audio.click()
    print("Botão de áudio clicado!")
    time.sleep(10)

    # Localizar o elemento de áudio e obter o atributo src com o link do audio
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    print(f"[INFO] URL do áudio: {src}")
    time.sleep(5)
    
    # Baixar o arquivo de áudio em MP3
    audio_mp3 = os.path.join(os.getcwd(), "sample.mp3")
    urllib.request.urlretrieve(src, audio_mp3)
    print(f"[INFO] Áudio salvo em: {audio_mp3}")
    time.sleep(5)

    # Converter de MP3 para WAV
    audio_wav = os.path.join(os.getcwd(), "sample.wav") 
    audiofile.convert_to_wav(audio_mp3, audio_wav) # converte em wav porque é o melhor para ler
    print(f"[INFO] Áudio convertido para WAV: {audio_wav}")
    time.sleep(5)
    
    # Usar o SpeechRecognition para transcrever o áudio
    transcrever = sr.Recognizer()
    with sr.AudioFile(audio_wav) as sample_audio:
        audio = transcrever.record(sample_audio)
    # Reconhecer texto com o Google Speech Recognition
    key = transcrever.recognize_google(audio)
   
    element = driver.find_element(By.ID, "audio-response")
    for char in key.lower():
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Intervalo de tempo entre cada caractere
    element.send_keys(Keys.ENTER)

    # deletar arquivos
    audio_mp3 = os.remove("sample.mp3")
    print("arquivo deletado mp3")
    audio_wav = os.remove("sample.wav")
    print("arquivo deletado wav")

    # sair do iframe
    driver.switch_to.default_content()


