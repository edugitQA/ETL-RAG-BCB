# Pipe-Rag: Engenharia de Dados para Base de Conhecimento RAG

## Descrição do Projeto
Este projeto realiza o tratamento de dados provenientes de APIs externas, aplicando processos de engenharia de dados para preparar os dados e alimentar uma base de conhecimento **RAG (Retrieval-Augmented Generation)** utilizando **ChromaDB** e **LangChain**.

O foco principal é garantir que os dados tratados sejam organizados e estruturados para serem utilizados em sistemas de geração de respostas baseados em IA, com suporte a consultas eficientes e contextualizadas.

---

## Estrutura do Projeto
```
Pipe-Rag/
├── configs/          # Arquivos de configuração (ex.: settings.json)
├── data/             # Dados brutos e processados
│   ├── raw/          # Dados brutos coletados
│   └── processed/    # Dados tratados e prontos para uso
├── notebooks/        # Notebooks Jupyter para desenvolvimento e análise
│   ├── 01_coleta_api.ipynb       # Coleta de dados via API
│   ├── 02_preprocessamento.ipynb # Transformação e limpeza de dados
│   ├── 03_vetorizacao.ipynb      # Vetorização de dados com ChromaDB
│   └── 04_langchain_query.ipynb  # Manipulação de dados vetorizados com LangChain
├── scripts/          # Código-fonte do projeto
│   ├── utils.py              # Funções utilitárias
│   └── utils_config.py       # Configuração e manipulação de dados
├── vectorstore/      # Base vetorial persistida pelo ChromaDB
├── app.py            # Front-end Streamlit para interação com a base de conhecimento
├── .github/workflows # Configuração de pipelines no GitHub Actions
│   └── pipeline.yml  # Pipeline automatizado para execução do projeto
├── requirements.txt  # Dependências do projeto
├── .gitignore        # Arquivos ignorados no controle de versão
└── README.md         # Documentação do projeto
```

---

## Stacks Utilizadas
### Linguagens e Frameworks
- **Python**: Linguagem principal para manipulação de dados e desenvolvimento.
- **Pandas**: Para manipulação e transformação de dados.
- **LangChain**: Para integração com a base de conhecimento RAG.
- **ChromaDB**: Para armazenamento e busca vetorial eficiente.
- **postgress**: Para armazenamento e busca vetorial eficiente em produçao
- **Streamlit**: Para desenvolvimento do front-end interativo.


### Ferramentas e Bibliotecas
- **Jupyter Notebook**: Para desenvolvimento e análise exploratória.
- **Requests**: Para coleta de dados via API.
- **Pathlib**: Para manipulação de caminhos de arquivos.
- **JSON**: Para leitura e manipulação de configurações.
- **GitHub Actions**: Para automação de pipelines de CI/CD.

---

## Processos de Engenharia de Dados Aplicados
1. **Extração de Dados**:
   - Coleta de dados de APIs externas (ex.: Banco Central do Brasil).

2. **Transformação de Dados**:
   - Filtragem e limpeza de dados.
   - Estruturação em formatos tabulares (ex.: CSV).
   - Criação de colunas contextuais para enriquecer os dados.

3. **Vetorização de Dados**:
   - Conversão de dados tratados em vetores utilizando **OpenAIEmbeddings**.
   - Persistência dos vetores no **ChromaDB**.

4. **Manipulação e Consulta**:
   - Configuração de retrievers para busca eficiente.
   - Uso de **LangChain** para responder perguntas baseadas nos dados vetorizados.

5. **Front-End Interativo**:
   - Desenvolvimento de uma interface com **Streamlit** para facilitar consultas e visualização de dados.

6. **Automação com GitHub Actions**:
   - Configuração de pipelines para execução automatizada do projeto, incluindo testes e deploy.

---

## Como Executar o Projeto
### Pré-requisitos
- Python 3.10 ou superior
- Ambiente virtual configurado
- Instalação das dependências listadas em `requirements.txt`

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/pipe-rag.git
   cd pipe-rag
   ```

2. Configure o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Execute os notebooks para tratamento de dados:
   - `notebooks/01_coleta_api.ipynb`: Coleta de dados.
   - `notebooks/02_preprocessamento.ipynb`: Transformação e salvamento de dados.
   - `notebooks/03_vetorizacao.ipynb`: Vetorização de dados com ChromaDB.
   - `notebooks/04_langchain_query.ipynb`: Manipulação e consulta com LangChain.

4. Execute o front-end Streamlit:
   ```bash
   streamlit run app.py
   ```

5. Utilize os pipelines automatizados no GitHub Actions para validação e deploy.

---

## Base de Dados Vetorial
Este projeto utiliza **ChromaDB** para armazenamento e busca vetorial. A configuração varia conforme o ambiente:

- **Ambiente de Desenvolvimento**:
  - Nos notebooks, o ChromaDB está configurado para usar **DuckDB** como backend, armazenando os dados localmente no diretório `vectorstore`.
  - Ideal para testes e desenvolvimento local.

- **Ambiente de Produção**:
  - Em produção, o ChromaDB está configurado para usar **PostgreSQL** como backend, garantindo maior escalabilidade e confiabilidade.
  - A configuração do PostgreSQL é gerenciada por variáveis de ambiente e está integrada ao pipeline automatizado.

### Configuração do PostgreSQL
Certifique-se de que o banco de dados PostgreSQL está configurado corretamente antes de executar o projeto em produção. As variáveis de ambiente necessárias incluem:

- `POSTGRES_HOST`: Endereço do servidor PostgreSQL.
- `POSTGRES_PORT`: Porta do servidor PostgreSQL.
- `POSTGRES_USER`: Usuário do banco de dados.
- `POSTGRES_PASSWORD`: Senha do banco de dados.
- `POSTGRES_DB`: Nome do banco de dados.

---

## Próximos Passos

- **Validação e Testes**:
  - Adicionar testes unitários para garantir a qualidade dos dados e do código.

- **Expansão da Base de Conhecimento**:
  - Adicionar mais fontes de dados e enriquecer os vetores com contexto adicional.

---

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).