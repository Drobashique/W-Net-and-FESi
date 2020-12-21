from PIL import Image
import cv2 as cv
import skimage
from skimage import data, io, filters,morphology,segmentation,feature
from scipy import ndimage
from skimage import color
import numpy as np
import math
import sys, getopt

def rgb2gs(fd):
    newobj  = np.zeros((fd.shape[0],fd.shape[1]))
    for i in range (fd.shape[0]):
        for j in range (fd.shape[1]):
            newobj[i,j] = 0.2989*fd[i,j,0] + 0.5870 * fd[i,j,1] + 0.1140 * fd[i,j,2]
    return newobj

def paint(fd,i,j):
    #a = list(i,j,fd.shape[0] - i, fd.shape[1] - j)
    #a.sort()
    fd[i][j]=127
    i1=i
    j1=j
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
            
def fon(fd):
    flag = 0
    for j in range(fd.shape[1]):
        if fd[0][j]==0:
            fd[0][j]=127
        if fd[fd.shape[0]-1][j] == 0:
            fd[fd.shape[0]-1][j] = 127
    for i in range(fd.shape[0]):
        if fd[i][0]==0:
            fd[i][0]=127
        if fd[i][fd.shape[1]-1] == 0:
            fd[i][fd.shape[1]-1] = 127

    #1       
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    #2           
    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
    #3           
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    #2           
    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
    #3           
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
    #4            
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(1,fd.shape[1]-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127

    #2           
    for i1 in range(fd.shape[0]-1,1,-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
    #3           
    for i1 in range(1,fd.shape[0]-1):
        for j1 in range(fd.shape[1]-1,1,-1):
            if fd[i1][j1]==0 and (fd[i1-1][j1]==127 or fd[i1][j1-1]==127 or fd[i1+1][j1]==127 or fd[i1][j1+1]==127):
                fd[i1][j1] = 127
    for i1 in range(fd.shape[0]):
        for j1 in range(fd.shape[1]):
            if fd[i1][j1]==0:
                fd[i1][j1]=255
                
    for i1 in range(fd.shape[0]):
        for j1 in range(fd.shape[1]):
            if fd[i1][j1]==127:
                fd[i1][j1]=0
        
    return fd
                

im = Image.open("/Users/vladimirlisovoi/desktop/out2.png")
data = np.array(im)
fd = data.astype(np.float)
#fd = rgb2gs(fd)
fd = fon(fd)
fd = fd.astype(np.uint8) 
omg = Image.fromarray(fd)
omg.show()
omg.save("/Users/vladimirlisovoi/desktop/out3.png")
