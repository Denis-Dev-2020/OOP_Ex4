import json
from math import inf
from Graph import DiGraph
from SingleEdge import SingleEdge
from SingleNode import SingleNode
def openJSON(path):
    json_file = open(path)
    temp = json.load(json_file)
    json_file.close()
    return temp
def Load2GraphExplicit(JsonData,Graph):
    #print("Loading nodes..\n")
    Nodes = JsonData.get("Nodes")
    #### ~~~~~~~~~~~` if no position presented ~~~~~~~~~~~~~~~~~~~~~##
    if len(Nodes[0])==1:
        for i in range(0, len(Nodes)):
            POSx = inf
            POSy = inf
            ID = Nodes[i].get("id")
            tempTuple = (POSx, POSy)
            Graph.add_node(ID, tempTuple)
            #print("(" + str(POSx) + "," + str(POSy) + "," + str(ID) + ")")
        #print("Loading edges..\n")
        Edges = JsonData.get("Edges")
        for i in range(0, len(Edges)):
            SRC = Edges[i].get("src")
            W = Edges[i].get("w")
            DEST = Edges[i].get("dest")
            Graph.add_edge(SRC, DEST, W)
            # print("("+str(SRC)+","+str(W)+","+str(DEST)+")")
    #####################################################################
    else:
    ################ if there is position #############################
        for i in range(0, len(Nodes)):
            Possition = Nodes[i].get("pos")
            PossitionSplited = Possition.split(',')
            POSx = PossitionSplited[0]
            POSy = PossitionSplited[1]
            ID = Nodes[i].get("id")
            tempTuple = (POSx, POSy)
            Graph.add_node(ID, tempTuple)
            #print("(" + str(POSx) + "," + str(POSy) + "," + str(ID) + ")")
        #print("Loading edges..\n")
        Edges = JsonData.get("Edges")
        for i in range(0, len(Edges)):
            SRC = Edges[i].get("src")
            W = Edges[i].get("w")
            DEST = Edges[i].get("dest")
            Graph.add_edge(SRC, DEST, W)
            # print("("+str(SRC)+","+str(W)+","+str(DEST)+")")
    ######################################################################
def Load2Graph(path,Graph):
    JsonData = openJSON(path)
    #print("Loading nodes..\n")
    Nodes = JsonData.get("Nodes")
    #### ~~~~~~~~~~~` if no position presented ~~~~~~~~~~~~~~~~~~~~~##
    if len(Nodes[0])==1:
        for i in range(0, len(Nodes)):
            POSx = inf
            POSy = inf
            ID = Nodes[i].get("id")
            tempTuple = (POSx, POSy)
            Graph.add_node(ID, tempTuple)
            #print("(" + str(POSx) + "," + str(POSy) + "," + str(ID) + ")")
        #print("Loading edges..\n")
        Edges = JsonData.get("Edges")
        for i in range(0, len(Edges)):
            SRC = Edges[i].get("src")
            W = Edges[i].get("w")
            DEST = Edges[i].get("dest")
            Graph.add_edge(SRC, DEST, W)
            # print("("+str(SRC)+","+str(W)+","+str(DEST)+")")
    #####################################################################
    else:
    ################ if there is position #############################
        for i in range(0, len(Nodes)):
            Possition = Nodes[i].get("pos")
            PossitionSplited = Possition.split(',')
            POSx = PossitionSplited[0]
            POSy = PossitionSplited[1]
            ID = Nodes[i].get("id")
            tempTuple = (POSx, POSy)
            Graph.add_node(ID, tempTuple)
            #print("(" + str(POSx) + "," + str(POSy) + "," + str(ID) + ")")
        #print("Loading edges..\n")
        Edges = JsonData.get("Edges")
        for i in range(0, len(Edges)):
            SRC = Edges[i].get("src")
            W = Edges[i].get("w")
            DEST = Edges[i].get("dest")
            Graph.add_edge(SRC, DEST, W)
            # print("("+str(SRC)+","+str(W)+","+str(DEST)+")")
    #####################################################################3