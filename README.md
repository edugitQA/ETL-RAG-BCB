# Pipe-Rag: Engenharia de Dados para Base de Conhecimento RAG

## Descrição do Projeto
Este projeto tem como objetivo realizar o tratamento de dados provenientes de diversas fontes, aplicando processos de engenharia de dados para preparar os dados e alimentar uma base de conhecimento **RAG (Retrieval-Augmented Generation)** utilizando a biblioteca **LangGraph**.

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
├── src/              # Código-fonte do projeto
│   ├── utils_config.py  # Funções utilitárias para configuração e manipulação de dados
│   └── other_scripts.py # Outros scripts auxiliares
├── tests/            # Testes unitários para validação do código
├── requirements.txt  # Dependências do projeto
├── .gitignore        # Arquivos ignorados no controle de versão
└── README.md         # Documentação do projeto
```

---

## Stacks Utilizadas
### Linguagens e Frameworks
- **Python**: Linguagem principal para manipulação de dados e desenvolvimento.
- **Pandas**: Para manipulação e transformação de dados.
- **LangGraph**: Para integração com a base de conhecimento RAG.

### Ferramentas e Bibliotecas
- **Jupyter Notebook**: Para desenvolvimento e análise exploratória.
- **Requests**: Para coleta de dados via API.
- **Pathlib**: Para manipulação de caminhos de arquivos.
- **JSON**: Para leitura e manipulação de configurações.

---

## Processos de Engenharia de Dados Aplicados
1. **Extração de Dados**:
   - Coleta de dados de APIs externas (ex.: Banco Central do Brasil).
   
2. **Transformação de Dados**:
   - Filtragem e limpeza de dados.
   - Estruturação em formatos tabulares (ex.: CSV).
   - Criação de colunas contextuais para enriquecer os dados.

3. **Carregamento de Dados**:
   - Salvamento de dados tratados em arquivos `.csv` no diretório `data/processed`.

4. **Preparação para Base de Conhecimento**:
   - Estruturação dos dados tratados para integração com **LangGraph** e alimentação da base RAG.

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

4. Integre os dados tratados com a base RAG utilizando **LangGraph**.

---

## Próximos Passos
- **Automatização do Pipeline**:
  - Criar scripts para execução automatizada do pipeline ETL.
  
- **Integração com LangGraph**:
  - Implementar a alimentação da base de conhecimento RAG com os dados tratados.

- **Validação e Testes**:
  - Adicionar testes unitários para garantir a qualidade dos dados e do código.

---

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).