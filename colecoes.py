lote = [
    {'origem': 'crm',         'registros': 22_100, 'status': 'sucesso'},
    {'origem': 'erp',         'registros': 8_450,  'status': 'sucesso'},
    {'origem': 'api_pagto',   'registros': 0,      'status': 'falha'},
    {'origem': 'app_mobile',  'registros': 54_300, 'status': 'sucesso'},
    {'origem': 'parceiro_x',  'registros': 0,      'status': 'falha'},
    {'origem': 'iot_sensores','registros': 180_000,'status': 'sucesso'},
]

# --- Seu código abaixo ---
sucessos = []
falhas = []
total_registros = 0
lista_origem = []

# 1. Contagem de sucessos
for evento in lote:
    if evento['status'] == 'sucesso':
        sucessos.append(evento)
    else: 
        falhas.append(evento)

print(f'Qntd. sucesso: {len(sucessos)}')
# 2. Total de registros com sucesso
for reg in lote:
    total_registros = total_registros + reg['registros']

print(f'Total Registros: {total_registros}')

# 3. Origens com falha
for origem_falhas in falhas:
    lista_origem.append(origem_falhas.get('origem', ''))
    
print(lista_origem)

# 4. Taxa de sucesso (%)
taxa_sucesso = len(sucessos) / len(lote)
print(f'Taxa Sucesso: {taxa_sucesso:.2f}')