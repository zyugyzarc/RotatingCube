cimport numpy as np
import numpy as np


cpdef render_screen(np.ndarray buf):
    
    for i in buf:
        for j in i:
            print('\033[38;2;%d;%d;%dm\033[48;2;%d;%d;%dm\u2580\033[0m'%(j[0], j[1], j[2], j[3], j[4], j[5]), end='')
        print()

cpdef point(np.ndarray screen, int x,int y, np.ndarray incolor, int mod=1):
    

    cdef int alpha = incolor[-1]
    cdef np.ndarray color = incolor[:-1]
    cdef np.ndarray point = screen[y//2, x].reshape((2,3))
    cdef np.ndarray old_color = point[(y+mod) %2]
    point[(y+mod) %2] = color*(alpha/255) + old_color*(1-alpha/255)
    #print(color, old_color,alpha, point[(y+1) %2])
    screen[y//2, x] = point.reshape((-1))


cpdef render_sprite(np.ndarray screen, np.ndarray sprite, x, y):
    
    cdef int width = sprite.shape[0]
    cdef int height = sprite.shape[1]
    cdef int i =0
    cdef int j =0
    cdef int x_ = 0
    cdef int y_ = 0
    for i in range(width):
        for j in range(height):
            x_ = x+i
            y_ = y+j

            point(screen, y_, x_, sprite[i][j])

cpdef render_line(np.ndarray screen, int x1,int  y1,int  x2,int  y2,np.ndarray color):

    cdef double m=0
    cdef double c=0 

    try:
        m = (y2-y1)/(x2-x1)
        c = y1-m * x1
        for i in range(min(x1,x2),max(x1,x2)):
            point(screen , int(i), int(m*i + c), color, 0)
    except ZeroDivisionError:
        pass
    try:
        m= (x2-x1)/(y2-y1)
        c= x1-m * y1
        for i in range(min(y1,y2),max(y1,y2)):
            point(screen ,int(m*i + c) ,int(i) , color, 0)
    except ZeroDivisionError:
        pass
