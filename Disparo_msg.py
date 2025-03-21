from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o WebDriver (baixe o ChromeDriver compatível com sua versão)
driver = webdriver.Chrome()

# Abrir o WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione ENTER...")  # Aguarda login manual

# Lista de contatos e mensagens
# Pode ser o nome salvo ou o número com DDD
contatos = ["6199973110", "61 9686-2374"]
mensagem = "Olá! Essa é uma mensagem automática do WhatsApp."

for contato in contatos:
    # Buscar o contato na barra de pesquisa
    search_box = driver.find_element(
        By.XPATH, "//div[@contenteditable='true']")
    search_box.click()
    search_box.send_keys(contato)
    time.sleep(2)  # Espera carregar

    # Clicar no contato
    contato_elemento = driver.find_element(
        By.XPATH, f"//span[@title='{contato}']")
    contato_elemento.click()
    time.sleep(1)

    # Enviar mensagem
    chat_box = driver.find_element(
        By.XPATH, "//div[@title='Digite uma mensagem']")
    chat_box.click()
    chat_box.send_keys(mensagem)
    chat_box.send_keys(Keys.ENTER)

    print(f"Mensagem enviada para {contato}")
    time.sleep(2)  # Pequeno delay entre mensagens

# Fechar navegador
driver.quit()
