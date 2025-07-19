import streamlit as st
import sys
from pathlib import Path

# Adiciona o diretório 'scripts' ao path para encontrar o 'qa_system'
sys.path.append(str(Path(__file__).resolve().parent / "scripts"))

try:
    # Importa as funções do nosso novo script
    from qa_system import init_qa_system, ask_question
    QA_SYSTEM_LOADED = True
except (ImportError, ValueError, FileNotFoundError) as e:
    QA_SYSTEM_LOADED = False
    ERROR_MESSAGE = e


# --- Interface do Streamlit ---

st.set_page_config(page_title="Q&A - Dados do BCB", layout="wide")

st.title("🤖 Sistema de Perguntas e Respostas com Dados do BCB")
st.markdown("Faça uma pergunta sobre dados de taxa de juros da Selic.")

# Verifica se o sistema de Q&A foi carregado corretamente
if not QA_SYSTEM_LOADED:
    st.error(f"Erro ao carregar o sistema de Q&A: {ERROR_MESSAGE}")
    st.warning("Verifique se o arquivo .env com a OPENAI_API_KEY está na raiz do projeto e se a pasta 'vectorstore' existe.")
else:
    # Carrega o sistema e mantém em cache para não recarregar a cada interação
    @st.cache_resource
    def load_system():
        return init_qa_system()

    qa_chain= load_system() # Não precisamos mais da vectorstore aqui

    # Campo para a pergunta do usuário
    user_question = st.text_input(
        "Sua pergunta:", 
        placeholder="Ex: Qual foi o valor da série em janeiro de 2023?"
    )

    if user_question:
        with st.spinner("Buscando a resposta..."):
            # AQUI ESTÁ A CORREÇÃO: removemos o argumento 'vectorstore'
            response = ask_question(user_question, qa_chain)
            
            st.success("Resposta Recebida!")
            st.write(f"**Resposta:** {response['result']}")

            # Expansor para mostrar as fontes usadas na resposta
            with st.expander("Ver fontes utilizadas na resposta"):
                for doc in response['source_documents']:
                    st.info(doc.page_content)