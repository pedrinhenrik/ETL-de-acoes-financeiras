# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:02:21 2025

@author: pedro
"""

# Bibliotecas
import yfinance as yf
import pandas as pd
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Lista de ações populares na B3
acoes_disponiveis = {
    "PETR4": "Petrobras",
    "VALE3": "Vale",
    "ITUB4": "Itaú Unibanco",
    "ABEV3": "Ambev",
    "BBAS3": "Banco do Brasil",
    "MGLU3": "Magazine Luiza"
}

# Abre o windows explorer para seleção da pasta para salvar os csv
root = tk.Tk()
root.withdraw()  # Esconde a janela principal do Tkinter
diretorio_csv = filedialog.askdirectory(title="Selecione a pasta para salvar os arquivos CSV")

# Seleciona todos os itens de acoes_disponiveis
for codigo, nome in acoes_disponiveis.items():
    print(f"Coletando dados para: {nome} ({codigo})")

    # Adiciona o ".SA"
    ticker = codigo if codigo.endswith(".SA") else codigo + ".SA"

    # Caminho completo do arquivo csv
    csv_filename = os.path.join(diretorio_csv, f"{ticker}_historico.csv")

    # Baixar dados do último dia
    dados_novos = yf.download(ticker, period="1d", threads=False)

    # Faz a coleta de dados de cada ação da acoes_disponiveis
    if dados_novos.empty:
        print(f"Erro: Dados não disponíveis para {nome} ({codigo}). Pulando para a próxima ação.")
        continue

    # Se já existir um csv, carregar e atualizar
    if os.path.exists(csv_filename):
        dados_antigos = pd.read_csv(csv_filename, index_col=0, parse_dates=True)
        df = pd.concat([dados_antigos, dados_novos]).drop_duplicates()
    else:
        df = dados_novos

    # Arredondar os valores para 2 casas decimais
    df = df.round(2)

    # Salvar o arquivo csv atualizado
    df.to_csv(csv_filename)
    print(f"Dados salvos em: {csv_filename}")

    # Buscar dados da última semana diretamente da API para plotar um gráfico
    df_ultima_semana = yf.download(ticker, period="7d", threads=False)

    if df_ultima_semana.empty:
        print(f"Erro: Não foi possível obter os dados da última semana para {nome} ({codigo}).")
    else:
        # Criar gráfico de preços de fechamento
        plt.figure(figsize=(10, 5))
        plt.plot(df_ultima_semana.index, df_ultima_semana["Close"], marker='o', linestyle='-', color="blue", label="Fechamento")
        plt.xlabel("Data")
        plt.ylabel("Preço (R$)")
        plt.title(f"Histórico de Preços - {nome} ({codigo}) (Última Semana)")
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()

print("Processo concluído.")