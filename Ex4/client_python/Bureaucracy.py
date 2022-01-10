from time import sleep
from types import SimpleNamespace
from client import Client
import json
from Graph import *
from GraphAlgo import *
from GUI import *
from numpy import ones,vstack
from numpy.linalg import lstsq
from pygame import gfxdraw
import pygame
from pygame import *
import random
PORT = 6666
HOST = '127.0.0.1'
def StrangeObject2Dictionaty(Strangeobject):
    temp = Strangeobject.__dict__
    PokemonsList = list(temp.get("Pokemons"))
    PokemonsList2Return = []
    SinglePokemonStatDictionary = {}
    for i in range (0,len(PokemonsList)):
        PokemonIndex = PokemonsList[i].__dict__
        SpecificPokemonDataDictionary = PokemonIndex.get("Pokemon").__dict__
        PokeValue = SpecificPokemonDataDictionary.get("value")
        PokeType = SpecificPokemonDataDictionary.get("type")
        PokePos = SpecificPokemonDataDictionary.get("pos").split(",")
        SinglePokemonStatDictionary.update({"value":PokeValue})
        SinglePokemonStatDictionary.update({"type":PokeType})
        SinglePokemonStatDictionary.update({"pos":PokePos})
        PokemonsList2Return.append(SinglePokemonStatDictionary)
        SinglePokemonStatDictionary = {}
        #print("\nPokemon "+str(i)+":")
        #print("\tValue = [" + str(PokeValue) + "]\n" + "\tType = [" + str(PokeType) + "]\n" + "\tPos = [" + str(
        #    PokePos) + "]")
    #print(PokemonsList2Return)
    return PokemonsList2Return
def DistanceBetween2Points(x1,y1,x2,y2):
    dis = float(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    return dis
def pointIsOnLine(m, c, x, y):
    # If (x, y) satisfies the
    # equation of the line
    # with round of decimal point 10 number behind the dot
    if (round(y,10) == round(((m * x) + c),10)):
        return True
    return False
def WhatIsTheClosestNodeToThisPokemon(Pokemon,Graph:DiGraph):
    #print(Graph.printEntireGraph())
    #print(Pokemon)
    PokeX = float(Pokemon.get("pos")[0])
    PokeY = float(Pokemon.get("pos")[1])
    EdgeFoundSrc = -1
    EdgeFoundDest = -1
    for i in Graph.EdgeSrcDic.keys():
        if len(Graph.EdgeSrcDic.get(i).keys())>0:
            Keys = list(Graph.EdgeSrcDic.get(i).keys())
            for j in Keys:
                Node_i_x = float(Graph.NodeDic.get(i).x)
                Node_i_y = float(Graph.NodeDic.get(i).y)
                Node_j_x = float(Graph.NodeDic.get(j).x)
                Node_j_y = float(Graph.NodeDic.get(j).y)
                points = [(Node_i_x, Node_i_y), (Node_j_x, Node_j_y)]
                #print(points)
                x_coords, y_coords = zip(*points)
                A = vstack([x_coords, ones(len(x_coords))]).T
                (m, c) = lstsq(A, y_coords, rcond=None)[0]
                Slope = float(m)
                CCC = float(c)
                #print("\n\ny = " + str(Slope) + "x + " + str(CCC) + "         Pokemon on the line? = "
                #      + str(pointIsOnLine(Slope, CCC, PokeX, PokeY)) + "")
                #print("<"+str(i)+","+str(j)+">"+"       "+str(pointIsOnLine(Slope, CCC, PokeX, PokeY)))
                if pointIsOnLine(Slope, CCC, PokeX, PokeY):
                    EdgeFoundSrc = i
                    EdgeFoundDest = j
    #print(EdgeFoundSrc)
    #print(EdgeFoundDest)
    #print(Graph.EdgeSrcDic.get(EdgeFoundSrc).get(EdgeFoundDest))
    DistanceFromSource = DistanceBetween2Points(float(Graph.NodeDic.get(EdgeFoundSrc).x),
                                                float(Graph.NodeDic.get(EdgeFoundSrc).y),PokeX,PokeY)
    DistanceFromDest = DistanceBetween2Points(float(Graph.NodeDic.get(EdgeFoundDest).x),
                                                float(Graph.NodeDic.get(EdgeFoundDest).y),PokeX,PokeY)
    #print(DistanceFromSource)
    #print(DistanceFromDest)
    if DistanceFromSource > DistanceFromDest:
        #print("Pokemon [" + str(Pokemon.get("pos")[0])
        #      + "," + str(Pokemon.get("pos")[1])+"], Value "+str(Pokemon.get("value"))+", Closest to node ["+str(EdgeFoundDest)+"]")
        return EdgeFoundDest
    else:
        #print("Pokemon [" + str(Pokemon.get("pos")[0])
        #      + "," + str(Pokemon.get("pos")[1])+"], Value "+str(Pokemon.get("value"))+", Closest to node ["+str(EdgeFoundSrc)+"]")
        return EdgeFoundSrc
def isTherePokeOnMyWay2MostValuable(ShortestPath2MostValuable ,PokemonsList,Graph:DiGraph):
    #print("\n\n\n")
    #print(ShortestPath2MostValuable)
    PokemonsOnTheWay = []
    for i in range(1,len(ShortestPath2MostValuable)-1):
        for j in range(0,len(PokemonsList)):
            #print("<"+str(ShortestPath2MostValuable[i])+","+str(WhatIsTheClosestNodeToThisPokemon(PokemonsList[j],Graph))+">")
            if WhatIsTheClosestNodeToThisPokemon(PokemonsList[j],Graph)==ShortestPath2MostValuable[i]:
                #print("Im at node "+str(ShortestPath2MostValuable[i])+" and I can catch another pokemon at node [" + str(WhatIsTheClosestNodeToThisPokemon(PokemonsList[j],Graph)) + "]")
                PokemonsOnTheWay.append(WhatIsTheClosestNodeToThisPokemon(PokemonsList[j],Graph))
    return PokemonsOnTheWay
########################## initialization #########################
client = Client()
client.start_connection(HOST, PORT)
pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
#~~~ Get Pokemons List ~~~#
PokemonsList = StrangeObject2Dictionaty(pokemons_obj)
## %%%%%%%%%%%%%%%%%%%% Images Initialization %%%%%%%%%%%%%%%%%%%%%%% ##
bg = pygame.image.load("images/bg.jpg")
hero = pygame.image.load(r'images/hero.png')
water1 = pygame.image.load(r'images/water1.png')
water2 = pygame.image.load(r'images/water2.png')
water3 = pygame.image.load(r'images/water3.png')
ground1 = pygame.image.load(r'images/ground1.png')
ground2 = pygame.image.load(r'images/ground2.png')
ground3 = pygame.image.load(r'images/ground3.png')
Rock = pygame.image.load(r'images/Rockk.png')
PokemonsTypes = [water1, water2, water3, ground1, ground2, ground3]
## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ##
GroundPokemonRandom = random.randint(3,5)
WaterPokemonRandom = random.randint(0,2)
#~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~ Get Graph ~~~~~~~#m
graph_json = client.get_graph()
GraphData = json.loads(graph_json)
nGraph = DiGraph()
GGraphAlgo = GraphAlgo()
GGraphAlgo.nGraph = nGraph
Load2GraphExplicit(GraphData,nGraph)
#nGraph.printEntireGraph()
#~~~~~~~~~~~~~~~~~~~~~~~~~#
client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
print("\n~~~~~ Agents ~~~~~\n\t")
print(client.get_agents())
client.start()
agents = json.loads(client.get_agents(),object_hook=lambda d: SimpleNamespace(**d)).Agents
agents = [agent.Agent for agent in agents]
####################################################################
####################### Stats from received example ##########################
WIDTH, HEIGHT = 1080, 720
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
radius = 15
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
# get data proportions
#min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_x = 35.187594216303474
#print(min(list(graph.Nodes), key=lambda n: n.pos.x).pos)
#min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
min_y = 32.10107446554622
#print(min(list(graph.Nodes), key=lambda n: n.pos.y).pos)
#max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_x = 35.21310882485876
#print(max(list(graph.Nodes), key=lambda n: n.pos.x).pos)
#max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_y = 32.10788938151261
#print(max(list(graph.Nodes), key=lambda n: n.pos.y).pos)
############################################################################
def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen
# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)
def WalkSpecificPath(i,ValueOf_i,Path,AgentID,Pokemons:pokemons):
    #print("~~~~~~~~~~~~~~~~~ Start ~~~~~~~~~~~~~~~~~~~~~")
    #print("Going to Node ["+str(ValueOf_i)+"]")
    #print(agents[AgentID].__dict__)
    if agents[AgentID].__dict__.get("dest") == -1:
        next_node = ValueOf_i
        client.move()

        client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
        ttl = client.time_to_end()
        print(next_node, ttl, client.get_info())
        return i+1
    else:
        #print("Moving 1 Node")
        client.move()
        return i
def CalculatePath1(FinalFinalFinalPath):
    # ***************************** Algo For Path ****************************************#
    RoadNotTaken = []
    # print(FinalFinalFinalPath)
    for i in range(0, len(FinalFinalFinalPath) - 2):
        if FinalFinalFinalPath[i + 1] > FinalFinalFinalPath[i]:
            for inrement in range(FinalFinalFinalPath[i], FinalFinalFinalPath[i + 1]):
                RoadNotTaken.append(inrement)
            RoadNotTaken.append(FinalFinalFinalPath[i + 1])
        elif FinalFinalFinalPath[i + 1] < FinalFinalFinalPath[i]:
            for deinrement in range(FinalFinalFinalPath[i], FinalFinalFinalPath[i + 1]):
                RoadNotTaken.append(deinrement)
            RoadNotTaken.append(FinalFinalFinalPath[i + 1])
        i = FinalFinalFinalPath[1]
    if FinalFinalFinalPath[len(FinalFinalFinalPath) - 1] > FinalFinalFinalPath[len(FinalFinalFinalPath) - 2]:
        for inrement in range(FinalFinalFinalPath[len(FinalFinalFinalPath) - 1],
                              FinalFinalFinalPath[len(FinalFinalFinalPath) - 2]):
            RoadNotTaken.append(inrement)
        RoadNotTaken.append(FinalFinalFinalPath[len(FinalFinalFinalPath) - 1])
    elif FinalFinalFinalPath[len(FinalFinalFinalPath) - 1] < FinalFinalFinalPath[len(FinalFinalFinalPath) - 2]:
        inrement = FinalFinalFinalPath[len(FinalFinalFinalPath) - 2]
        while inrement != FinalFinalFinalPath[len(FinalFinalFinalPath) - 1]:
            inrement = inrement - 1
            RoadNotTaken.append(inrement)
    return RoadNotTaken
    # ************************************************************************************#
def SorintImportantPokemons():
    ############# Finding out which node is closest to the pokemon and sorting by value ###########
    # print(PokemonsList)
    PokeDataList = []
    SinglePokeTuple_Pos_Val_ClosNod_DistFromAgen_ValDistRatio_Path = ()
    for i in range(0, len(PokemonsList)):
        SinglePokeTuple_Pos_Val_ClosNod_DistFromAgen_ValDistRatio_Path = (
        PokemonsList[i], PokemonsList[i].get("value"),
        WhatIsTheClosestNodeToThisPokemon(
            PokemonsList[i],
            nGraph), float(-1.1), (-0.6454),
        [0, 0, 0])
        PokeDataList.append(SinglePokeTuple_Pos_Val_ClosNod_DistFromAgen_ValDistRatio_Path)
        # print(SinglePokeTuple_Pos_Val_ClosNod_DistFromAgen)
    SemiPriorityQue = sorted(PokeDataList, key=lambda x: x[1], reverse=True)
    PokemonHitchHikingList = []
    ###############################################################################################
    ######################### Pokemon data priortizing and gathering ####################################
    print("\n~~~~ Pokemons Ordered and hitch-hiking list ~~~~\n\t")
    for i in range(0, len(SemiPriorityQue)):
        SemiPriorityQue[i] = list(SemiPriorityQue[i])
        ##~~~~~~~~~~~~ Get agent position ~~~~~~~~~~~~~~~~~~~~~~~~##
        # print(agents[0].__dict__.get("pos").split(","))
        # kkkk = {"pos": [agents[0].__dict__.get("pos")]}
        # print("kkkk="+str(kkkk))
        tempForAlgo = {}
        #print(tempForAlgo)
        tempForAlgo.update({"pos": agents[0].__dict__.get("pos").split(",")})
        #print(str(tempForAlgo))
        tempAgentPosition = WhatIsTheClosestNodeToThisPokemon(tempForAlgo, nGraph)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        DijekstraPath = GGraphAlgo.shortest_path(tempAgentPosition, 5)[1]
        SemiPriorityQue[i][3] = GGraphAlgo.shortest_path(tempAgentPosition, i)[0]
        if SemiPriorityQue[i][3] != 0:
            SemiPriorityQue[i][4] = (float(SemiPriorityQue[i][1]) / float(SemiPriorityQue[i][3]))
        else:
            SemiPriorityQue[i][4] = 999999999  ## really high ratio value/distance
        SemiPriorityQue[i][5] = GGraphAlgo.shortest_path(tempAgentPosition, i)[1]
        SemiPriorityQue[i] = tuple(SemiPriorityQue)[i]
        # print(SemiPriorityQue[i])
        tttttemp = isTherePokeOnMyWay2MostValuable(SemiPriorityQue[i][5], PokemonsList, GGraphAlgo.nGraph)
        if len(tttttemp) > 0:
            # print(tttttemp)
            PokemonHitchHikingList.append(tttttemp)
    FinalSortedQue = sorted(SemiPriorityQue, key=lambda x: x[4], reverse=True)
    # print(FinalSortedQue)
    ReturnTuple = (SemiPriorityQue, FinalSortedQue, PokemonHitchHikingList)
    return ReturnTuple
def FinalOrgnize(FinalSortedQue):
    ######################################################################################################
    ##~~~~~~~~ last orgnizing before walk ~~~~~~~~##
    NodesQue = []
    for i in range(0, len(FinalSortedQue)):
        NodesQue.append(FinalSortedQue[i][2])
    print("Path Queue         : " + str(NodesQue))
    print("Hitch-Hiking Queue : " + str(PokemonHitchHikingList) + "\n\n")
    #### _____ Spliting the task queue to half to get only valuable pokemons ______#####
    for i in range(0, int(len(NodesQue) / 2)):
        NodesQue.pop()
        FinalSortedQue.pop()
    print(NodesQue)
    print(FinalSortedQue)
    #####__________________________________________________________________________######
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    ### ~~~~~~~~ WALKING LIKE IM TALKING WALKINGWALKING LIKE IM TALKING ~~~~~~~~~###
    FinalFinalFinalPath = []
    FinalFinalFinalPath.append(0)
    print("\t####### Walking.. #######")
    for i in range(0, len(FinalSortedQue)):
        TempDestination = FinalSortedQue[i][2]
        doingAlso = -1
        for n in range(0, len(PokemonHitchHikingList)):
            for k in range(0, len(PokemonHitchHikingList[n])):
                if PokemonHitchHikingList[n][k] == TempDestination and PokemonHitchHikingList[n][k] != -1:
                    doingAlso = PokemonHitchHikingList[n][k]
                    PokemonHitchHikingList[n][k] = -1
                    # print(PokemonHitchHikingList)
        if doingAlso != -1:
            print("\t\tAlso on the way : node[" + str(doingAlso) + "]")
            FinalFinalFinalPath.append(doingAlso)
        else:
            print("\tGo to node[" + str(TempDestination) + "]")
            FinalFinalFinalPath.append(TempDestination)
    print("\t#########################")
    ReturnTuple = (FinalFinalFinalPath, NodesQue, FinalSortedQue)
    return ReturnTuple
    ### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))
while True:

    # ~~~~~~~~~~~~~~~~~~~~~~~~~#
    client.add_agent("{\"id\":0}")
    # client.add_agent("{\"id\":1}")
    # client.add_agent("{\"id\":2}")
    print("\n~~~~~ Agents ~~~~~\n\t")
    print(client.get_agents())
    client.start()
    agents = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    ####################################################################

    pokemons = client.get_pokemons()
    pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
    # ~~~ Get Pokemons List ~~~#
    PokemonsList = StrangeObject2Dictionaty(pokemons_obj)


    ttttuple = SorintImportantPokemons()
    SemiPriorityQue = ttttuple[0]
    FinalSortedQue = ttttuple[1]
    PokemonHitchHikingList = ttttuple[2]
    FinaleTupleee = FinalOrgnize(FinalSortedQue)
    FinalFinalFinalPath = FinaleTupleee[0]
    NodesQue = FinaleTupleee[1]
    FinalSortedQue = FinaleTupleee[2]

    # print(agents[1])
    # print(agents[2])

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ BEGIN SCREEN ANIMATION @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    i = 1
    # nGraph.printNodesDic()
    while client.is_running() == 'true':

        RoadNotTaken = CalculatePath1(FinalFinalFinalPath)
        # print(RoadNotTaken)

        screen.blit(bg, (0, 0))
        pokemons = json.loads(client.get_pokemons(),
                              object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        for p in pokemons:
            p.type = random.randint(0, 5)

        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        agents = json.loads(client.get_agents(),
                            object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]
        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        # refresh surface
        # draw nodes
        for n in graph.Nodes:
            x = my_scale(n.pos.x, x=True)
            y = my_scale(n.pos.y, y=True)
            screen.blit(Rock, (int(x) - 25, int(y)))
            # draw the node id
            id_srf = FONT.render(str(n.id), True, Color(32, 32, 32))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)
        # draw edges
        for e in graph.Edges:
            # find the edge nodes
            src = next(n for n in graph.Nodes if n.id == e.src)
            dest = next(n for n in graph.Nodes if n.id == e.dest)
            # scaled positions
            src_x = my_scale(src.pos.x, x=True)
            src_y = my_scale(src.pos.y, y=True)
            dest_x = my_scale(dest.pos.x, x=True)
            dest_y = my_scale(dest.pos.y, y=True)
            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))
        # draw agents
        for agent in agents:
            screen.blit(hero, (int(agent.pos.x) - 20, int(agent.pos.y) - 20))
        # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
        for p in pokemons:
            if p.pos.y > 440 or p.pos.x > 820:
                screen.blit(PokemonsTypes[WaterPokemonRandom], (int(p.pos.x) - 20, int(p.pos.y) - 20))
            else:
                screen.blit(PokemonsTypes[GroundPokemonRandom], (int(p.pos.x) - 20, int(p.pos.y) - 20))
        # update screen changes
        display.update()
        clock.tick(60)
        AgentID = 0

        if i != len(RoadNotTaken):
            i = WalkSpecificPath(i, RoadNotTaken[i], RoadNotTaken, AgentID, pokemons)
        else:
            break

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

