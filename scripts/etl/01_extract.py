import pandas as pd
import requests
import os
import json
from pathlib import Path
from datetime import datetime

def run_extraction():
    """
    Busca os dados da API do Banco Central e salva em um arquivo Parquet.
    """
    print("--- Iniciando Etapa 1: Extração de Dados ---")
    
    # Carrega as configurações
    with open('configs/settings.json', 'r') as f:
        settings = json.load(f)
    
    api_url = settings['api_url']
    raw_data_path = Path(settings['raw_data_path'])
    
    # Garante que o diretório de dados brutos exista
    raw_data_path.mkdir(parents=True, exist_ok=True)

    try:
        print(f"📡 Requisitando dados da API: {api_url}")
        response = requests.get(api_url)
        response.raise_for_status()  # Lança um erro se a requisição falhar
        
        print("✅ Dados recebidos com sucesso.")
        df_raw = pd.DataFrame(response.json())
        df_raw['data'] = pd.to_datetime(df_raw['data'], dayfirst=True)
        df_raw = df_raw.sort_values('data')

        # Salva o arquivo com um timestamp para manter o histórico
        file_name = f'dados_bcb_raw_{datetime.now().strftime("%Y%m%d_%H%M%S")}.parquet'
        output_path = raw_data_path / file_name
        df_raw.to_parquet(output_path, index=False)
        
        print(f"💾 Dados brutos salvos com sucesso em: {output_path}")
        print("--- Etapa 1 Concluída ---\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        raise

if __name__ == "__main__":
    run_extraction()
