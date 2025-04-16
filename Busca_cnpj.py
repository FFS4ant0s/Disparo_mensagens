import requests

url = "https://api.casadosdados.com.br/v1/empresas?query=completo"
headers = {
    # Substitua com sua chave real
    "Authorization": "a92880586d12861f0a43a5e91ea30669504b8db8bfa40e2baa59f9c6f2ddd6237efaddb2ca3d06a89ff14414286191f549c8b9a458e406043f2bb67694a65a8d",
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
        cnpj = empresa.get('cnpj', 'Não disponível')
        nome = empresa.get('razao_social', 'Não disponível')
        telefone = empresa.get('telefone', 'Não disponível')

        if telefone != 'Não disponível':  # Exibir apenas empresas com telefone
            print(f"CNPJ: {cnpj}")
            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print("=" * 30)
else:
    print(f"Erro: {response.status_code} - {response.text}")
