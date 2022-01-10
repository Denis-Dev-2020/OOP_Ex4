import random
import json
from math import inf
from typing import List
from GraphAlgoInterface import *
import GraphInterface
from Graph import *
from LoadFromJSON import *
from Dijkstra import *
import itertools
class GraphAlgo(GraphAlgoInterface):
    nGraph = DiGraph()
    def __init__(self,Graphh=DiGraph()):
        self.nGraph = Graphh
    def CopyFrom(self,Graph):
        self.nGraph.NodeDic = Graph.NodeDic
        self.nGraph.EdgeSrcDic = Graph.EdgeSrcDic
        self.nGraph.NodeCount = Graph.NodeCount
        self.nGraph.EdgeCount = Graph.EdgeCount
        self.nGraph.OperationsMC = Graph.OperationsMC
    def get_graph(self) -> GraphInterface:
        return self.nGraph
    def load_from_json(self, file_name: str) -> bool:
        Load2Graph(file_name, self.nGraph)
        if len(self.nGraph.NodeDic)>0:
            return True
        else:
            return False
    def EncodeSingleNode(self,SSingleNode:SingleNode):
        strPos = ""+str(SSingleNode.x)+","+str(SSingleNode.y)
        return {"pos" : strPos,"id" : SSingleNode.id}
    def EncodeSingleEdge(self,SSingleEdge:SingleEdge):
        return {"src" : SSingleEdge.Src.id,"w" : SSingleEdge.Weight,"dest" : SSingleEdge.Dest.id}
    def EncoderEdges(self,dummy):
        EdgesList = []
        for itemsI in self.nGraph.EdgeSrcDic:
            for itemsJ in self.nGraph.EdgeSrcDic.get(itemsI):
                workingOn = self.nGraph.EdgeSrcDic.get(itemsI).get(itemsJ)
                EdgesList.append(self.EncodeSingleEdge(workingOn))
        return EdgesList
    def EncoderNodes(self,dummy):
        totalNodesDumps = []
        allNodes = list(self.nGraph.get_all_v())
        for i in range(0,len(allNodes)):
            workingOn = self.nGraph.NodeDic.get(allNodes[i])
            totalNodesDumps.append(self.EncodeSingleNode(workingOn))
        return totalNodesDumps
    def EncodeEntireGraph(self,dummy):
        EntireGraph = {}
        EntireGraph.update({"Edges" : self.EncoderEdges(None)})
        EntireGraph.update({"Nodes" : self.EncoderNodes(None)})
        return EntireGraph
    def save_to_json(self, file_name: str) -> bool:
        if self.nGraph.NodeCount>0 and self.nGraph.EdgeCount>0:
            toPrint = json.dumps(self, default=self.EncodeEntireGraph, indent=2)
            json_file = open(file_name, "w")
            json_file.write(str(toPrint))
            json_file.close()
            return True
        else:
            return False
    def sortSecond(val):
        return val[1]
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        return Dijekstra(self.nGraph,id1,id2)
    def DFS(self,key:int):
        #print(self.nGraph.printNodesDic())
        NodeStack = []  ##~~~~~~~~~~ General followup stack
        allNodes = self.nGraph.get_all_v()
        NodeDataT = allNodes.get(key)
        NodeStack.append(NodeDataT.id)
        NodeDataT.tag = 1
        while len(NodeStack)>0:
            print("NodeStack = "+str(NodeStack))
            NodeDataT = NodeStack.pop()
            NeiborEdges = self.nGraph.all_in_edges_of_node(NodeDataT)
            if NeiborEdges!=None:
                NeiborEdgesKeyset = list(NeiborEdges.keys())  ##~~~ temp edges neibors stack
                print("NeiborKeyset = " + str(NeiborEdgesKeyset))
                while len(NeiborEdgesKeyset) > 0:
                    EdgeTempED = NeiborEdgesKeyset.pop()
                    if allNodes.get(EdgeTempED).tag != 1:
                        allNodes.get(EdgeTempED).tag = 1
                        NodeStack.append(allNodes.get(EdgeTempED).id)
        #print(self.nGraph.printNodesDic())
    def GraphAlgoInstance(self):
        return "                      "+str(317623189)
    def CanIGetFromEveryNodeToAnyNode(self):
        ###~~~~~~~~~~~~~~~~~` basic quick answers ~~~~~~~~~~~~~~~~~~~~~~~#
        if self.nGraph==None:
            return True
        if self.nGraph.EdgeCount == 0 or self.nGraph.NodeCount == 1:
            return True
        if (self.nGraph.EdgeCount+1) < self.nGraph.NodeCount:
            return False
        ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ###~~~~~~~~~~~~~ making a stack like in dfs the iterating each element ~~~~~~~~#
        allNodes = self.nGraph.get_all_v()
        NodesKeyset = list(allNodes.keys())
        print(NodesKeyset)
        while len(NodesKeyset)>0:
            NodedataT = NodesKeyset.pop()
            self.DFS(NodedataT)    ##~~~~~~ itereating depth to check all possibilities
            #####~~~~~~ making another stack to be sub stack of each previous stack element ~~~~###
            allNodes2 = self.nGraph.get_all_v()
            NodesKeyset2 = list(allNodes.keys())
            while len(NodesKeyset2)>0:
                NodedataT = NodesKeyset2.pop()
                if self.nGraph.get_all_v().get(NodedataT).tag!=1:
                    ###~~~~~~~~~~~~~~~~~~~ Cleaning Tags ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`####
                    tempCleanTag = list(self.nGraph.get_all_v().keys())
                    while len(tempCleanTag)>0:
                        self.nGraph.NodeDic.get(tempCleanTag.pop()).tag = 0
                    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~###
                    return False
                self.nGraph.get_all_v().get(NodedataT).tag = 0
        tempCleanTag2 = list(self.nGraph.get_all_v().keys())
        ###~~~~~~~~~~~~~~~~~~~ Cleaning Tags ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`####
        while len(tempCleanTag2) > 0:
            self.nGraph.NodeDic.get(tempCleanTag2.pop()).tag = 0
        ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~###
        return True
    def isThereEdgeConnecting(self,src,dest):
        if self.nGraph.EdgeSrcDic.get(src)!=None:
            if self.nGraph.EdgeSrcDic.get(src).get(dest)!=None:
                return True
            return False
        return False
    def CheckIfPathExists(self,ListInt):
        Answer = False
        for i in range(0,len(ListInt)-1):
            if self.isThereEdgeConnecting(ListInt[i],ListInt[i+1]):
                Answer = True
            else:
                return False
        return Answer
    def CalculateDistFromPathList(self,ListInt):
        TotalDist = 0
        for i in range(0,len(ListInt)-1):
            TotalDist = TotalDist + self.nGraph.EdgeSrcDic.get(ListInt[i]).get(ListInt[i+1]).Weight
        return TotalDist
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if self.CanIGetFromEveryNodeToAnyNode:
            ShortestPath = ()
            ShortestDist = inf
            permutations = list(itertools.permutations(node_lst))
            while len(permutations) > 0:
                self.nGraph.OperationsMC = self.nGraph.OperationsMC +1
                workOn = permutations.pop()
                ########### ~~~ check only elegible paths ~~~~~############
                if self.CheckIfPathExists(workOn):
                    # print(str(workOn) +"  Dist = " + str(self.CalculateDistFromPathList(workOn)))
                    if self.CalculateDistFromPathList(workOn) < ShortestDist:
                        ShortestDist = self.CalculateDistFromPathList(workOn)
                        ShortestPath = workOn
                ###########################################################
            ReturnList = [1, 2]
            ReturnList[0] = list(ShortestPath)
            ReturnList[1] = ShortestDist
            ##print("Shortest TSP Path = "+str(ReturnList))
            return ReturnList
        else:
            ReturnList2 = [1,2]
            ReturnList2[0] = []
            ReturnList2[1] = inf
            return ReturnList2
    def centerPoint(self) -> (int, float):
        ecentricity = []
        LargestInTheHood = []
        CenterNode = -1
        SmallestInTheHood = []
        ShortestDistAmong2 = inf
        LongestDistAmong2 = 0
        allNodes = list(self.nGraph.get_all_v())
        for i in range(0,len(allNodes)):
            for j in range(0,len(allNodes)):
                self.nGraph.OperationsMC = self.nGraph.OperationsMC +1
                newTempList = []
                newTempList.append(allNodes[i])
                newTempList.append(allNodes[j])
                if self.CheckIfPathExists(newTempList):
                    #print(str(newTempList)+"  dist = "+str(self.CalculateDistFromPathList(newTempList)))  # Values
                    if self.CalculateDistFromPathList(newTempList)>LongestDistAmong2:
                        LongestDistAmong2 = self.CalculateDistFromPathList(newTempList)
                        LargestInTheHood = newTempList
            #print("Calculate here")
            if LongestDistAmong2>0:
                ecentricity.append(LargestInTheHood)
                LongestDistAmong2 = 0
        #print(ecentricity)
        if len(ecentricity)>0:
            for i in range(0,len(ecentricity)):
                tempEcentCouple = ecentricity.pop()
                #print(tempEcentCouple)
                if self.CheckIfPathExists(tempEcentCouple):
                    #print(str(tempEcentCouple)+"  dist = "+str(self.CalculateDistFromPathList(tempEcentCouple)))  # Values
                    if self.CalculateDistFromPathList(tempEcentCouple)<ShortestDistAmong2:
                        ShortestDistAmong2 = self.CalculateDistFromPathList(tempEcentCouple)
                        SmallestInTheHood = tempEcentCouple
        #print(ShortestDistAmong2)
        #print(SmallestInTheHood)
        if len(SmallestInTheHood)>0:
            CenterNode = SmallestInTheHood[0]
        ReturnList = [1,2]
        ReturnList[0] = CenterNode
        ReturnList[1] = ShortestDistAmong2
        return ReturnList
    def plot_graph(self) -> None:
        allNodes = list(self.nGraph.get_all_v())
        for i in range(0,len(allNodes)):
            self.nGraph.OperationsMC = self.nGraph.OperationsMC + 1
            workingOn = self.nGraph.NodeDic.get(allNodes[i])
            if workingOn.x == inf and workingOn.y == inf:
                #print(workingOn)
                self.nGraph.NodeDic.get(allNodes[i]).x = random.randint(0,700)
                self.nGraph.NodeDic.get(allNodes[i]).y = random.randint(0,700)