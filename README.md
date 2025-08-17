Este README esá em inglês e português <br>
This README is in english and portuguese

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
<br>

# 🤖 RPA Extract Site Report

This RPA project automates the extraction of reports from a website using Python and Selenium automation, as well as tools for audio handling and speech recognition (useful for breaking captchas and automating challenges).

## ✨ How it works

- The project automates website access, navigation, downloading, and report handling.
- It includes modules to deal with captchas (including audio recognition via SpeechRecognition).
- Uses Selenium for browser automation; ChromeDriver is required.
- The main flow is in `main.py`, which orchestrates the automation functions.

## 🛠️ Libraries Used

The project uses several libraries, including:

- 🕹️ **Selenium** (`selenium`): browser automation.
- 🗂️ **Pandas** (`pandas`): data and report handling.
- 🧠 **SpeechRecognition**: audio recognition to solve captchas.
- 🔊 **soundfile**, **audiofile**, **audmath**, **audeer**: audio file and signal manipulation.
- ⏳ **tqdm**: progress bar.
- 💻 **colorama**: terminal text colorization.
- 🌎 **urllib3**, **websocket-client**: webservice communication.
- 📦 And other utilities listed in `requirements.txt`.

See the full list of dependencies in the [`requirements.txt`](./requirements.txt) file.

## 📁 File Structure

- `main.py`: project entry point.
- `variable_global.py`: global variables and configurations.
- `funcoes/`: auxiliary functions for automation.
- `captcha/`, `crack_reCaptcha/`: modules for captcha handling and breaking.
- `chromedriver/`: ChromeDriver needed for Selenium and browser handling.
- `requirements.txt`: project dependency list.

## ⚠️ Notes

- File paths are set for Windows; adjust for your environment as needed.
- Make sure to install all dependencies with `pip install -r requirements.txt`.
- ChromeDriver must be compatible with your Chrome browser version.

## ▶️ Example of execution

```bash
python main.py
```
