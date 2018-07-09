def kmeans(puntos,k):
    import numpy
    #1. Generar k centroides
    mean=[0,0]
    cov=[[1,0],[0,1]]
    centroides=numpy.random.multivariate_normal(mean,cov,k)
    print(centroides)
    
    iteracion=0
    #centroides_nuevos=centroides+10
    while True:
        #2.Asignar al centroide más cercano
        kmin=[]
        for x in puntos:
            distance=[]
            for y in centroides:
                distance.append(numpy.linalg.norm(x-y))
            kmin.append(numpy.argmin(distance))
       
        #3. Calcular la distancia promedio: nuevos centroides
        kmin=numpy.asarray(kmin)
        
        list_k=list(range(k))
        centroides_nuevos=numpy.zeros((k,2))
        for n in list_k:
            centroides_nuevos[n]=(numpy.mean(puntos[kmin==n,:], axis=0))

        iteracion=iteracion+1
        print('Iteración:')
        print(iteracion)
        print('Centroides:')
        print(centroides_nuevos)
        if (numpy.linalg.norm(centroides-centroides_nuevos)>1*10**-5):
            centroides=centroides_nuevos     
        else:
            break
                 
        
    return centroides_nuevos
    #El resultado final varía dependiendo de la semilla

