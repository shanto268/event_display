"""
Created on Wed Apr 24 19:35:24 2019

@author: CM
"""

import pygame
import numpy as np
import time
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

nmax = 0

class Cube: #Creates Geometry
    #This Create a just layer without channel
    
    vertices = [[-0.3,-0.3,0.4],[0.3,-0.3,0.4],[0.3,0.25,0.4],[-0.3,0.25,0.4],[-0.3,-0.3,0.45],[0.3,-0.3,0.45],[0.3,0.25,0.45],[-0.3,0.25,0.45], # x-bottom
                [-0.3,-0.3,-0.4],[0.3,-0.3,-0.4],[0.3,0.25,-0.4],[-0.3,0.25,-0.4],[-0.3,-0.3,-0.45],[0.3,-0.3,-0.45],[0.3,0.25,-0.45],[-0.3,0.25,-0.45], # x-top
                [-0.3,-0.3,0.45],[-0.3,0.3,0.45],[0.25,0.3,0.45],[0.25,-0.3,0.45],[-0.3,-0.3,0.5],[-0.3,0.3,0.5],[0.25,0.3,0.5],[0.25,-0.3,0.5], # y-bottom
                [-0.3,-0.3,-0.35],[-0.3,0.3,-0.35],[0.25,0.3,-0.35],[0.25,-0.3,-0.35],[-0.3,-0.3,-0.4],[-0.3,0.3,-0.4],[0.25,0.3,-0.4],[0.25,-0.3,-0.4]] # y-top

    edges = [[0,1],[0,3],[0,4],[1,5],[2,1],[2,3],[2,6],[3,7],[4,5],[6,5],[6,7],[7,4]] #Creates edges/lines between verticies. edges = [[point0,point1],[point2,point3]]
    ed = edges
    for k in np.arange(1,4,1): #Creates new lines/edges between the new bars
        for i in np.arange(0,12,1):
            edges.append([k*8+ed[i][0],k*8+ed[i][1]]) #adds new edges/lines to the end of the "edges" list
            
    def __init__(self):
        self.edges = Cube.edges
        self.vertices = Cube.vertices
        #self.surfaces = Cube.surfaces
    
    def draw(self):
        #self.draw_sides()
        glLineWidth(1) #Thickness of edges/lines in pixels
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0,1,0) #Color for edges/lines
        glEnd()

    
class Ray: #Creates Rays
    vertices = [[-0.275,-0.275,0.45],[-0.225,-0.275,0.45],[-0.175,-0.275,0.45],[-0.125,-0.275,0.45],[-0.075,-0.275,0.45],[-0.025,-0.275,0.45],[0.025,-0.275,0.45],[0.075,-0.275,0.45],[0.125,-0.275,0.45],[0.175,-0.275,0.45],[0.225,-0.275,0.45]]
    verbottom = vertices
    for k in np.arange(1,11,1):
        for i in np.arange(0,11,1):
            vertices.append([verbottom[i][0],k*0.05+verbottom[i][1],verbottom[i][2]])

    vertop = [[-0.275,-0.275,-0.4],[-0.225,-0.275,-0.4],[-0.175,-0.275,-0.4],[-0.125,-0.275,-0.4],[-0.075,-0.275,-0.4],[-0.025,-0.275,-0.4],[0.025,-0.275,-0.4],[0.075,-0.275,-0.4],[0.125,-0.275,-0.4],[0.175,-0.275,-0.4],[0.225,-0.275,-0.4]]
    for k in np.arange(0,11,1):
        for i in np.arange(0,11,1):
            vertices.append([vertop[i][0],k*0.05+vertop[i][1],vertop[i][2]])
    
    vertindex = []
    for k in np.arange(0,11,1):
        for j in np.arange(0,11,1): 
            vertindex.append([2,10-j,3,10-k])        
    for k in np.arange(0,11,1):
        for j in np.arange(0,11,1):
            vertindex.append([0,10-j,1,10-k])
    muonfile = input("Data file:")
    n = input("# of Muons:")
    nmax = int(n)
    maxrays = int(input("Max number of Rays:"))
    raycount = 0
    n=0
    data = []
    edgess = []
    with open(muonfile) as f:
        for line in f:
            n=n+1
            if n>nmax:
                break
            a = line.split()
            data.append([0,float(a[9]),1,float(a[11]),2,float(a[13]),3,float(a[15]),float(a[1])])
            
    for i in np.arange(0,len(data)-1,1):
        for j in np.arange(0,242,1):
                if vertindex[j][0] == data[i][0]:
                    if vertindex[j][1] == data[i][1]:
                        if vertindex[j][2] == data[i][2]:
                            if vertindex[j][3] == data[i][3]:
                                for f in np.arange(0,242,1):
                                    if vertindex[f][0] == data[i][4]:
                                        if vertindex[f][1] == data[i][5]:
                                            if vertindex[f][2] == data[i][6]:
                                                if vertindex[f][3] == data[i][7]:
                                                    edgess.append([j,f])
    edges = []
    def edgesss(Ti):#When called uses the Ti(Time) to added a new element to the list "edges" using a the list "edgess"
        if len(Ray.edgess)-1 != Ti:
            Ray.edges.append(Ray.edgess[int(Ti-1)-1])
            shade.colors[1+Ray.edgess[int(Ti-1)-1][1]][1] = shade.colors[1+Ray.edgess[int(Ti-1)-1][1]][1] - 0.15
            shade.colors[1+Ray.edgess[int(Ti-1)-1][1]][0] = shade.colors[1+Ray.edgess[int(Ti-1)-1][1]][2] - 0.15
            shade.colors[1+Ray.edgess[int(Ti-1)-1][0]][1] = shade.colors[1+Ray.edgess[int(Ti-1)-1][0]][1] - 0.15
            shade.colors[1+Ray.edgess[int(Ti-1)-1][0]][0] = shade.colors[1+Ray.edgess[int(Ti-1)-1][0]][2] - 0.15
            Ray.raycount += 1
            if Ray.raycount > Ray.maxrays: #& nmax != Ray.maxrays:
                del Ray.edges[0]
    
    def __init__(self):
        self.edges = Ray.edges
        self.vertices = Ray.vertices
    
    def draw(self):
        glLineWidth(0.5) #Thickness of edges/lines in pixels
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(1,0,0.9) #Color for edges/lines
        glEnd()



#code for later use
"""
class orientation: #Creates Geometry
    vertices = [[-0.35,-0.35,0.4],[-0.35,-0.35,0.30],[-0.35,-0.25,0.4],[-0.25,-0.35,0.4]]

    edges = [[0,1],[0,2],[0,3]] 
       
    def __init__(self):
        self.edges = orientation.edges
        self.vertices = orientation.vertices
        
    
    def draw(self):
        glLineWidth(2) 
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(1,0,0) 
        glEnd()
"""

class shade: #Ceates Geometry
    vertices = [[0.6,0,-0.1],[0.65,0,-0.1],[0.65,0,-0.05],[0.6,0,-0.05]]#[0.6,0,-1],[0.65,0,-1],[0.65,0,-0.95],[0.6,0,-0.95]
    for k in np.arange(1,11,1):
        for i in np.arange(0,4,1):
            vertices.append([vertices[i][0],vertices[i][1],k*0.05+vertices[i][2]])
    for k in np.arange(1,11,1):
        for i in np.arange(0,44,1):
            vertices.append([k*0.05+vertices[i][0],vertices[i][1],vertices[i][2]])
    for k in np.arange(0,484,1):
        vertices.append([vertices[k][0],vertices[k][1],-0.9+vertices[k][2]])

    vert = [[0.6,0,-0.1],[0.65,0,-0.1],[0.65,0,-0.05],[0.6,0,-0.05]]#[0.6,0,-1],[0.65,0,-1],[0.65,0,-0.95],[0.6,0,-0.95]
    for k in np.arange(1,11,1):
        for i in np.arange(0,4,1):
            vert.append([vert[i][0],vert[i][1],k*0.05+vert[i][2]])
    for k in np.arange(1,11,1):
        for i in np.arange(0,44,1):
            vert.append([k*0.05+vert[i][0],vert[i][1],vert[i][2]])
    for k in np.arange(0,484,1):
        vert.append([vert[k][0],vert[k][1],-0.9+vert[k][2]])
                
    
    edges = [[0,1],[1,2],[2,3],[3,0]]
    for k in np.arange(1,242,1): 
        for i in np.arange(0,4,1):
            edges.append([k*4+edges[i][0],k*4+edges[i][1]])

    surfaces = [[0,3,2,1]]
    su = surfaces
    for k in np.arange(1,242,1):
        for i in np.arange(0,1,1):
            surfaces.append([k*4+su[i][0],k*4+su[i][1],k*4+su[i][2],k*4+su[i][3]])
    
    colors = []
    for i in np.arange(0,243,1):
        colors.append([1,1,1])
    def rot(ang):
        for k in np.arange(0,968,1):
            shade.vertices[k][0] = (math.sqrt(shade.vert[k][0]**2+shade.vert[k][1]**2))*math.cos(math.radians(ang))
            shade.vertices[k][1] = (math.sqrt(shade.vert[k][0]**2+shade.vert[k][1]**2))*math.sin(math.radians(ang))
    

    def __init__(self):
        self.edges = shade.edges
        self.vertices = shade.vertices
        self.surfaces = shade.surfaces
    
    def draw(self):
        self.draw_sides()
        glLineWidth(1) #Thickness of edges/lines in pixels
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0,0,0) #Color for edges/lines
        glEnd()

    def draw_sides(self):
        glBegin(GL_QUADS)
        x=0
        for surface in self.surfaces:
            x=x+1
            for vertex in surface:
                glColor3f(*shade.colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()

def main():
    p = 0
    mucount = 0
    #nmax = int(n)
    
    pygame.init()
    pygame.font.init()
    display = (800,600) #Display size
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50)
    glTranslatef(0,0,-4.5) #Displacement of perspective
    c = Cube()
    r = Ray()
    s = shade()
    #o = orientation()
    
    glRotatef(90,1,0,0)
    glRotatef(30,0,0,1)

    for k in np.arange(0,968,1):
        shade.vertices[k][0] = (math.sqrt(shade.vert[k][0]**2+shade.vert[k][1]**2))*math.cos(math.radians((-30)))
        shade.vertices[k][1] = (math.sqrt(shade.vert[k][0]**2+shade.vert[k][1]**2))*math.sin(math.radians((-30)))
    
    index = 0
    indexrot = - 30
    clock = pygame.time.Clock()
    while True:
        clock.tick(60) #Refresh rate (FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        Time = pygame.time.get_ticks()/1000#Creates timer
        if Time < Ray.nmax+1:
            if Time < int(Time)+0.044:#Creates a ray and a print out every second
                mucount = 1 + mucount
                Ray.edgesss(Time)#Send time to the function "edgesss" in the class "Ray"
                print('Event#=',Ray.data[int(Time-1)][8],' Muon Count=',mucount,' Time=',Time)


        keys = pygame.key.get_pressed() #Key presses that rotate the object
        if keys[pygame.K_LEFT]:
            if index > -2:
                glRotatef(15*2,0,0,-1)
                index = index-2
                indexrot = indexrot + 30
                shade.rot(indexrot)
            time.sleep(0.05)
            
        if keys[pygame.K_RIGHT]:
            if index < 4:
                glRotatef(15*2,0,0,1)
                index = index+2
                indexrot = indexrot - 30
                shade.rot(indexrot)
            time.sleep(0.05)
            
        if keys[pygame.K_UP]:
            if index < 0:
                glRotatef(15*index,0,0,-1)
                indexrot = -30
                shade.rot(indexrot)
                index = index-index
            if index > 0:
                glRotatef(15*index,0,0,-1)
                indexrot = -30
                shade.rot(indexrot)
                index = index-index
            time.sleep(0.05)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        c.draw()
        r.draw()
        s.draw()
        #o.draw()
        pygame.display.flip()
    

main()

