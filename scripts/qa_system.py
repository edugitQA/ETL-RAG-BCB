import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.pgvector import PGVector

load_dotenv()


CONNECTION_STRING = os.getenv("DATABASE_URL")
COLLECTION_NAME = "dados_bcb_sgs_1783"
# --------------------------------------------

def init_qa_system():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not CONNECTION_STRING:
        raise ValueError("Verifique as variáveis de ambiente: OPENAI_API_KEY, DATABASE_URL")

    # 1. Inicializa o Embedding
    embedding = OpenAIEmbeddings(openai_api_key=api_key)
    
    # 2. Inicializa o VectorStore apontando para a coleção no PGVector
    vectorstore = PGVector(
        connection_string=CONNECTION_STRING,
        embedding_function=embedding,
        collection_name=COLLECTION_NAME,
    )

    llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0, openai_api_key=api_key)
    
    # O prompt continua o mesmo...
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
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    

    return qa_chain

def ask_question(question, qa_chain):
    result = qa_chain.invoke({"query": question})
    return result