import numpy as np 
    
def get_coefficient(v1, v2):
    return np.dot(v1, v2)

def get_u(q):
    return q/np.linalg.norm(q)

def proj(v1, v2):
    return np.multiply(get_coefficient(v1, v2), v2)
           
def dot_prod(matrix):
    return (np.dot(matrix.T, matrix))

def gram_smith(matrix):
    Y, vectors, S = [], [], []
    [vectors.append(i) for i in matrix.T]
    Y.append(vectors[0])
    i = [1]
    for i in range(1, len(vectors)):
        y_i = vectors[i]
        for q in Y:
            y_i = y_i - proj(vectors[i], get_u(q))
        Y.append(y_i)
    return np.array(Y).T

def Gram_Smith_PS(P, A): 
    S = np.eye(len(P[0]))
    for i in range(len(P[0])):
        for s in range(len(P[0])):
            if (s > i): 
                S[i][s] = (1/(np.linalg.norm(P.T[i])**2))*(P.T[i]@A.T[s])
    return S
    
     
    
        

# Defining matrix
matrix = np.array([[1,1], [2,4], [-1,1]])
