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
contatos = ["5561982627402", "5561985977274"]
mensagem = (
    "Olá! Me chamo Fernando, sou desenvolvedor e sempre tive um fascínio por tecnologia e inovação.  "
    "Percebi que sua empresa trabalha com Desenvolvimento de Software, e queria saber se vocês estão precisando "
    "de alguém que tenha força de vontade, sede de aprendizado e esteja disposto a resolver problemas de verdade. "
    "Tenho alguns projetos que mostram minha habilidade em resolver problemas reais, e adoraria trocar uma ideia "
    "para entender como posso ajudar sua empresa."
)

for contato in contatos:
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={contato}")
        time.sleep(10)

        try:
            # Esperar a caixa de mensagem estar disponível
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

            print(f"✅ Mensagem enviada para {contato}")
        except Exception as e:
            print(
                f"⚠️ Não foi possível enviar mensagem para {contato}: {str(e)}")
            continue

        # Aguarda 5 minutos
        time.sleep(300)

    except Exception as e:
        print(f"❌ Erro inesperado com {contato}: {str(e)}")
        continue

# Fechar navegador
driver.quit()
