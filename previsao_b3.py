import yfinance as yf
import numpy as np
import pandas as pd

def baixar_dados_ibovespa(periodo="5y"):
    ibov = yf.download('^BVSP', period=periodo)
    return ibov

def definir_estado(variacao):
    if variacao < -3:
        return 'A' 
    elif -3 <= variacao < 0:
        return 'B'  
    elif 0 <= variacao < 3:
        return 'C' 
    else:
        return 'D'  

def criar_matriz_transicao(estados):
    matriz = pd.DataFrame(np.zeros((4, 4)), columns=['A', 'B', 'C', 'D'], index=['A', 'B', 'C', 'D'])
    
    for i in range(len(estados)-1):
        estado_atual = estados[i]
        proximo_estado = estados[i+1]
        matriz.loc[estado_atual, proximo_estado] += 1
    
    matriz = matriz.div(matriz.sum(axis=1), axis=0)
    return matriz

def aplicar_markov(dados):
    dados['Retorno'] = dados['Adj Close'].pct_change() * 100
    dados['Estado'] = dados['Retorno'].apply(definir_estado)
    matriz_transicao = criar_matriz_transicao(dados['Estado'].dropna().values)
    
    return matriz_transicao

def prever_proximo_estado(matriz_transicao, estado_atual):
    if estado_atual in matriz_transicao.index:
        return matriz_transicao.loc[estado_atual]
    else:
        return None

dados_ibovespa = baixar_dados_ibovespa()

matriz_transicao = aplicar_markov(dados_ibovespa)

print("Matriz de Transição de Markov:")
print(matriz_transicao)

estado_atual = input("Qual é o estado de acordo com o fechamento de ontem da B3?\nA = Variação < -3%\nB = -3% <= Variação < 0\nC = 0% <= Variação < 3%\nD = 3% <= Variação\n# ").upper()
proximo_estado = prever_proximo_estado(matriz_transicao, estado_atual)

print(f"\nProbabilidades do estado em que a bolsa irá fechar hoje a partir de {estado_atual}:")
print(proximo_estado)
