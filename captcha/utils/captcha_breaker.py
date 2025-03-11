import sqlite3
import json
import random
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By


def solve_text_captcha(driver, url):
    driver.maximize_window()
    driver.get(url)
    sleep(5)
    # Capturar Captcha ID
    id = driver.find_element(By.ID, "idCaptcha").get_attribute("value")
    url = f"window.open('https://autenticaint.vivo.com.br/LoginCorp/captcha?id={id}', '_blank');"
    driver.execute_script(url)
    janelas = driver.window_handles
    driver.switch_to.window(janelas[1])
    sleep(5)
    # Captura o codigo Base64 de todos os caracteres
    captchaid_list = []
    while len(captchaid_list) != 5:
        texto = driver.execute_script("return document.documentElement.innerText;")
        captchaid_list = json.loads(texto)["base64"]
    driver.close()
    driver.switch_to.window(janelas[0])
    sleep(5)
    # Resumo dos Captchas da pagina (Pode ser adicionado mais trechos para melhorar a acuracia, apenas tem de contornar o fato do python não comparar strings tão longas)
    captchaid_list_resume = []
    for _ in captchaid_list:
        captchaid_list_resume.append(
            [_][0][0:100] + [_][0][1000:1100] + [_][0][2000:2100]
        )
    # Banco de Captchas
    conn = sqlite3.connect("C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B/captcha/database2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Captcha")
    resultados = cursor.fetchall()
    conn.commit()
    conn.close()
    # Resumo dos captchas do Banco
    df_resultados = pd.DataFrame(resultados, columns=["Captcha", "Caracter"])
    lsresumo = []
    for _ in df_resultados["Captcha"]:
        lsresumo.append([_][0][0:100] + [_][0][1000:1100] + [_][0][2000:2100])
    # Adiciona a coluna 'Resumo'
    df_resultados["Resumo"] = lsresumo
    # Compara o resumo do banco com o resumo da pagina
    captcha_answer = []
    for _ in range(len(captchaid_list_resume)):
        try:
            captcha_answer.append(
                df_resultados.loc[df_resultados["Resumo"] == captchaid_list_resume[_]][
                    "Caracter"
                ].iloc[0]
            )
        except:
            if captchaid_list_resume[_][25:50] == "AAPAAAAEAAAJkAAEBAQEBAQIC":  # 6
                captcha_answer.append(
                    df_resultados.loc[df_resultados["Caracter"] == "6"][
                        "Caracter"
                    ].iloc[0]
                )

            elif captchaid_list_resume[_][25:50] == "AAPAAAACQAAFoAAHBwcHBwcHB":  # k
                captcha_answer.append(
                    df_resultados.loc[df_resultados["Caracter"] == "k"][
                        "Caracter"
                    ].iloc[0]
                )

            elif captchaid_list_resume[_][25:50] == "AAPAAAADAAAHUAAFRUVFRUVFR":  # f
                captcha_answer.append(
                    df_resultados.loc[df_resultados["Caracter"] == "f"][
                        "Caracter"
                    ].iloc[0]
                )
    # Escreve a resposta
    tempo_aleatorio = random.uniform(1, 2)
    for _ in captcha_answer:
        sleep(tempo_aleatorio)
        captcha_input = driver.find_element(
            By.XPATH, '//*[@id="form"]/fieldset/fieldset/input'
        )
        captcha_input.send_keys(_)
    sleep(5)

