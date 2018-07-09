import numpy as np
#Programacion basada en la publicada en: https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
#Tambien se consulto: https://codereview.stackexchange.com/questions/80050/k-means-clustering-algorithm-in-python
#y https://flothesof.github.io/k-means-numpy.html

def cluster_points(puntos, centroide):
    clusters  = {}
    for x in puntos:
        bestmukey = min([(i[0], np.linalg.norm(x-centroide[i[0]])) for i in enumerate(centroide)], key=lambda t:t[1])[0]

        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

    def reevaluate_centers(centroide, clusters):
    centroide_nuevo = []
    keys = sorted(clusters.keys())
    for k in keys:
        centroide_nuevo.append(np.mean(clusters[k], axis = 0))
    return centroide_nuevo

    def centroide_final(centroide, centroide_viejo):
    return (set([tuple(a) for a in centroide]) == set([tuple(a) for a in centroide_viejo]))

    from numpy import random

def kmeans(puntos, k):

    centroide_viejo = np.random.randn(k, 2)
    centroide = np.random.randn(k, 2)
    while not  centroide_final(centroide, centroide_viejo):
        centroide_viejo = centroide
        clusters = cluster_points(puntos, centroide)
        centroide = reevaluate_centers(centroide_viejo, clusters)
    return centroide
