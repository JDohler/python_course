import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1
print(a)
# Another way

a2 = np.arange(10)==4
a2 = a2 * 1

# b. Create a vector with values ranging from 10 to 49

b = np.arange(10,50)

print('\n')
print(b)

# c. Reverse a vector (first element becomes last)

c = np.flip(b)

print('\n')
print(c)

# d. Create a 3x3 matrix with values ranging from 0 to 8

d = np.arange(0,9).reshape(3,3)

print('\n')
print(d)


# e. Find indices of non-zero elements from [1,2,0,0,4,0]

e = np.array([1,2,0,0,4,0])
e = np.where(e != 0)[0]

print('\n')
print(e)

# f. Create a random vector of size 30 and find the mean value
f = np.random.random(30)  
f2 = np.mean(f)

print('\n')
print(f);print('\n')
print(f2) 

# g. Create a 2d array with 1 on the border and 0 inside

g = np.ones((5,5))

g[1:-1,1:-1] = 0
print('\n')
print(g)

# h. Create a 8x8 matrix and fill it with a checkerboard pattern


print('\n')
print("Checkerboard pattern:")
h = np.zeros((8,8),dtype=int)
h[1::2,::2] = 1
h[::2,1::2] = 1

print(h)


# i. Create a checkerboard 8x8 matrix using the tile function

i= np.array([[0,1], [1,0]])

i = np.tile(i,(4,4))

print('\n')
print (i)

# j. Given a 1D array, negate all elements which are between 3 and 8, in place

j = np.arange(11)

j2 = (j > 3) & (j < 8)
j[j2] *= -1

print('\n')
print(j)



#k. Create a random vector of size 10 and sort it

k = np.random.random(10)
k = np.sort(k)

print('\n')
print(k)



#l. Consider two random array A anb B, check if they are equal

AA = np.random.randint(0,2,5)
BB = np.random.randint(0,2,5)
equal = np.allclose(AA, BB)

print('\n')
print(AA)
print(BB)
print(equal)


#m. How to convert an integer (32 bits) array into a float (32 bits) in place?

m = np.arange(10, dtype=np.int32)

print('\n')
print(m.dtype)
m = m.astype(float)

print('\n')
print(m.dtype)


#n. How to get the diagonal of a dot product?

A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)

print('\n')
print(A)
print(B)

print('\n')
print(C)

print('\n')
print(D)