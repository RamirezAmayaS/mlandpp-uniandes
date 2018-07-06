import numpy as np
import math
import random

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def kmeans(x,K):
    np.random.seed(1)
    lenx = np.shape(x)[0]
    kmeans = KMeans(n_clusters = 4, init = 'random').fit(x)

    if K >= 1:
        clusters = range(0, K)
    else:
        print('K debe ser mayor a cero (0)')
  
    randomsample = np.random.choice(clusters, lenx, replace = True)
    x = np.concatenate((x, randomsample.reshape(lenx,1)), axis = 1)
    leny = np.shape(x)[1]
    poscentroid = np.zeros((K, leny - 1), dtype = float)
    iteracion = 0
    cambios = 1

    while cambios > 0:
        
        cambios = 0
        
        for i in range(0, K):
            sumtemp = 0
            cont = 0
            for j in range(0, lenx):
                if x[j, leny - 1] == i:
                    cont = cont + 1
                    temp = x[j, 0:leny - 1]
                    sumtemp = sumtemp + temp
            if cont != 0:
                poscentroid[i, ] = sumtemp/cont

        for i in range(0, lenx):
            distanciastemp = np.zeros((K, 1), dtype = int)
            coord = x[i, 0:leny - 1]
            mindist = 0
            cluster = 0
            for j in range(0, K):
                temp = poscentroid[j, ]
                eucliddist = math.sqrt(np.sum(np.power((temp - coord), 2)))
                if j == 0:
                    mindist = eucliddist
                    cluster = j
                else:
                    if mindist > eucliddist:
                        mindist = eucliddist
                        cluster = j
                distanciastemp[j] = eucliddist
            if x[i, leny - 1] != cluster:
                x[i, leny - 1] = cluster
                cambios = cambios + 1

        iteracion = iteracion + 1

##        xpos = x[:,0]
##        ypos = x[:,1]
##        color = x[:,2]
##
##        centrx = poscentroid[:,0]
##        centry = poscentroid[:,1]
##        
##        plt.scatter(xpos,ypos,c=color)
##        plt.scatter(centrx,centry,c='cyan',marker='^')
##        plt.show()

##        print(x)
##        print(iteracion)
##        print(poscentroid)

    
##    print(kmeans.cluster_centers_)
##    print(poscentroid)
    poskmx = kmeans.cluster_centers_[:,0]
    poskmy = kmeans.cluster_centers_[:,1]
    
    xpos = x[:,0]
    ypos = x[:,1]
    color = x[:,2]

    centrx = poscentroid[:,0]
    centry = poscentroid[:,1]

    plt.figure()
    plt.scatter(xpos,ypos,c=color)
    plt.scatter(centrx,centry,c='cyan',marker='^')
    plt.scatter(poskmx,poskmy,c='magenta',marker='x')
    plt.savefig("RepresentacionGrafica")
    
    return poscentroid


