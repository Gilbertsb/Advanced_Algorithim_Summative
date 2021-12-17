#!/usr/bin/env python
# coding: utf-8

# In[3]:


from heapq import heappush, heappop
import heapq
def shortestReach(n,edge, S):        #shortestreach functio declaration
    paths = [-1]*n                   #initializing path to not connected 
    visited = [False]*n               #marking the current node as visted
    visited[S] = True                 #assuming the starting node is visted 
    chld = 0                          #assigning chil var o zero
    next_vist = [(chld,S)]            #next vist 
    while next_vist:                 #while next vist
        d,c = heappop(next_vist)     #prioritize 
        for r,n in g[c]:
            node_weight = d+r      #currernt weight
            if not visited[n]:    #if node has not yet visted 
                visited[n] = True   #set vist to true
                heappush(next_vist, (node_weight,n))  #prioritize the order of nodes
                paths[n] = node_weight              #set current weight to path
            else:
                if paths[n] > node_weight:    #if current weight is less then
                    index = next_vist.index((paths[n],n)) 
                    next_vist[index] = (node_weight,n)     
                    heapq._siftdown(next_vist, 0, index)
                    paths[n] = node_weight               #let the path take the current weight
                
                
                
    paths = paths[:S] + paths[S+1:]
    return print(" ".join(map(str, paths)))

for i in range(int(input())):                 #taking test case number
    
    N,M = map(int, input().split())            #split two enterd numbr
    g = [[] for i in range(N)]                #graph for all nodes
    for j in range(M):                     
        x,y,r = map(int,input().split())       #taking values
        x,y = x-1,y-1                    
        g[x].append((r,y))                   #appednding
        g[y].append((r,x))
    S = int(input()) - 1
    shortestReach(N,M,S)                     #calling finction


# In[ ]:




