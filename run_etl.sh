#!/bin/bash

# Navega para o diretório onde o script está localizado
# Isso garante que os caminhos relativos (como 'configs/settings.json') funcionem corretamente
cd "$(dirname "$0")"

echo "============================================="
echo "🚀 INICIANDO PIPELINE DE ETL - $(date)"
echo "============================================="

# Ativa o ambiente virtual do Python
# (Ajuste o caminho para .venv se o seu tiver outro nome)
source .venv/bin/activate

# Executa cada etapa do pipeline em sequência
# O '&&' garante que a próxima etapa só rode se a anterior for bem-sucedida
python3 scripts/etl/01_extract.py && \
python3 scripts/etl/02_transform.py && \
python3 scripts/etl/03_load.py

# Verifica o status de saída do último comando
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: Pipeline ETL concluído com êxito."
else
    echo "❌ FALHA: Ocorreu um erro durante a execução do pipeline."
fi

echo "============================================="
echo "🏁 PIPELINE FINALIZADO - $(date)"
echo "============================================="