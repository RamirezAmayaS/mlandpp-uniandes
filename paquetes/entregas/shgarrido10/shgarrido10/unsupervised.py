import numpy as np

def kmeans(puntos, k):
    
    """
    K-means algorithm:
    Input = A 2D matrix of coordinates we want to make a 2-means clustering.
    Output = A 2x2 matrix with the resulting means
    Process = Iteratively assign the coordinates to a certain mean. After all points are assigned, the clustering means are reestimated based on the           
    points assigned to each of these means.
    """

    eps = 0 # Tolerance for the while 

    # Initialization of variables, we initialize with data points
    centroides = puntos[np.random.choice(puntos.shape[0], size=k, replace=False), :] # Initial means
    new_centroides = np.zeros((centroides.shape)) 
    
    aux_matrix = np.zeros((puntos.shape[0], k+1)) # Auxiliary matrix for calulations
    
    dif_norm = 1
    
    while dif_norm > eps:
    
        for idx in range(puntos.shape[0]):
            aux_matrix[idx,0:k] = np.linalg.norm((puntos[idx,:]-centroides), ord=2, axis=1)

            if len(np.where(aux_matrix[idx,0:k]==np.min(aux_matrix[idx,0:k]))[0]) == 1:
                aux_matrix[idx, k] = np.where(aux_matrix[idx,0:k]==np.min(aux_matrix[idx,0:k]))[0]
            else:
                aux_matrix[idx, k] = np.where(aux_matrix[idx,0:k]==np.min(aux_matrix[idx,0:k]))[0][0]

        for clu in range(k):
            new_centroides[clu,:] = np.mean(puntos[aux_matrix[:,k]==clu], axis=0)

        dif_norm = np.linalg.norm((centroides-new_centroides), ord=1)
        centroides = new_centroides

    return centroides 
