import pandas as pd
import locale
import json
from pathlib import Path


def run_transformation():
    """
    Carrega os dados brutos, os transforma e salva como um arquivo CSV processado.
    """
    print("--- Iniciando Etapa 2: Transformação dos Dados ---")
    
    # Define o local para o português do Brasil para formatar os meses
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except locale.Error:
        print("⚠️ Aviso: Locale 'pt_BR.UTF-8' não encontrado. Usando o padrão do sistema.")

    # Carrega as configurações
    with open('configs/settings.json', 'r') as f:
        settings = json.load(f)
        
    raw_data_path = Path(settings['raw_data_path'])
    processed_path = Path(settings['processed_data_path'])
    
    # Garante que o diretório de dados processados exista
    processed_path.mkdir(parents=True, exist_ok=True)
    
    # Pega o arquivo de dados brutos mais recente
    latest_raw_file = max(raw_data_path.glob("*.parquet"), key=lambda p: p.stat().st_mtime)
    
    if not latest_raw_file:
        print("❌ Nenhum arquivo de dados brutos encontrado. Abortando.")
        return

    print(f"📥 Carregando arquivo de dados brutos: {latest_raw_file}")
    df = pd.read_parquet(latest_raw_file)
    df = df.dropna(subset=['data', 'valor'])
    df['valor'] = df['valor'].astype(int)

    def gerar_contexto(row):
        data_formatada = row['data'].strftime("%B de %Y")
        valor_formatado = f"R$ {row['valor'] / 100:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return f"Em {data_formatada}, o valor registrado na série foi de {valor_formatado}."

    df['contexto'] = df.apply(gerar_contexto, axis=1)
    
    output_file = processed_path / "dados_processados.csv"
    df[['contexto']].to_csv(output_file, index=False)
    
    print(f"✅ Dados transformados e salvos em: {output_file}")
    print("--- Etapa 2 Concluída ---\n")

if __name__ == "__main__":
    run_transformation()
