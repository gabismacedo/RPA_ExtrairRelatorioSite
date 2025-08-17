# 🤖 RPA Extrair Relatorio Site


O projeto de RPA para extração de relatórios de um site, utiliza Python e automação com Selenium, 
além de ferramentas para manipulação de áudio e reconhecimento de fala (útil para quebra de captchas e automação de desafios).

## ✨ Como funciona

- O projeto automatiza o acesso a um site, navegação, download e manipulação de relatórios.
- Possui módulos para lidar com captchas (incluindo reconhecimento de áudio via SpeechRecognition).
- Utiliza Selenium para automação de browser, sendo necessário o ChromeDriver.
- O fluxo principal está em `main.py`, que orquestra as funções de automação.

## 🛠️ Bibliotecas Utilizadas

O projeto utiliza diversas bibliotecas, principais:

- 🕹️ **Selenium** (`selenium`): automação de navegador.
- 🗂️ **Pandas** (`pandas`): manipulação de dados e relatórios.
- 🧠 **SpeechRecognition**: reconhecimento de áudio para resolver captchas.
- 🔊 **soundfile**, **audiofile**, **audmath**, **audeer**: manipulação de arquivos e sinais de áudio.
- ⏳ **tqdm**: barra de progresso.
- 💻 **colorama**: colorização de textos no terminal.
- 🌎 **urllib3**, **websocket-client**: comunicação com webservices.
- 📦 E outras utilidades presentes em `requirements.txt`.

Veja a lista completa de dependências no arquivo [`requirements.txt`](./requirements.txt).

## 📁 Estrutura dos Arquivos

- `main.py`: ponto de entrada do projeto.
- `variable_global.py`: variáveis e configurações globais.
- `funcoes/`: funções auxiliares para automação.
- `captcha/`, `crack_reCaptcha/`: módulos para manipulação e quebra de captcha.
- `chromedriver/`: ChromeDriver necessário para Selenium e manipulação da página.
- `requirements.txt`: lista de dependências do projeto.

## ⚠️ Observações

- Os caminhos de arquivos estão configurados para ambiente Windows, altere de acordo com o seu ambiente.
- Certifique-se de instalar todas as dependências com `pip install -r requirements.txt`.
- O ChromeDriver deve ser compatível com a versão do seu navegador Chrome.

## ▶️ Exemplo de execução

```bash
python main.py
```
