# 🎶 Spot.py - Sistema de Recomendação de Músicas

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/seu-usuario/spot.py)

Este repositório contém um sistema de recomendação de músicas baseado em conteúdo (TF-IDF), implementado em Python e exibido através de uma aplicação web com Streamlit.

## 📂 Arquivos Principais

* **`Spot_py.ipynb`**: Notebook Jupyter com todo o passo a passo da análise de dados, processamento de texto (TF-IDF) e lógica de recomendação.
* **`app_spot_py.py`**: Aplicação interativa que utiliza o Streamlit para servir o modelo de recomendação em uma interface web amigável.
* **`requirements.txt`**: Lista de todas as bibliotecas e dependências necessárias para executar o projeto.

## 🚀 Como Usar

### Opção 1: Testar Online (Sem instalação)
Você pode acessar a aplicação rodando diretamente no navegador:
🔗 **[Clique aqui para acessar o Spot.py Live Demo](https://spotpy-sistema-de-recomendacao.streamlit.app/)**


### Opção 2: Rodar Localmente
Siga o passo a passo abaixo para configurar o ambiente e executar a aplicação na sua máquina.

```bash
# 1. Clone o repositório
git clone [https://github.com/caueoliver/spot.py.git](https://github.com/caueoliver/spot.py.git)

# 2. Entre na pasta do projeto
cd spot.py

# 3. Crie um ambiente virtual (Recomendado)
python -m venv venv

# 4. Ative o ambiente virtual
# No Windows (Git Bash):
source venv/Scripts/activate
# No Mac/Linux:
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Execute a aplicação
streamlit run app_spot_py.py