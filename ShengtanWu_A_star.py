# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:32:28 2016

@author: Wushengtan
"""

import random
import math   

                
class State(object):
    def __init__(self,value,parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value

        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def h_function(self):
        pass
    def CreateChildren(self):
        pass
        
class State_String(State):
    def __init__(self,value,parent,start = 0,goal = 0):
        super(State_String, self).__init__(value, parent,start,goal)
        if not parent:
            self.g = 0
        else:
            self.g = parent.g + 1 # gvalue       
        self.f = self.h_function() + self.g
    
    # H_function using Manhattan Distance:
           
    def h_function(self):
        if self.value == self.goal:
            return 0
        else:
            h_val = 0
            l = self.value
            for i in range(9):
                letter = self.goal[i]
                j = l.index(letter)
                g_row = j/3+1
                g_col = j%3+1
                c_row = j/3+1
                c_col = j%3+1
                h_val+= abs(g_row - c_row) +abs(g_col-c_col) 
        return h_val
        
    #maybe trash code            
    def cost(self):        
        self.g += 1
        return self.g        
    # Create New Children Objects and set parents as "self"
    # Expand code
    def CreateChildren(self):
        if not self.children:
            i = self.value.index(0)
            if i in [3,4,5,6,7,8]:
                value = self.value[:]
                value[i],value[i-3] = value[i-3], value[i]
                if self.parent:                
                    if value!= self.parent.value:                    
                        child = State_String(value,self)
                        self.children.append(child)
            if i in [1, 2, 4, 5, 7, 8]:
                value = self.value[:]
                value[i], value[i - 1] = value[i - 1], value[i]
                if self.parent:                
                    if value!= self.parent.value:                    
                        child = State_String(value,self)
                        self.children.append(child)
                else:
                    child = State_String(value,self)
                    self.children.append(child)
            if i in [0, 1, 3, 4, 6, 7]:
                value = self.value[:]
                value[i], value[i + 1] = value[i + 1], value[i]
                if self.parent:                
                    if value!= self.parent.value:                    
                        child = State_String(value,self)
                        self.children.append(child)
                else:
                    child = State_String(value,self)
                    self.children.append(child)
            if i in [0, 1, 2, 3, 4, 5]:
                value = self.value[:]
                value[i], value[i + 3] = value[i + 3], value[i]
                if self.parent:
                    if value!= self.parent.value:                    
                        child = State_String(value,self)
                        self.children.append(child)
                else:
                    child = State_String(value,self)
                    self.children.append(child)
        
            

class Astar_Solver:
    def __init__(self,start,goal):
        self.path = []
        self.closelist = [] #visited queue so that we don't visit a same node twice
        self.openlist = [] #Openlist
        self.start = start
        self.goal = goal
    
    def OnList(self,child,Ob_list): 
        for i in range(len(Ob_list)):
            if(child.value == Ob_list[i].value):        
                return Ob_list[i]
            else:
                return None
    
        
        
    def Solve(self):        
        startState = State_String(self.start, # current value
                                  0,          #parent
                                  self.start, # start state
                                  self.goal)   #goal
        self.openlist.append(startState)
                
        while(not self.path):# in path is set then jump out of the loop
                        
            if not self.openlist: #if openlist is empty then raise error
                raise Exception("EmptyOpenlist!")
            self.openlist.sort(key = lambda a: a.f)
            
            Node = self.openlist.pop(0)
            BestNode = Node
            print(BestNode.g,"/n")
            self.closelist.append(BestNode)
            if(BestNode.value == self.goal):
                self.path = BestNode.path                
            BestNode.CreateChildren()
            
            
#start = [1,4,2,3,7,5,6,8,0] #4 steps.
start = [8,6,7,2,5,4,3,0,1] #it runs like forever 
# start = [6,4,7,8,5,0,3,2,1] #it runs like forever
goal = [0,1,2,3,4,5,6,7,8]
solver = Astar_Solver(start,goal)
solver.Solve()
print(solver.path)                              
