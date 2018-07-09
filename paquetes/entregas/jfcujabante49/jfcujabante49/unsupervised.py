#Algoritmo Kmeans


#REFERENCIAS
#El siguiente algoritmo esta basado en los siguientes url y en el apoyo de Simón Ramirez
#https://mubaris.com/2017/10/01/kmeans-clustering-in-python/
#http://jonchar.net/notebooks/k-means/
##############PASO 0 CARGAR BASE###################
####Genero datos método Simón
import numpy as np
import copy

#A continuacion una base de datos donde se crean puntos, esta esta basada
#en el ejemplo del taller 1.

#mean = [1,1]
#cov = [[0.25,0],[0,0.25]]
#size = 1000
#datos_dist1 = np.random.multivariate_normal(mean,cov,size)
#mean = [-1,-1]
#cov = [[0.25,0],[0,0.25]]
#size = 1000
#datos_dist2 = np.random.multivariate_normal(mean,cov,size)
#Covarianza debe ser semipositiva definida
#datos = np.append(datos_dist1,datos_dist2,axis=0)
#K=2
def kmeans(datos, k):

    ##############PASO 1 DEFINIR CLUSTERS#################
    #Coordinada X de los centroides
    CentroidesX = np.random.randint(np.min(datos), np.max(datos), size=k) #Defino coordenadas X de centroides
    CentroidesY = np.random.randint(np.min(datos), np.max(datos), size=k) #Defino coordenadas Y de centroides
    Centroides = np.array(list(zip(CentroidesX, CentroidesY)), dtype=np.float32)
    #print(Centroides)

    #Importo paquete para plotear
    #import matplotlib.pyplot as plt
    #from matplotlib import style

    #Plotear base de datos y centroides
    #plt.scatter(datos[:,0], datos[:,1], s=10)
    #plt.scatter(CentroidesX, CentroidesY, s=200, c='r')

    #Recipiente para centroides
    #print(Centroides.shape)
    Centroides_antiguos = np.zeros(Centroides.shape) #Llena la dimensión de la matriz de centroides (filas x columnas) con ceros, es un recipiente para que se actualice el valor de los centroides en cada iteración
    #print(Centroides_antiguos)

    #Recipiente para asignar el label de un cluster a cada punto de los datos
    #print(len(datos))
    clusters = np.zeros(len(datos)) #Genero vector vacio de 1 columna y con la cantidad de filas de la base de datos aleatoria

    #Definir fórmula de distancia
    def dist(a, b, ax=1):
        return np.linalg.norm(a - b, axis=ax)
    #Definir criterio para deterner iteración
    #El criterio es que la distancia (diferencia) entre centroides nuevos y antiguos sea cero
    diferenciascentroides = dist(Centroides, Centroides_antiguos, None)

    #############PASO 3 CLASIFICAR PUNTOS EN CENTROIDES#################
    while diferenciascentroides != 0:
        #Mientras que la diferencia entre centroides nuevos y antiguos no sea igual a cero
        #Clasifico cada punto a un cluster
        for i in range (len(datos)):
            distancias = dist(datos[i], Centroides)
            cluster = np.argmin(distancias) #toma la distancia mínima
            clusters[i] = cluster #mete cada distancia mínima en el recipiente de labels
        #import copy
        Centroides_antiguos = copy.deepcopy(Centroides) #Guardo valor de centroide antiguo

        #Encuentro nuevos centroides
        for i in range(k):
            dots = [datos[j] for j in range(len(datos)) if clusters[j] == i]
            Centroides[i] = np.mean(dots, axis=0)
        diferenciascentroides = dist(Centroides, Centroides_antiguos, None)


    return (Centroides)
