# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 11:02:22 2018

@author: Stefany-Pc
"""
### Algoritmo de K Means 

#Grupo conformado por Nicolle Castillo Código: 200915392, Stephanie Pino: 201717296 y Andrés Pérez: 201628968

#Tomando como referencia a Harrington(2012), k means es un algortmo de aprendizaje no supervisado para análisis de clúster.
#Para el clúster, llevaremos a cabo los siguientes pasos:
#1. Importar las librerías necesrias
#2. Encontrar los centroides iniciales de manera aleatoria 
#3. Definir la medida de distancia entre el centroide y los puntos, para este caso tomaremos la distancia euclidiana
#4. Asignar a cada punto de la base a un clúster
#5. Recalcular los centroides 
#6. Asignar a cada punto, el clúster con la menor distancia 
#7. Para cada clúster calcula el promedio de los puntos, asignar el centroide al promedio

#Para el desarrollo de este código, se adaptaron los trabajos de Harrington(2012), Tim van Werkhoven (2018) fuente: https://gist.github.com/tvwerkhoven/4fdc9baad760240741a09292901d3abd, Zambo004 fuente: https://stackoverflow.com/questions/43254116/labeling-k-means-cluster-data-points-with-matplotlib 
# de la página web de StreamPy Source code K.means http://streampy.readthedocs.io/en/latest/_modules/ML/KMeans/kmeans.html
# y de National Taiwan Normal University fuente: https://github.com/teinhonglo/Information-retrieval/blob/master/K-means/kmeans.py

#Pasos del código
#Importar las librerías 
import numpy as np

#Establecer una semilla con el propósito de obtener siempre los mismos resultados 
np.random.seed(0)

#Definicion de la distancia euclidiana entre un punto de la base de datos y los centroides, se toma la mínima distancia entre cada punto i y los centroides más cercanos.
#Al tomar la función np.linalg.norm,normaliza y por lo tanto, no es necesario elevar al cuadradado. 
def distanciaeu(puntos, centroides, clusters):
    for i in puntos:
        eu_index = min([(i[0], np.linalg.norm(i-centroides[i[0]])) \
                        for i in enumerate(centroides)], key=lambda t:t[1])[0]
#asignación de centroides a los clústeres
    try:
        clusters[eu_index].append(i)
    except KeyError:
        clusters[eu_index] = [i]

#Definición de la función de k means, la cual toma en consideración la base de datos, número de clúster y establecimos un máximo de 10 iteraciones. 
def kmeans(puntos, K, maxIters = 10):

#Definición de los centroides iniciales, los cuales son asignados de manera aleatoria
    centroides = puntos[np.random.choice(np.arange(len(puntos)), K), :]
#Para cada i en el rango máximo de iteraciones,se establece un índice de los centroides más cercanos para cada punto de i 
    for i in range(maxIters):
        C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in 
        centroides]) for x_i in puntos])
#Reasignación de centroides de acuerdo con el índice establecido anteriormente y cálculo del promedio
        centroides = [puntos[C == k].mean(axis = 0) for k in range(K)]
#La función me regresará el valor de los centroides
    return np.array(centroides)
#imprimir el valor de k medias
print(kmeans(puntos, k))