lote = [
    {'id': 101, 'origem': 'api_vendas',  'valor': 1500.00},
    {'id': 102, 'origem': 'erp_sap',     'valor': -50.00},
    {'id': None,'origem': 'crm',         'valor': 200.00},
    {'id': 104, 'origem': '',            'valor': 750.00},
    {'id': 105, 'origem': 'app_mobile',  'valor': 0.00},
    {'id': 106, 'origem': 'parceiro',    'valor': 3200.00},
]

validos = []
invalidos = []

# --- Seu código abaixo ---
def validar_registro(registro): 

    if registro.get('id') is None:
        invalidos.append(registro)
        registro['motivo'] = 'Id Invalido'

    elif registro.get('valor') < 0:
        invalidos.append(registro)
        registro['motivo'] = 'valor negativo'

    elif registro.get('origem') == '':
        invalidos.append(registro)
        registro['motivo'] = 'origem vazia'

    else:
        validos.append(registro)

for evento in lote:
    validar_registro(evento)

# Resumo
print(f'\nResumo:')
print(f'  Válidos:   {len(validos)}')
print(f'  Inválidos: {len(invalidos)}')
print(f'\nRegistros inválidos:')
for inv in invalidos:
    print(f"  id={inv.get('id')} → {inv.get('motivo')}")