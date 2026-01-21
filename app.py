import pandas as pd
import yfinance as yf

nome_acao = input("Insira o nome da ação da bolsa que deseja obter cotação: ")
data_inicio = input("Insira a data de início (formato AAAA-MM-DD): ")
data_fim = input("Insira a data de fim (formato AAAA-MM-DD): ")

# Obter os dados de cotação em bolsa

df =yf.download(nome_acao, start=data_inicio, end=data_fim)
print(df)

