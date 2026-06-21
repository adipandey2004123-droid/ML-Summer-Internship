import numpy as np

# #1D Array
arr_1d = np.array([1,2,3,4,5,6])

print(arr_1d)

print("   ")

# #2D Array
arr_2d = np.array([[1,2,3],
                   [3,4,5],
                   [6,7,8]])

print(arr_2d)

# #Matrix 
Matrix = np.array([[1,2,3],
                   [3,4,5],
                   [6,7,8]])

print(Matrix)


# #Default Zero
Zero_Array = np.zeros(3)
Zero_Matrix = np.zeros((3,3))

print(Zero_Array)
print("     ")
print(Zero_Matrix)

# #Default Ones
Ones_Array = np.ones(3)
Ones_Matrix = np.ones((3,3))

print(Ones_Array)
print("    ")
print(Ones_Matrix)

# #Full function
Full_Array = np.full((3),8)
Full_Matrix = np.full((3,3),7)

print(Full_Array)
print("   ")
print(Full_Matrix)

#Creating Sequence of numbers
#arange(start,stop,step)

arr = np.arange(1,10,2)
print(arr)


#Creating an Identiy matrix
Identiy_Matrix = np.eye(3)
print(Identiy_Matrix)

print("     ")

Identiy_Matrix = np.eye(4)
print(Identiy_Matrix)
