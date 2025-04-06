# YouTube F1 Highlights Dashboard

Este projeto tem como objetivo analisar o desempenho de vídeos de highlights da temporada 2024 de Fórmula 1 publicados no YouTube, com foco em métricas como visualizações, curtidas, comentários e taxa de engajamento.

---

# Escolhas de projeto e Desafios
Durante o desenvolvimento, optei por remover colunas como a duração dos vídeos, já que todos tinham tempos muito semelhantes (cerca de 8 minutos), o que não traria valor analítico.

O maior desafio foi entender como consumir a API do YouTube, como faz um tempo que não consumo uma API então ainda estou ganhando prática com integração de APIs em geral — o que exigiu um
tempo extra de aprendizado.

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **Google YouTube Data API v3**
- **Pandas, Seaborn, Matplotlib**
- **Power BI**
- **Jupyter Notebook**
- **.env** para a chave da API

---

## Estrutura do Repositório

```bash
.
├── f1_youtube_filtered.json       # Dados extraídos e prontos para o Power BI
├── f1_youtube.json                # json com todos os dados extraídos da API
├── main.py                        # Script de extração via API
├── API_Youtube.ipynb              # Análises e gráficos no notebook
├── Desafio_Ray.pbix               # Relatório Power BI final
├── .env                           # Chave da API (não incluso no repositório)
└── README.md                      # Este arquivo
```

---

# Como Rodar o Projeto
1. Clonar o repositório
```bash
git clone https://github.com/dan-albuquerque/Desafio_Ray.git
cd Desafio_Ray
```

2. Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instalar as dependências
```bash
pip install -r requirements.txt
```

4. Adicionar sua chave da API do YouTube
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```bash
YOUTUBE_API_KEY=sua_chave_api_aqui
```

---

# Coletar os dados
Rode o script para extrair os dados da playlist de vídeos:

```bash
python "main.py"
```
Isso irá gerar o arquivo f1_youtube_filtered.json com os campos:
- videoId
- publishedAt
- title
- viewCount
- likeCount
- commentCount

E vai gerar também o arquvio f1_youtube.json com todos os dados extraídos da API

---

# Exploração e Visualização
Baixe e abra o arquivo API_Youtube.ipynb no Google Collab.

Nesse arquivo, você encontrará:
- Conversão de tipos
- Gráficos de séries temporais
- Cálculo da taxa de engajamento ((likes + comments) / views)
- Análises complementares para orientar decisões visuais no Power BI

---

# Power BI Dashboard
Abra o arquivo F1_Highlights_Report.pbix com o Power BI Desktop.

O relatório inclui:
- Gráficos por mês (views, likes, comentários)
- Engajamento médio e total de views
- TOP 5 vídeos com mais visualizações
- Filtros por trimestre
