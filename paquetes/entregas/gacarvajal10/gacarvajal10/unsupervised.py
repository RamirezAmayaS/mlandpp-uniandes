def kmeans(data, k):
    
    import numpy as np
    
    if isinstance(k,int):
        if isinstance(data,np.ndarray):
            if data.shape[1]==2:
                if data.shape[0]>=k:
                    centers=np.random.rand(k,2)
                    while True:
                        distance=sq_euc(data,centers)
                        index=np.argmin(distance,1)+1
                        results=np.zeros((k,2))
                        for x in range(k):
                            if np.isnan(np.average(data[np.where(index==(x+1))][...,0])):
                                results[x]=centers[x]
                            else:
                                results[x]=([np.average(data[np.where(index==(x+1))][...,0]), np.average(data[np.where(index==(x+1))][...,1])])
                        if np.allclose(centers,results):
                            break
                        else:
                            centers=results
                    return centers
                else:
                    print('El número de clusters no debe ser mayor que la cantidad de observaciones')
            else:
                print('La matriz de datos debe ser de tamaño Nx2. El algoritmo sólo permite observaciones de 2 dimensiones.')
        else:
            print('La matriz de datos debe ser un objeto numpy.ndarray')
    else:
        print('El argumento K debe ser un número entero')

def sq_euc(data,centros):
    
    import numpy as np
    
    distancia=np.zeros((data.shape[0],centros.shape[0]))
    for j in range(centros.shape[0]):
        x0=centros[j]
        for i in range(data.shape[0]):
            x=data[i]
            distancia[i,j]=((x[0]-x0[0])**2)+((x[1]-x0[1])**2)
    return distancia
