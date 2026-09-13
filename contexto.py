# Registro de log de ingestão
origem = 's3://raw-zone/crm/'
nome_arquivo = 'clientes_20240115'
extensao = '.csv'
bytes_processados = 209_715_200  # bytes
status = 'sucesso'
erro = None

# --- Seu código abaixo ---

# 1. Caminho completo
caminho_completo = f'{origem}{nome_arquivo}{extensao}'

# 2. MB processados
tamanho_mb = bytes_processados/1_048_576
print(f'Tamanho em MB: {tamanho_mb} MB' )
# 3. Verificar status
print('sucesso' in status)
# 4. Verificar campo erro
if erro is None:
    print('Tem vazio')
else: 
    print('Não tem vazio')

