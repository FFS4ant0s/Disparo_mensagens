import requests

url = "https://api.casadedados.com.br/v1/empresas?query=completo"
headers = {
    "Authorization": "Bearer SEU_TOKEN_AQUI",
    "Content-Type": "application/json"
}

payload = {
    "situacao_cadastral": ["ATIVA"],
    "uf": ["df"],
    "municipio": ["brasilia"],
    "mais_filtros": {
        "com_telefone": True
    },
    "limite": 20,
    "pagina": 1
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    empresas = response.json()
    for empresa in empresas.get('empresas', []):
        print(f"CNPJ: {empresa.get('cnpj')}")
        print(f"Nome: {empresa.get('razao_social')}")
        print(f"Telefone: {empresa.get('telefone')}")
        print("="*30)
else:
    print(f"Erro: {response.status_code} - {response.text}")
