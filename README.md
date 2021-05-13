# Análise de Dados e Finanças (Wizard - Idiomas)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

**Projeto de consultoria para a empresa Wizard Idiomas, focando na análise de dados financeiros e de funcionários para otimizar operações e fornecer insights estratégicos.**

## Sumário
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Objetivos de Negócio](#objetivos-de-negócio)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Bases de Dados](#bases-de-dados)
- [Metodologia de Análise](#metodologia-de-análise)
- [Resultados Chave e Insights](#resultados-chave-e-insights)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Uso](#instalação-e-uso)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral do Projeto:

Este projeto atua como uma consultoria de dados para a empresa Wizard Idiomas, utilizando Python e Pandas para analisar dados de funcionários, clientes e serviços prestados. O objetivo principal é transformar dados brutos em informações estratégicas e financeiras, respondendo a questões cruciais para a gestão.

## Objetivos de Negócio:

O projeto foi desenvolvido para responder às seguintes questões de negócio:

1.  **Folha Salarial Total:** Qual foi o gasto total da empresa com salários de funcionários?
2.  **Faturamento da Empresa:** Qual foi o faturamento total da empresa, detalhando por tipo de serviço?
3.  **Engajamento de Funcionários:** Qual a porcentagem de funcionários que já fecharam algum contrato, indicando o engajamento da equipe de vendas?
4.  **Contratos por Área:** Quantos contratos cada área da empresa (ex: Operações, Comercial) já fechou?
5.  **Funcionários por Área:** Quantos funcionários trabalham em cada área da empresa?
6.  **Ticket Médio Mensal:** Qual é o valor do ticket médio dos contratos mensais com os clientes?

## Estrutura do Projeto:

O repositório está organizado de forma clara para facilitar a navegação e o entendimento:

-   `dados/`: Contém as bases de dados utilizadas no projeto.
    -   `CadastroClientes.csv`: Informações sobre os clientes.
    -   `CadastroFuncionarios.csv`: Informações sobre os funcionários.
    -   `BaseServiçosPrestados.xlsx`: Detalhes dos serviços prestados e contratos.
-   `notebooks/`: Contém os notebooks Jupyter com a análise detalhada.
    -   `18.13 Mini Projeto Pandas_atualizado.ipynb`: O notebook principal que executa todas as análises e cálculos.
-   `README.md`: Este arquivo, fornecendo uma visão geral e documentação do projeto.
-   `LICENSE.md`: Arquivo contendo os termos da licença do projeto (Licença MIT).
-   `requirements.txt`: Lista de todas as bibliotecas Python e suas versões necessárias para executar o projeto.

## Bases de Dados:

O projeto utiliza três arquivos principais localizados na pasta `dados/`:

* **`CadastroClientes.csv`**: Contém dados dos clientes, incluindo o 'Valor Contrato Mensal'.
* **`CadastroFuncionarios.csv`**: Contém dados dos funcionários, incluindo 'Salario' e 'Area'.
* **`BaseServiçosPrestados.xlsx`**: Contém registros dos serviços, vinculando-os a funcionários e clientes.

As bases de dados foram carregadas, inspecionadas e, quando necessário, passaram por processos de limpeza e padronização (como tratamento de valores nulos e correção de tipos de dados) para garantir a integridade e a qualidade da análise.

## Metodologia de Análise:

A análise foi conduzida através das seguintes etapas no notebook `18.13 Mini Projeto Pandas_atualizado.ipynb`:

1.  **Importação de Dados:** Carregamento das três bases de dados (`.csv` e `.xlsx`) usando Pandas.
2.  **Análise e Cálculos:**
    * **Folha Salarial:** Soma dos salários da base de funcionários.
    * **Faturamento:** Cálculo do faturamento por serviço e o total geral, utilizando as bases de serviços.
    * **Engajamento:** Cruzamento de dados entre funcionários e serviços para identificar quantos funcionários fecharam contratos e calcular a porcentagem.
    * **Contratos por Área:** Agrupamento e contagem de contratos por área de atuação dos funcionários.
    * **Funcionários por Área:** Contagem de funcionários por cada área da empresa.
    * **Ticket Médio:** Cálculo da média dos valores dos contratos mensais dos clientes.
3.  **Visualização de Dados:** Geração de gráficos para ilustrar a distribuição de funcionários por área.

## Resultados Chave e Insights:

Os principais resultados e insights obtidos incluem:

* **Total da Folha Salarial:** O gasto total com salários foi calculado para fornecer uma visão clara dos custos operacionais fixos.
* **Faturamento Detalhado:** A análise do faturamento por serviço permitiu identificar quais serviços geram mais receita e o faturamento total da empresa.
* **Taxa de Engajamento:** A porcentagem de funcionários com contratos fechados oferece um KPI (Key Performance Indicator) importante sobre a produtividade da equipe de vendas.
* **Desempenho por Área:** A distribuição de contratos e funcionários por área ajuda a identificar quais setores são mais ativos ou necessitam de mais recursos.
* **Ticket Médio:** O valor do ticket médio oferece uma métrica essencial para entender o valor médio dos contratos com os clientes, auxiliando em estratégias de precificação e vendas.

Todos os resultados numéricos detalhados e gráficos podem ser encontrados na seção de resultados do notebook.

## Tecnologias Utilizadas:

* **Python:** Linguagem de programação principal.
* **Pandas:** Essencial para manipulação, limpeza e análise de dados tabulares.
* **NumPy:** Para operações numéricas eficientes.
* **Matplotlib:** Para criação de gráficos, especialmente para visualização da distribuição de funcionários por área.

## Instalação e Uso:

Para configurar e executar este projeto em seu ambiente local, siga as instruções abaixo:

1.  **Pré-requisitos:**
    * Python 3.8+
    * `pip` (gerenciador de pacotes do Python)
    * Jupyter Lab ou Jupyter Notebook

2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/Projeto_2_Mini_Projeto_de_Analise_de_Dados_Financas.git](https://github.com/seu-usuario/Projeto_2_Mini_Projeto_de_Analise_de_Dados_Financas.git)
    cd Projeto_2_Mini_Projeto_de_Analise_de_Dados_Financas
    ```
    *(Lembre-se de substituir `seu-usuario` pelo seu nome de usuário do GitHub.)*

3.  **Crie o arquivo `requirements.txt`:**
    * Certifique-se de que está na raiz do projeto e que todas as bibliotecas usadas nos notebooks estão instaladas no seu ambiente Python.
    * **No PowerShell (Windows) no Terminal do Jupyter Lab:**
        ```powershell
        pip freeze | Out-File -FilePath requirements.txt -Encoding UTF8
        ```
    * **No Linux/macOS (ou Git Bash no Windows) no Terminal do Jupyter Lab:**
        ```bash
        pip freeze > requirements.txt
        ```

4.  **Instale as dependências:**
    * Com o `requirements.txt` criado, instale todas as bibliotecas necessárias:
        ```bash
        pip install -r requirements.txt
        ```

5.  **Acesse e Execute o Notebook:**
    * Inicie o Jupyter Lab na raiz do projeto:
        ```bash
        jupyter lab
        ```
    * Navegue até a pasta `notebooks/` e abra o notebook `18.13 Mini Projeto Pandas_atualizado.ipynb` para reproduzir a análise e os resultados.

## Licença:

Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo [LICENSE.md](LICENSE.md) na raiz do repositório.

## Contato:

Se tiver alguma dúvida, sugestão ou quiser colaborar, sinta-se à vontade para entrar em contato:
-   **Nome:** Flávio Henrique Barbosa
-   **LinkedIn:** [Flávio Henrique Barbosa | LinkedIn](https://www.linkedin.com/in/fl%C3%A1vio-henrique-barbosa-38465938)
-   **Email:** flaviohenriquehb777@outlook.com
