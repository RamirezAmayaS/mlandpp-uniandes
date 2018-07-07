import numpy as np

def centroide(k,data,cent):
    n = np.array(data.shape)[0]
    dataF = np.zeros(shape=(n,k),dtype=float)
    for counter in range(0,k):
        diff = cent[counter,:] - data
        diff2 = diff**2
        diffm = diff2[:,0] + diff2[:,1]
        distance = [ x**(1/2) for x in diffm]
        dataF[:,counter] = distance
    dataC = np.zeros(shape=(k,2),dtype=float)
    indice = np.argmin(dataF,1)
    for counter in range(0,k):
        x = data[indice == counter][:,0].mean()
        y = data[indice == counter][:,1].mean()
        new_center = [x,y]
        dataC[counter,:] = new_center
    return(dataC)

def kmeans(data,k):
    center = np.random.rand(k,2)
    while True:
        new_center = centroide(k,data,center)
        comp = center - new_center
        if np.all(comp == 0):
            center = new_center
            break
        else:
            center = new_center
            new_center = centroide(k,data,center)
    return center
