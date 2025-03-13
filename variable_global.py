import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurações do ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Executando o chromedriver
web = Service(r'chromedriver/chromedriver.exe')

# Configurações do login
config = configparser.ConfigParser()
config.read('auth.ini')
usuario = config["INFOB2B"]["usuario"]
senha = config["INFOB2B"]["senha"]

# Inicializando o driver com as opções configuradas
driver = webdriver.Chrome(service=web, options=chrome_options)
url_portal = "https://www.portalinfob2b.com.br/Homeprincipal"