from funcoes.wait_for_element import *
from variable_global import *
from time import sleep
from crack_reCaptcha.reCaptcha import *
from selenium.webdriver.common.by import By



def login_portal():
# login no portal
    login = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[2]')
    login.send_keys(usuario)

    password = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[3]')
    password.send_keys(senha)

    btn_entrar = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[4]')
    btn_entrar.click()
    sleep(15)

# clica no menu para entrar na opção "Time Parceiro"   
    menu = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/label')
    menu.click()
    sleep(5)

    pesquisar = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/ol/li/div/span[3]/i')
    pesquisar.click()
    sleep(2)

    digita_pesquisar = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/ol/div/div[1]/div/div/input')
    digita_pesquisar.send_keys("Time")
    sleep(2)

    time_parceiro = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/ol/div/div[2]/div[1]/li[4]/ol/li/a')
    time_parceiro.click()
    sleep(10)

# Verifica se tem algum captcha dentro dos iframes
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
 
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            # verifica se tem o botão de audio do captcha dentro do iframe
            driver.find_element(By.ID, "recaptcha-audio-button")  
            driver.switch_to.default_content()
            reCaptcha_solver() # se tiver, entrar na função para resolver
            break # sai do loop
        except:
            driver.switch_to.default_content()
            print("Nenhum CAPTCHA encontrado.")
            continue
    sleep(10)

# clica no botão para exportar o excel e depois clica no botão de download
    exporta_excel = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-lista-consultor/div[1]/div/div/div/div[1]/div[2]/div[3]/a')
    exporta_excel.click()
    sleep(60)
 
    btn_download = wait_for_element(driver, '/html/body/div[1]/div/div[3]/button[1]')
    btn_download.click()
    sleep(10)

  
