from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Aguardar login manual
input("Escaneie o QR Code e pressione ENTER...")

# Lista de contatos no formato internacional sem '+'
contatos = ["556199973110", "556196862374"]
mensagem = "Olá! Essa é uma mensagem automática do WhatsApp."

for contato in contatos:
    try:
        # Abrir conversa com o número usando link direto
        driver.get(f"https://web.whatsapp.com/send?phone={contato}")
        time.sleep(10)  # Tempo para carregar a conversa

        # Esperar a caixa de mensagem estar disponível
        chat_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p"))
        )

        # Clicar na caixa de mensagem
        chat_box.click()
        time.sleep(1)  # Pequena pausa para garantir que o campo está ativo

        # Digitar a mensagem
        chat_box.send_keys(mensagem)
        time.sleep(1)

        # Encontrar e clicar no botão de enviar
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[2]/button/span"))
        )
        send_button.click()

        print(f"✅ Mensagem enviada para {contato}")

        # Aguardar 5 minutos (300 segundos) antes de enviar para o próximo contato
        time.sleep(300)

    except Exception as e:
        print(f"❌ Erro ao enviar para {contato}: {str(e)}")

# Fechar navegador
driver.quit()
