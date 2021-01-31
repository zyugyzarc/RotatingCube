from time import sleep, time
import numpy as np
import render
import os

class Display:

    def __init__(self, size=[155, 50]):
        self.size = size
        self.buf = np.ones((self.size[1] , self.size[0], 6)).astype(int)
        self.sprites = []

    def point(self,x, y, color):

        
        if len(color) <= 3:
            color_np = list(color)
            color_np+= (255, )
            color = np.array(color_np).astype(int)
        render.point(self.buf, x, y, color)

    def line(self, x1, y1, x2, y2, color):
        if len(color) <= 3:
            color_np = list(color)
            color_np+= (255, )
            color = np.array(color_np).astype(int)
        render.render_line(self.buf, x1, y1, x2, y2, color)

    def render_loop(self):
        tick = self._tick ; update = self._update
        while True:
            tick(update)

    def tick(self):
        
        i=time()
        self.update()
        t= time()-i
        print(t*1000, 1/t)
        sleep(max(0,1/20-t))


    def update(self):

        CLEAR()
        render.render_screen(self.buf)

    def clear(self): self.buf = np.ones((self.size[1] , self.size[0], 6)).astype(int)
