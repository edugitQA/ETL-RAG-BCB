set -e

# Instala as dependências do sistema para envio de e-mail (só será executado se necessário)
echo "📦 Verificando e instalando dependências do sistema (mailutils)..."
sudo apt-get update && sudo apt-get install -y mailutils

# Navega para o diretório do script para que os caminhos funcionem
cd "$(dirname "$0")"

echo "============================================="
echo "🚀 INICIANDO PIPELINE DE ETL - $(date)"
echo "============================================="

# Ativa o ambiente virtual (Render faz isso automaticamente, mas é uma boa prática)
# source .venv/bin/activate

# Executa o pipeline. O 'set -e' fará o script parar se algum comando falhar.
python3 scripts/etl/01_extract.py
python3 scripts/etl/02_transform.py
python3 scripts/etl/03_load.py

# Se o script chegou até aqui, tudo correu bem.
echo "✅ SUCESSO: Pipeline ETL concluído com êxito."
echo "============================================="
echo "🏁 PIPELINE FINALIZADO - $(date)"
echo "============================================="
