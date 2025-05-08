from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Lê o versículo do arquivo
with open("versiculo.txt", "r", encoding="utf-8") as f:
    mensagem = f.read()

chrome_options = Options()
chrome_options.add_argument("user-data-dir=/caminho/para/seu/perfil")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")

input("Se for a primeira vez, escaneie o QR Code e pressione ENTER...")

# Lista de contatos
contatos = ["5561991680627"]

for contato in contatos:
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={contato}")
        time.sleep(10)

        chat_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p"))
        )
        chat_box.click()
        time.sleep(1)

        chat_box.send_keys(mensagem)
        time.sleep(1)

        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[2]/button/span"))
        )
        send_button.click()

        print(f"✅ Versículo enviado para {contato}")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Erro com {contato}: {str(e)}")

driver.quit()
