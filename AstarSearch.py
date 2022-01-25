# -*- coding: utf-8 -*-

###############################################
#     Created on Thu Sep  15 19:02:04 2020    
#       Assignment #1:    Chengpi Wu          
###############################################

#Part of the romania roadmapp

roadmap = [("arad","zerind",75), ("arad","sibiu",140),("arad","timisoara",118),("zerind","oradea",71),
       ("oradea","sibiu",151),("timisoara","lugoj",111),("lugoj","mehadia",70),("mehadia","drobeta",75),
       ("drobeta","craiova",120),("craiova","rimnicu",146),("rimnicu","sibiu",80),
       ("craiova","pitesti",138),("rimnicu","pitesti",97),("sibiu","fagaras",99),
       ("pitesti","bucharest",101), ("fagaras","bucharest",211), ("giurgiu","bucharest",90)]

location={"arad":(1.75,10.75), "zerind":(2.5,12.5), "sibiu":(6.75,9.25),
          "timisoara":(1.75,7), "oradea":(3.3,14), "lugoj":(4.8,5.8),
          "mehadia":(5,4), "drobeta":(4.8,2.5), "craiova":(8.75,1.75),
          "rimnicu":(8,7), "fagaras":(10.5, 9), "pitesti":(11.75,5.25),
          "bucharest":(15,3.5), "giurgiu":(14,1) }

# Successor fn: successor(state,action)=list of states arrived at after action in state

def successor(roadmap,city):
    """generate list of successors of startcity in roadmap"""
    # assumes format of roadmap and that city is a strong
    successorList=[]
    for mapentry in roadmap:
        if mapentry[0]==city:
            successorList.append( (mapentry[1], mapentry[2]) )
        elif mapentry[1]==city:
            successorList.append( (mapentry[0], mapentry[2]) )
    return successorList

print('\n----------------- ASTAR search -------------------\n')

import math

def sld(X,Y):  #1: Straight Line Distance  [ (x2-x1)^2 + (y2-y1)^2)^1/2
    return round(math.sqrt((location[Y][0]-location[X][0])**2 +  (location[Y][1]-location[X][1])**2) , 2)
    
def md(X,Y):   #2: Manhattan Distance (x2-x1)+(y2-y1)
    return round(abs(location[Y][0]-location[X][0]) +  abs(location[Y][1]-location[X][1]) ,2)

def sumsldmd(X,Y):#3: Sum of first two heuristics
    return sld(X,Y) + md(X,Y)

def avgsldmd(X,Y):#4: Average of first two heuristics
    return round((sld(X,Y) + md(X,Y))/2,2)
        
# define 4 ratio scales
scaleSld = 25
scaleMd = 25
scaleSumsldmd = 25
scaleAvgsldmd = 25

#          calculate scale ratio - end

disDic = {'sld':('Heuristic #1: Straight Line Distance',scaleSld),'md':('Heuristic #2: Manhattan Distance',scaleMd), \
              'sumsldmd':('Heuristic #3: Sum of first two heuristics',scaleSumsldmd),'avgsldmd':('Heuristic #4: Average of first two heuristics',scaleAvgsldmd)}

def ASTARtreesearch(start,goal,heuristic): # not finished! everytime just search the shortest branch!
    """carry out a tree search for goal from this fringe (set of unexpanded nodes to search)"""
    # assumes that the start state is in the fringe
    print("\n\n##### ",disDic.get(heuristic)[0],"#####\n")
    ratioScale = disDic.get(heuristic)[1]
    rubbish = list() # list of already seached cities
    routes = list()
    fringe = [ [start,[], 0, round(globals()[heuristic](start,goal)*ratioScale ,2)] ]
    steps = 0
    while len(fringe)>0:
        fringe = sorted(fringe,key=lambda x:(x[3]))
        rootnode = fringe.pop(0) # thisis the strategy - just pick the first one
        root = rootnode[0]
        if root == goal:
            print ('\nFound goal and the route is: \n',rootnode[1]+[goal], '\n length: ', rootnode[2] ,'\nsteps: ',steps,'\n')
            routes.append([rootnode[1]+[goal],rootnode[2]])
            return rootnode[1]+[goal]
        nextcitylist = successor(roadmap,root) # assumes global scope roadmap
        rubbish.append(root)
        #
        fringecity=list() # can't check fringe directly for duplicates so extract cities to list
        for searchnode in fringe:
            fringecity.append(searchnode[0])
        #ASTAR
        steps += 1
        # print('ASTAR search: ', root, round(rootnode[3],2))
        # print(nextcitylist)
        for mapentry in nextcitylist: 
            city = mapentry[0]
            g = rootnode[2] # cost happened
            # h = sld(city,goal)
            h = round( globals()[heuristic](city,goal) * ratioScale ,2)
            f = g + h
            length = rootnode[2] + mapentry[1]
            if not city in fringecity and not city in rubbish or city == goal: # 
                newnode=[city,rootnode[1]+[root], length, f] # expand the path by one city
                fringe.append(newnode)# put them at the end
    if routes:
        return routes
    else:
        return "No route to "+goal
      
#     define a city pairs list
pairsCity = [('drobeta', 'zerind'), ('fagaras', 'mehadia'), ('timisoara', 'bucharest'), ('bucharest', 'mehadia'), ('bucharest', 'zerind'), ('oradea', 'drobeta'), ('rimnicu', 'lugoj'), ('timisoara', 'giurgiu'), ('lugoj', 'fagaras'), ('zerind', 'craiova')]
   
print("\nCity pairs: \n",pairsCity)

print("\n\n----- Plot optimal paths -----\n")

import matplotlib.pyplot as plt 

# convert the coordinate to a list to plot
coord = location.values()
cityCoordlist = list(zip(*coord))
cityCoordinate = [list(x) for x in cityCoordlist]

cityList = list(location.keys())

#     draw original map - begin
def drawMap():
    plt.axis([0, 18, 0, 16]) 
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis')     
    for i, txt in enumerate(cityList):
        plt.annotate(txt, (cityCoordinate[0][i]+0.2, cityCoordinate[1][i]+0.2))
    for i,pair in enumerate(roadmap):
        plt.plot([location[roadmap[i][0]][0],location[roadmap[i][1]][0]], [location[roadmap[i][0]][1],location[roadmap[i][1]][1]], marker = 'o', linestyle=':')

#     draw original map - end

#     draw optimal route - begin
 
def drawArrow(cityA, cityB):
    location.get(cityA)[0]
    plt.plot([location.get(cityA)[0],location.get(cityB)[0]],[location.get(cityA)[1],location.get(cityB)[1]], marker = 'o', color='red')
    plt.arrow(location.get(cityA)[0],location.get(cityA)[1], location.get(cityB)[0] - location.get(cityA)[0], location.get(cityB)[1] - location.get(cityA)[1],
              head_width=0.6, length_includes_head=True,color='red')

def drawRoute(routeList):
    for i in range(0,len(routeList)-1):
        drawArrow(routeList[i],routeList[i+1])
        
#     draw optimal route - end
  
#     draw optimal route of 10 pairs - begin

# slect one heuristic
for  heuristicItem in disDic.keys():
    print(disDic.get(heuristicItem)[0])

numHeur = int(input('\nEnter an integer to select an heuristic:'))


for i,pair in enumerate(pairsCity):
    # for numHeur in range(1,5): # run all heuristics.
        fig = plt.figure(figsize=(10, 7))
        print("----- pair ",i+1,pair," -----")
        drawMap()
        drawRoute(ASTARtreesearch(pair[0],pair[1],list(disDic.keys())[numHeur-1]))
        # giving a title to the graph 
        plt.title(list(disDic.values())[numHeur-1][0] +'\nA* optimal path between\ncity pair' + " " + str(i+1) + ": " + pair[0] + ' - ' + pair[1]) 
        plt.show() 
        plt.close()

#     draw optimal route of 10 pairs - end

