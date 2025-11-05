#  Spot.py - Sistema de Recomendação de Músicas

Este repositório contém um sistema de recomendação de músicas baseado em conteúdo (TF-IDF), implementado em Python e Streamlit.

## Arquivos Principais

* **`Spot_py.ipynb`**: Notebook Jupyter com todo o passo a passo da análise, processamento e construção do sistema de recomendação.
* **`app_spot_py.py`**: Aplicação em Python que utiliza o Streamlit para criar uma interface web local e exibir o sistema.
* **`requirements.txt`**: Lista de todas as dependências Python necessárias para rodar o projeto.

##  Como Usar

Siga os passos abaixo para configurar e executar a aplicação em seu computador.

### 1. Instalação

Primeiro, clone o repositório e instale as dependências.

```bash
# 1. clonar o repositório
git clone https://github.com/caueoliver/spot.py.git

# 2. entre na pasta do projeto
cd spot.py

# 3. crie um ambiente virtual 
python -m venv venv

# 4. ativar o ambiente virtual
# no Windows (Git Bash):
source venv/Scripts/activate
# no Mac/Linux:
source venv/bin/activate

# 5. instale as dependências
pip install -r requirements.txt
```
### 2. Execução

Com os requisitos instalados é só executar o programa no terminal com o seguinte comando

```bash
streamlit run app_spot_py.py
```