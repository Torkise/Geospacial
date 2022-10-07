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
    Y, vectors = [], []
    [vectors.append(i) for i in matrix.T]
    Y.append(vectors[0])
    for i in range(1, len(vectors)):
        y_i = vectors[i]
        for q in Y:
            y_i = y_i - proj(vectors[i], get_u(q))
        Y.append(y_i)
    return np.array(Y).T

# Defining matrix
matrix = np.array([
    [1, 0, 1],
    [1, 2, 0],
    [1, 2, -1],
    [1, 0, 0]
    ])

#Gram Smit metod 
g_s = gram_smith(matrix)
print("Gram smit matrix \n ", g_s)

#Dot prod
n = dot_prod(g_s)
print("n matrix \n", n)