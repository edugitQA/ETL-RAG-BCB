import json
from pathlib import Path

def load_settings(path='configs/settings.json'):
    """
    Carrega e retorna as configurações do projeto em formato dicionário.
    """
    try:
        # Calcula o caminho absoluto com base no diretório raiz do projeto
        absolute_path = Path(__file__).parent.parent / path
        with open(absolute_path, 'r') as f:
            settings = json.load(f)
        return settings
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo de configuração '{absolute_path}' não encontrado.")

def ensure_path_exists(path: str):
    """
    Garante que o diretório informado exista. Se não existir, cria.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
