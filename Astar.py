import pygame
from pygame.locals import *
import math
import time

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
crashed = False
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
run = False
gameDisplay.fill(white)

gameboard = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0

    def __eq__(self, other):
        return self.position == other.position
 
def astar(gameboard, start, end):
    snode = Node(None, start)  
    snode.gCost = snode.hCost = snode.fCost = 0
    enode = Node(None, end)
    enode.gCost = enode.hCost = enode.fCost = 0
    openList = []
    closedList = []
    openList.append(snode)
    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if currentNode.fCost > item.fCost:
                currentNode = item
                currentIndex = index

        openList.pop(currentIndex)
        closedList.append(currentNode)

        #if reached end
        if currentNode == enode:
            path = []
            current = currentNode
            while current is not None:
                if current.position != snode.position and current.position != enode.position:
                    gameboard[current.position[0]][current.position[1]] = 4
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
            if nodePosition[0] > (len(gameboard) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(gameboard[len(gameboard)-1]) -1) or nodePosition[1] < 0:
                continue
            if Node(currentNode, nodePosition) in closedList: 
                continue
            
            if gameboard[nodePosition[0]][nodePosition[1]] == 1:
                continue

            new_node = Node(currentNode, nodePosition)
            children.append(new_node)

        for child in children:
            for closed_child in closedList:
                if child == closed_child:
                    continue
            child.gCost = currentNode.gCost + 1
            child.hCost = ((child.position[0] - enode.position[0]) ** 2) + ((child.position[1] - enode.position[1]) ** 2)
            child.fCost = child.gCost + child.hCost

            for open_node in openList:
                if child == open_node and child.gCost > open_node.gCost:
                    continue
            
            openList.append(child)
         
        
def check_if_placed(gameboard, x):
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[j][i] == x:
                return False
    return True

def getstartandend(gameboard):
    x = []
    for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if gameboard[j][i] == 2:
                    x.append(j)
                    x.append(i)
                elif gameboard[j][i] == 3:
                    x.append(j)
                    x.append(i)
    return x 
     
        

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            gameboard[my // 25][mx // 25] = 1
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mx, my = pygame.mouse.get_pos()
            gameboard[my // 25][mx // 25] = 0
       
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            if not check_if_placed(gameboard, 2):
                pass
            else:
                mx, my = pygame.mouse.get_pos()
                gameboard[my // 25][mx // 25] = 2
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            if not check_if_placed(gameboard, 3):
                pass
            else:
                mx, my = pygame.mouse.get_pos()
                gameboard[my // 25][mx // 25] = 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            path = astar(gameboard, (getstartandend(gameboard)[0], getstartandend(gameboard)[1]), (getstartandend(gameboard)[2], getstartandend(gameboard)[3]))
            print(path)
        
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[j][i] == 0:
                pygame.draw.rect(gameDisplay, black, (i * 25, j * 25, 25, 25))
                pygame.draw.rect(gameDisplay, white, (i * 25, j * 25, 23, 23))
            elif gameboard[j][i] == 1:
                pygame.draw.rect(gameDisplay, white, (i * 25, j * 25, 25, 25))
                pygame.draw.rect(gameDisplay, black, (i * 25, j * 25, 23, 23))
            elif gameboard[j][i] == 2:
                pygame.draw.rect(gameDisplay, black, (i * 25, j * 25, 25, 25))
                pygame.draw.rect(gameDisplay, green, (i * 25, j * 25, 23, 23))
            elif gameboard[j][i] == 3:
                pygame.draw.rect(gameDisplay, black, (i * 25, j * 25, 25, 25))
                pygame.draw.rect(gameDisplay, red, (i * 25, j * 25, 23, 23))
            elif gameboard[j][i] == 4:
                pygame.draw.rect(gameDisplay, black, (i * 25, j * 25, 25, 25))
                pygame.draw.rect(gameDisplay, blue, (i * 25, j * 25, 23, 23))    
                
    pygame.display.update()
    
    clock.tick(60)
    
    

    
pygame.quit()