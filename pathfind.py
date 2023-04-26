import math

canPass=['a', 0, 'e', 2, 'c']

##Node Class Creation
class Node:
    def __init__(self, pos):
        self.pos = pos
        self.g = math.inf
        self.h = math.inf
        self.f = math.inf  #Sets these to infinity as when they are created you want them to be as big as possible so that any g or h cost will be lower
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f  #This is used for the min function later

def pathfind(start, goal, level):  #This is the main pathfinding function which is called from the other files
    startNode = Node(start)
    goalNode = Node(goal)  #This initialises the start and goal nodes so they can be used

    unvisitedNodes = set([startNode])
    visitedNodes = set()  #This initialises the visited and unvisited sets

    while unvisitedNodes:  #This makes it so that whilst there is something in the unvisited nodes set, it will be run
        
        currentNode = min(unvisitedNodes)  #This retrieves the smallest f cost from the nodes in the unvisitedNodes list by using the __lt__ method
        
        if currentNode == goalNode:
            path = []
            while currentNode is not None:
                path.append(currentNode.pos)
                currentNode = currentNode.parent  #This iterates through the path needed by appending the position of the node and then making the node its parent to repeat
            return list(reversed(path))  #This reverses it so that it goes from the starting node to the goal node and not the other way around

        unvisitedNodes.remove(currentNode)
        visitedNodes.add(currentNode)  #This moves the current node from the unvisited nodes set to the visited nodes set

        for neighbourPos in neighbours(currentNode.pos, level):  #This finds all the neighbours and iterates through them
            neighbour = Node(neighbourPos)

            if neighbour in visitedNodes:
                continue  #This makes it so that nodes are not checked more than once

            tempG = currentNode.g + 10  #This adds a set amount to the G cost

            if neighbour not in unvisitedNodes:
                unvisitedNodes.add(neighbour)
                
            elif tempG >= neighbour.g:
                continue  #This makes it so that if the newly found g cost is higher than a previously found one, it is not edited so that the shortest path is found

            neighbour.parent = currentNode
            neighbour.g = tempG
            neighbour.h = heuristic(neighbour, goalNode)
            neighbour.f = neighbour.g + neighbour.h  #This sets all the attributes of the node to their correct values

    return None


def heuristic(currentNode, endNode):
    return math.sqrt((endNode.pos[0]-currentNode.pos[0])**2 + (endNode.pos[1]-currentNode.pos[1])**2)  #Simple pythagoras to find the magnitude of the distance between two nodes


def neighbours(pos, level):
    x=pos[0]
    y=pos[1]
    adjacents = []

    if x > 0 and isValidPosition(level, (y, x-1)):  #This is 2 levels of validation, checking if its in the bounds of the original array and if it is passable
        adjacents.append((x-1, y))

    if y > 0 and isValidPosition(level, (y-1, x)):
        adjacents.append((x, y-1))

    if x < len(level[y])-1 and isValidPosition(level, (y, x+1)):
        adjacents.append((x+1, y))

    if y < len(level)-1 and isValidPosition(level, (y+1, x)):
        adjacents.append((x, y+1))


    return adjacents


def isValidPosition(level, pos):
    x = pos[0]
    y=pos[1]
    
    if x < 0 or x >= len(level[0]) or y < 0 or y >= len(level):
        return False
    
    if self.level[y][x] not in canPass:
        return False  #This checks if the value of the position being checked is in the passable list or not, and if it fails then False is returned
    
    return True