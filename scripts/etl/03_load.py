import os
import shutil
import json
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def run_vectorization():
    """
    Lê os dados processados e os carrega em uma nova base de dados vetorial ChromaDB.
    A base vetorial antiga é apagada para garantir que os dados estejam sempre atualizados.
    """
    print("--- Iniciando Etapa 3: Carga e Vetorização ---")
    load_dotenv()
    
    # Carrega as configurações
    with open('configs/settings.json', 'r') as f:
        settings = json.load(f)
        
    processed_file_path = os.path.join(settings['processed_data_path'], 'dados_processados.csv')
    vectorstore_path = os.path.abspath(settings['vectorstore_path'])
    
    if not os.path.exists(processed_file_path):
        raise FileNotFoundError(f"Arquivo processado não encontrado em: {processed_file_path}")

    print("🗑️ Apagando base de dados vetorial antiga (se existir)...")
    if os.path.exists(vectorstore_path):
        shutil.rmtree(vectorstore_path)
    os.makedirs(vectorstore_path, exist_ok=True)
    
    print(f"📚 Carregando documentos do arquivo: {processed_file_path}")
    loader = CSVLoader(file_path=processed_file_path, source_column="contexto", encoding='utf-8')
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_split = splitter.split_documents(documents)

    print("🧠 Criando embeddings e vetorizando os documentos...")
    embedding = OpenAIEmbeddings()
    
    db = Chroma.from_documents(
        documents=docs_split,
        embedding=embedding,
        persist_directory=vectorstore_path,
        collection_name="documents_dados_bcb"
    )
    
    print("✅ Nova base de dados vetorial criada com sucesso!")
    print("--- Etapa 3 Concluída ---")

if __name__ == "__main__":
    run_vectorization()