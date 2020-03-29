import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    output = 0
    for i in range(3):
        output += (a[i] * b[i])
    # print(output)
    return output

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    vector_a = [polygons[i+1][0]-polygons[i][0], polygons[i+1][1]-polygons[i][1], polygons[i+1][2]-polygons[i][2]]
    vector_b = [polygons[i+2][0]-polygons[i][0], polygons[i+2][1]-polygons[i][1], polygons[i+2][2]-polygons[i][2]]
    # print([vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1], vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2], vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]])
    return [vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1], vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2], vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]]
