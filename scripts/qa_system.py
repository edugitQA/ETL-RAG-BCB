import os
from dotenv import load_dotenv
# Imports atualizados para a nova estrutura do LangChain
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Carrega as variáveis de ambiente (como a OPENAI_API_KEY) do arquivo .env
load_dotenv()

def init_qa_system():
    """
    Inicializa e retorna a cadeia de Q&A e a vectorstore.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API da OpenAI (OPENAI_API_KEY) não foi encontrada")

    # Caminho absoluto para a base de dados vetorial
    vectorstore_path = os.path.abspath("./vectorstore")
    if not os.path.exists(vectorstore_path):
         raise FileNotFoundError(f"O diretório da base vetorial não foi encontrado em '{vectorstore_path}'. Execute o notebook de vetorização primeiro.")
    
    # Carrega a base vetorial persistida
    embedding = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = Chroma(
        persist_directory=vectorstore_path, 
        embedding_function=embedding,
        collection_name="documents_dados_bcb" # Especifique o nome da coleção
    )

    # Define o modelo de LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.0,
        openai_api_key=api_key
    )

    # Cria o template do prompt
    prompt_template = """
    Você é um assistente prestativo especialista em análise de dados.
    Sua tarefa é responder à pergunta do usuário com base no contexto fornecido.

    **Instruções de Formatação:**
    1.  Responda de forma direta e clara, em português.
    2.  Se a resposta contiver uma lista de dados (como valores em datas diferentes), organize-os em uma lista com bullet points (`*`).
    3.  Apresente os valores monetários formatados em Reais (R$) e os meses por extenso (ex: "Janeiro de 2025").
    4.  Não comece a resposta com "Com base no contexto..." ou "A resposta é...". Vá direto ao ponto.

    **Contexto:**
    {context}

    **Pergunta:** {question}

    **Resposta Formatada:**
    """
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    # Cria a cadeia de RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    
    return qa_chain, vectorstore

def ask_question(question, qa_chain):
    """
    Faz uma pergunta ao sistema e retorna a resposta.
    """
    result = qa_chain.invoke({"query": question})
    return result