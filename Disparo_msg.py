from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Aguardar login manual
input("Escaneie o QR Code e pressione ENTER...")

# Lista de contatos (formato internacional, sem '+')
contatos = ["556199973110", "556196862374"]
mensagem = "Olá! Essa é uma mensagem automática do WhatsApp."

for contato in contatos:
    try:
        # Abrir conversa com o número
        link = f"https://web.whatsapp.com/send?phone={contato}&text={mensagem}"
        driver.get(link)
        time.sleep(10)  # Tempo para carregar a conversa

        # Aguardar caixa de mensagem
        chat_box = driver.find_element(
            By.XPATH, "//div[@contenteditable='true']")
        chat_box.send_keys(Keys.ENTER)  # Enviar mensagem

        print(f"✅ Mensagem enviada para {contato}")

    except Exception as e:
        print(f"❌ Erro ao enviar para {contato}: {str(e)}")

    time.sleep(5)  # Pequeno delay entre mensagens

# Fechar navegador
driver.quit()
