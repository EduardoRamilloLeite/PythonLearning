# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# https://selenium-python.readthedocs.io/locating-elements.html
# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = r"C:\Users\eduar\OneDrive\Desktop\Codigos\PythonLearning\drivers\chromedriver.exe"

# O WebDriver no Selenium é um componente que permite automatizar a interação com navegadores da web.
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return browser
if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)
    # Como antes
    browser.get('https://www.google.com')
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)