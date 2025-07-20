import os
import json
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.pgvector import PGVector


load_dotenv()

CONNECTION_STRING = os.getenv("DATABASE_URL")

COLLECTION_NAME = "dados_bcb_sgs_1783"
# --------------------------------------------

def run_vectorization():
    """
    Lê os dados processados e os carrega na base de dados PGVector.
    A coleção antiga é apagada para garantir que os dados estejam sempre atualizados.
    """
    print("--- Iniciando Etapa 3: Carga e Vetorização para o PGVector ---")
    
    if not CONNECTION_STRING:
        raise ValueError("A variável de ambiente DATABASE_URL não foi encontrada.")


    with open('configs/settings.json', 'r') as f:
        settings = json.load(f)
    processed_file_path = os.path.join(settings['processed_data_path'], 'dados_processados.csv')


    print(f"📚 Carregando documentos do arquivo: {processed_file_path}")
    loader = CSVLoader(file_path=processed_file_path, source_column="contexto", encoding='utf-8')
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_split = splitter.split_documents(documents)

    # 2. Cria embeddings
    print("🧠 Criando embeddings...")
    embedding = OpenAIEmbeddings()

    # 3. Conecta ao PGVector e recria a coleção com os novos documentos
    print(f"🔄 Conectando ao PGVector e recriando a coleção '{COLLECTION_NAME}'...")
    
    PGVector.from_documents(
        embedding=embedding,
        documents=docs_split,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        pre_delete_collection=True, 
    )

    print(f"✅ Nova base de dados vetorial criada com sucesso na coleção '{COLLECTION_NAME}'!")
    print("--- Etapa 3 Concluída ---")

if __name__ == "__main__":
    run_vectorization()