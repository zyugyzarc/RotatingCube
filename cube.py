from main import Display
from math import sin, cos
import numpy as np

class Object3dPersp:
    def __init__(self,r,color=(0,255,0),shape = None):
        self.r = r
        self.color = color
        self.verts = [[[-1], [-1], [-1]],[[-1], [1], [-1]],[[-1], [-1], [1]], [[-1], [1], [1]], [[1], [-1], [-1]], [[1], [-1], [1]], [[1], [1], [-1]], [[1], [1], [1]]]
        self.edges = [[0,1],[0,2],[0,4],[1,3],[1,6],[2,3],[2,5],[3,7],[4,5],[4,6],[5,7],[6,7]]
        self.faces = [[0,1,3,2],[0,2,5,4],[0,1,6,4],[1,3,7,6],[2,3,7,5],[4,5,7,6]]
        self.pos = [75,50]
        self.scale = 120

        #pyramid
        #self.verts = [[[-1],[-1],[-0.5]],[[1],[1],[-0.5]],[[1],[-1],[-0.5]],[[-1],[1],[-0.5]],[[0],[0],[1]]]
        #self.edges = [[0,2],[1,3],[2,1],[3,0],[0,4],[1,4],[2,4],[3,4]]


    def matrix_multiplication(self,a, b):
        columns_a = len(a[0]);rows_a = len(a)
        columns_b = len(b[0]);rows_b = len(b)
        result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
        if columns_a == rows_b:
            for x in range(rows_a):
                for y in range(columns_b):
                    sum = 0
                    for k in range(columns_a):
                        sum += a[x][k] * b[k][y]
                    result_matrix[x][y] = sum
            return result_matrix

        else:
            print("columns of the first matrix must be equal to the rows of the second matrix")
            return None

    def render(self,anglex=45, angley=45,anglez=0):

        #

        points = self.verts
 
        anglex /= -100; angley /= 100; anglez = 0
        scale = 200
        matrix_multiplication = self.matrix_multiplication

        projected_points = [j for j in range(len(points))]

        rotation_x = [[1, 0, 0],
                      [0, cos(anglex), -sin(anglex)],
                      [0, sin(anglex), cos(anglex)]]

        rotation_y = [[cos(angley), 0, -sin(angley)],
                      [0, 1, 0],
                      [sin(angley), 0, cos(angley)]]

        rotation_z = [[cos(anglez), -sin(anglez), 0],
                      [sin(anglez), cos(anglez), 0],
                      [0, 0 ,1]]

        index = 0
        for point in self.verts:
            rotated_2d = self.matrix_multiplication(rotation_x, point)
            rotated_2d = self.matrix_multiplication(rotation_y, rotated_2d)
            #rotated_2d = matrix_multiplication(rotation_z, rotated_2d)
            distance = 5
            z = 1/(distance - rotated_2d[2][0])
            projection_matrix = [[z, 0, 0],
                                [0, z, 0]]
            projected_2d = matrix_multiplication(projection_matrix, rotated_2d)

            x = projected_2d[0][0]
            y = projected_2d[1][0]
            projected_points[index] = [x, y, z]
            index += 1

        projected_points = [[i[0]*self.scale+self.pos[0], i[1]*self.scale+self.pos[1],i[2]] for i in projected_points]

        #draw edges
        prevz = -10
        max_point = [-10,-10,-10]
        max2_point = [-10,-10,-10]
        for i in projected_points:
            if i[2] > max_point[2]:
                max_point = i
                max2_point = max_point

        max_point = projected_points.index(max_point)
        max2_point = projected_points.index(max2_point)
        

        if True:

            for m in self.edges:
                x1 = projected_points[m[0]][0]
                y1 = projected_points[m[0]][1]
                x2 = projected_points[m[1]][0]
                y2 = projected_points[m[1]][1]
                self.r.line(x1,y1,x2,y2,self.color)


            for m in range(len(self.verts)):
                self.r.point(projected_points[m][0], projected_points[m][1], self.color)

        else:

            for m in self.faces:
                self.r.quad(projected_points[m][0],projected_points[m][1],projected_points[m][2],projected_points[m][3],'#',colors[0])

 
d = Display()
obj = Object3dPersp(d)
x=10; s= 1.5
t = 0
while True:
	d.clear()
	obj.pos[1]= int(50 + sin(t/100)*8)
	for i in range(0,x):
		obj.color = [0,int(255*i/x),int(64*(1-i/x))]
		obj.render((t-i*s)/2, t-i*s)
	d.tick()
	t += 15
