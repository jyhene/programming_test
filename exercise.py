import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from math import *

# Logic


def smallest_difference(array):
    # Code a function that takes an array and returns the smallest
    # absolute difference between two elements of this array
    # Please note that the array can be large and that the more
    # computationally efficient the better
    
    nb_lignes, nb_col =np.shape(array)[0], np.shape(array)[1]  #recupération du nombre de lignes et de colonnes du tableau
    n=nb_lignes*nb_col        #nombre de valeurs totales
    M=[]                      #liste vide où seront stockées les valeurs des différences
    
    
    #i est le positionnement d'une valeur dans le tableau
    for i in range(n):
        l1 = floor(i/nb_col)   #indice ligne
        c1 = i%nb_col          #indice colonne
        
        for j in range(i+1,n):   #j est le positionnement de l'autre valeur dans le tableau, décalé d'une valeur par rapport au tableau précédent
            l2 = floor(j/nb_col)
            c2 = j%nb_col
            
            d = abs(array[l1][c1]-array[l2][c2])   #valeur absolue de la différence
            M.append(d)
            
        
    return(min(M))


# Finance and DataFrame manipulation


def macd(prices, window_short=13, window_long=26):
    # Code a function that takes a DataFrame named prices and 
    # returns it's MACD (Moving Average Convergence Difference) as
    # a DataFrame with same shape
    # Assume simple moving average rather than exponential moving average
    # The expected output is in the output.csv file
    
    alldata = prices
    prices = prices['SX5T Index']
    
    mml = prices.rolling(window_long).mean()
    mmc = prices.rolling(window_short).mean()
    M = pd.DataFrame(np.abs(mml-mmc))
    M.columns = [f'macd_{window_short}_{window_long}']
    
    return pd.concat([data, M], axis=1)
    
    pass


def sortino_ratio(prices):
    # Code a function that takes a DataFrame named prices and
    # returns the Sortino ratio for each column
    # Assume risk-free rate = 0
    # On the given test set, it should yield 0.05457
    
    alldata = prices
    prices = prices['SX5T Index']
    R = returns.mean()
    s = returns.std()
    
    return(R/s)


def expected_shortfall(prices, level=0.95):
    # Code a function that takes a DataFrame named prices and
    # returns the expected shortfall at a given level
    # On the given test set, it should yield -0.03468
    alldata = prices
    prices = prices['SX5T Index']
    
    m = prices.mean()
    s = prices.std()
    
    alpha = 1-level
    ES = (1/alpha) * scipy.stats.norm.pdf(scipy.stats.norm.ppf(alpha))*s - m
    
    return(ES)


# Plot 


def visualize(prices, path):
    # Code a function that takes a DataFrame named prices and
    # saves the plot to the given path
    # Code a function that takes a DataFrame named prices and
    # saves the plot to the given path
    alldata = prices
    prices = prices['SX5T Index']
    
    data_temp = alldata.reset_index()
    date_list = data_temp["date"]
    
    fig, ax = plt.subplots(figsize=(20,7))
    xs = date_list
    xy = prices
    ax.plot(xs, xy)
    plt.ylabel('Prices')
    plt.xlabel('date')
    plt.title("Prices Graph")
    plt.show()
    
    fig.savefig(path+'/MyGgraph.png')
    
    pass
