import numpy as np
#from sklearn.cluster import KMeans

def distancia(punto1, punto2):
 distanciaX = punto1[0] - punto2[0]
 distanciaY = punto1[1] - punto2[1]
 return np.sqrt(distanciaX*distanciaX + distanciaY*distanciaY)


def aleatorio(puntos,k):
  A = np.arange(len(puntos))
  np.random.shuffle(A)
  A = A[:k]
  B = [puntos[x] for x in A]
  return B

#print(np.mean(arreglo1, axis=0))

def asigCluster(puntos,arreglo1): #parametros son puntos y posiciones de clusters
 #itere para todo elemento D en el rango de puntos(0 a 64)
 k = len(arreglo1)
 #distFinales = np.zeros(shape=(k,3))
 while True:
  distFinales = np.zeros(shape=(k,3))
  for D in range(len(puntos)):
    #itere para todo elemento E en un rango de k(4)
    for E in range(k):
      if distancia(puntos[D],arreglo1[E]) < puntos[D][2]:
        puntos[D][2] = distancia(puntos[D],arreglo1[E])
        puntos[D][3] = E
    distFinales[int(puntos[D][3])][0] += puntos[D][0]
    distFinales[int(puntos[D][3])][1] += puntos[D][1]
    distFinales[int(puntos[D][3])][2] += 1
  distFinales = [[x[0]/x[2] , x[1]/x[2], x[2]] for x in distFinales]
  distFinales = [x[:-1] for x in distFinales]
  if np.array_equal(arreglo1, distFinales):
    return np.array(distFinales)
  else:
    arreglo1 = [x for x in distFinales]

def kmeans(puntos,k):
    puntos = np.c_[puntos, np.ones(len(puntos))*10000]
    puntos = np.c_[puntos, np.zeros(len(puntos))]
    posIniciales = aleatorio(puntos,k)
    posIniciales = [x[:-2] for x in posIniciales]
    centroides = asigCluster(puntos,posIniciales)
    return centroides
