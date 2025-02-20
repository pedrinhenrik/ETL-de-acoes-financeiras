# ETL-de-acoes-financeiras
Este projeto em Python coleta dados de ações da B3 utilizando a biblioteca `yfinance`, permitindo que o usuário baixe dados históricos e gere gráficos de preço.

# Coleta de Dados de Ações da B3
Este projeto em Python coleta dados de ações da B3 (Bolsa de Valores do Brasil) utilizando a biblioteca `yfinance`. Ele permite que o usuário escolha uma pasta para salvar os dados históricos das ações e gera gráficos com o histórico de preços da última semana.

## Funcionalidades
* Coleta dados das ações (MGLU3, BBAS3, ABEV3, ITUB4, VALE3 e PETR4), podendo ser alterado na variável acoes_disponiveis
* Coleta dados diários e semanais de ações da B3.
* Permite ao usuário escolher a pasta para salvar os arquivos CSV.
* Geração de gráficos com o histórico de preços da última semana.
* Atualiza os dados automaticamente, adicionando novas informações aos arquivos CSV existentes.
* Agendamento para execução diária.

## Tecnologias Utilizadas
* Python 3.x
* yfinance - Biblioteca da Yahoo Finance
* pandas - Manipulação de dados
* matplotlib - Geração de gráficos
* tkinter (para a caixa de diálogo de seleção de pasta)

## Pré-requisitos
* Python 3.x instalado
* Bibliotecas listadas em "Requisitos" instaladas

## Requisitos
Para instalar as bibliotecas necessárias, execute o seguinte comando no seu terminal:

```bash
pip install yfinance pandas matplotlib
