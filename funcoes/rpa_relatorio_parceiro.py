from captcha.utils.captcha_breaker import *
from funcoes.login_portal import *
from variable_global import *
from funcoes.descompactar_arquivo import *

def rpa_relatorio_parceiro():
    solve_text_captcha(driver, url_portal)
    login_portal()
    descompactar_arquivo()

    

