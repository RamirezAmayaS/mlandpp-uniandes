import g-caball as np

import numpy as np
mean = [1,1]
cov = [[0.25,0],[0,0.25]]
size = 1000
puntos_dist1 = np.random.multivariate_normal(mean,cov,size)
mean = [-1,-1]
cov = [[0.25,0],[0,0.25]]
size = 1000
puntos_dist2 = np.random.multivariate_normal(mean,cov,size)
puntos = numpy.append(puntos_dist1,puntos_dist2,axis=0)
