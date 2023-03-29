import numpy as np;

# 1.a
vector = np.random.randint(1, 20, 15)
print ("1.a Vector: ", vector)

# 1.a.1
reshaped = vector.reshape(3, 5)

# 1.a.2
print ("1.a.2 Reshaped array shape: ", reshaped.shape)

# 1.a.3
for i in range(reshaped.shape[0]):
    reshaped[i, np.where(reshaped[i] == reshaped[i].max())] = 0
print ("1.a.3 Replaced max in each row by 0: \n", reshaped)

# 1.b
array = np.random.randint(1, 20, (4, 3), dtype=np.int32)
print ("1.b Array: \n", array)
print ("1.b Array shape: ", array.shape)
print ("1.b Array type: ", type(array))
print ("1.b Array data type: ", array.dtype)

# 1.b
oneB = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(oneB)
print ("1.b Eigenvalues: \n", eigenvalues)
print ("1.b Eigenvectors: \n", eigenvectors)

# 1.c
oneC = np.array([[0, 1, 2], [3, 4, 5]])
print ("1.c Array: \n", oneC)
print ("1.c Sum of diagonal elements: ", np.trace(oneC))

# 1.d
oneD = np.arange(1, 7)
print ("1.d Array: ", oneD)
# reshape to 3x2
oneD = oneD.reshape(3, 2)
print ("1.d Reshaped array 3x2: \n", oneD)
# reshape to 2x3
oneD = oneD.reshape(2, 3)
print ("1.d Reshaped array 2x3: \n", oneD)