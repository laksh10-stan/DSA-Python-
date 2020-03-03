# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:28:30 2019

@author: Lakshmendra Singh
"""

def getval(A, i, j, L, H):
    if (i< 0 or i >= L or j< 0 or j >= H):
        return 0
    else:
        return A[i][j]
def findMaxBlock(A, r, c, L, H, size):
    global maxsize
    global cntarr
    if ( r >= L or c >= H):
        return
    cntarr[r][c]= 1
    size+= 1
    if (size > maxsize):
        maxsize =size
#search in eight direclions
direction=[[- 1,0],[- 1, - 1],[0,- 1],[1,- 1],[1 ,0],[1, 1] ,[0,1],[-1, 1]]
for i in range(0, 7):
    newi = r+direction[i][0]
    ncwj =c+direction [i][1]
    val=getval (A, newi, newj, L, H)
    if (val>O and (cntarr[newi][newj]== 0)):
            findMaxBlock(A, newi, newj, L, H, size)
    cntarr[r][c]=0
def getMaxOnes(A, rmax, colmax):
    global maxsize
    global size
    global cntarr
    for i in range(O,rmax):
        for j in range(0,colmax):
            if (A[i][j] == 1):
                findMaxBlock(A, i, j, rmax, colmax, 0)
    return maxsize
zarr=[[ 1, 1,0,0,0],[0, 1, 1,0, 1],[0,0,0, 1, 1],[ 1,0,0, 1, 1],[0, 1,0, 1, 1 ]]
rmax = 5
colmax = 5
maxsize=0
size=O
cntarr=rmax*[colmax*[0]]
print ("Number of maximum 1s are ")
print (getMaxOnes(zarr, rmax, colmax))