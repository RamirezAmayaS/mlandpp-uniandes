def kmeans(puntose,k):
    puntos=puntose.astype(np.ndarray)
    print(type(puntos))
    num_rows = np.shape(puntos)[0]
    k_1=k-1
    kp2=p+2
    # Acá debería ir la lógica correcta de k-means
    #inicializamos los centroides aleatoriamente y realizamos una primera asignacion de todos los puntos al primer centroide
    centroides_1 = random.randn(k,2)
    mas_cercano_1 = np.ndarray(shape=(num_rows,),dtype=np.float64,buffer=np.array([ones(num_rows),zeros(num_rows)]))
    centroides = np.ndarray(zeros(numrows,kp2))
    mas_cercano = np.ndarray(shape=(num_rows,),dtype=np.float64,buffer=np.array([zeros(num_rows),zeros(num_rows)]))
    # asignacion1=[ones(1000),zeros(1000)]
    distancias = np.ndarray(zeros(numrows,k))
    #primero calculamos las distancias
    #distances=np.sqrt(puntos[1]-)
    while mas_cercano_1!=mas_cercano :
        for x in range(k_1):
            centroide_x = np.tile(centroides_1[0,:],(num_rows,1))
            #print(centroide0.shape)
            #print(puntos.shape)
            #print(centroides[1,1])
            #el programa esta fallando aca pero no nos queda claro porque, sin poder probarlo los comandos que siguen
            distancias[:,x] = np.sqrt( (puntos[:,0] - centroide0[:,0])**2+(puntos[:,1]-centroide0[:,1])**2)
            #print(distancias0.shape)
        distancia_minima = np.min(distancias, axis=1)
        mas_cercano = np.argmin(distancias, axis=1)
        centroides_1=centroides
        mas_cercano_1=mas_cercano
        for x in range(k_1):
            centroides[x,0]=np.dot(puntos[:,0],mas_cercano)/np.dot(mas_cercano)
            centroides[x,1]=np.dot(puntos[:,1],mas_cercano)/np.dot(mas_cercano)

    return centroides
