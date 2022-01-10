from math import inf

from SingleEdge import SingleEdge
from SingleNode import SingleNode
import sys
from GraphInterface import *
class DiGraph(GraphInterface):
    EdgeSrcDic = {}

    def __init__(self):
        self.NodeCount = 0
        self.EdgeCount = 0
        self.NodeDic = {}
        self.EdgeSrcDic = {}
        self.OperationsMC = 0
    def AddNode(self,node):
        if self.NodeDic.__contains__(node.id):
            print("Node already Exists")
            self.OperationsMC = self.OperationsMC +1
            return False
        else:
            self.NodeDic[node.id] = node
            self.NodeCount = self.NodeCount+1
            self.OperationsMC = self.OperationsMC +1
            return True
    def AddEdge(self,EEdge):
        #print(str(self.EdgeSrcDic.keys())+"   searching for - "+str(EEdge.Src.id))
        if self.EdgeSrcDic.keys().__contains__(EEdge.Src.id):
            #print("Contains this source")
            if self.EdgeSrcDic.get(EEdge.Src.id).get(EEdge.Dest.id)!=None: # ~~~   if Edgegraph on src and dest not empty
                print("Src #"+str(EEdge.Src.id)+" and Dest #"+str(EEdge.Dest.id)+" already exist")
                self.OperationsMC = self.OperationsMC + 1
            else:# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Add new src edge
                #print("Have src but dont have dest so creating dest inside src")
                self.EdgeSrcDic[EEdge.Src.id][EEdge.Dest.id] = EEdge
                self.EdgeCount = self.EdgeCount + 1
                self.OperationsMC = self.OperationsMC + 1
        else:
            #print("Creating new src ")
            self.EdgeSrcDic[EEdge.Src.id] = {}
            self.EdgeSrcDic[EEdge.Src.id][EEdge.Dest.id] = EEdge
            self.EdgeCount = self.EdgeCount+1
            self.OperationsMC = self.OperationsMC +1
    def printNodesDic(self):
        for items in self.NodeDic:
            print("~~ "+str(items)+" -> "+str(self.NodeDic[items]))
            self.OperationsMC = self.OperationsMC +1
    def printEdgesDic(self):
        for items in self.EdgeSrcDic:
            print("~ SOURCE #"+str(items)+" ->")
            for subitems in self.EdgeSrcDic.get(items):
                print(self.EdgeSrcDic.get(items).get(subitems))
                self.OperationsMC = self.OperationsMC + 1
    def printEntireGraph(self):
        print("\n=========================== NODES SET ("+str(self.NodeCount)+") =========================")
        self.printNodesDic()
        print("\n===================================================================")
        print("\n========================== EDGES SET ("+str(self.EdgeCount)+") ==========================")
        self.printEdgesDic()
        print("\n===================================================================\n")
        self.OperationsMC = self.OperationsMC + 1
    def v_size(self) -> int:
        return self.NodeCount
    def e_size(self) -> int:
        return self.EdgeCount
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        tuple0 = (inf,inf)
        if pos == None:
            temp = SingleNode(node_id, tuple0[0], tuple0[1])
            return self.AddNode(temp)
        else:
            temp = SingleNode(node_id, pos[0], pos[1])
            return self.AddNode(temp)
    def remove_node(self, node_id: int) -> bool:
        if self.NodeDic.__contains__(node_id):
            if self.NodeDic.pop(node_id)!=None:
                self.OperationsMC = self.OperationsMC + 1
                return True
            return False
        else:
            return False
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        Node1temp = self.NodeDic.get(id1)
        Node2temp = self.NodeDic.get(id2)
        if Node1temp and Node2temp!=None:
            a = True
            EdgeTemp = SingleEdge(Node1temp, Node2temp, weight)
            self.AddEdge(EdgeTemp)
            self.OperationsMC = self.OperationsMC +1
            return True
        return False
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        Node1temp = self.NodeDic.get(node_id1)
        Node2temp = self.NodeDic.get(node_id2)
        if Node1temp and Node2temp!=None:
            a = True
            self.EdgeSrcDic[node_id1].pop(node_id2)
            self.OperationsMC = self.OperationsMC +1
            return True
        return False
    def get_all_v(self) -> dict:
        return self.NodeDic
    def all_in_edges_of_node(self, id1: int) -> dict:
        TempDic = {}
        if self.EdgeSrcDic.get(id1)!= None:
            for subitems in self.EdgeSrcDic.get(id1):
                #print(self.EdgeSrcDic.get(id1).get(subitems))
                TempDic[self.EdgeSrcDic.get(id1).get(subitems).Dest.id] = self.EdgeSrcDic.get(id1).get(subitems).Weight
                self.OperationsMC = self.OperationsMC + 1
        if len(TempDic)>0:
            return TempDic
        else:
            return None
    def all_out_edges_of_node(self, id1: int) -> dict:
        TempDic = {}
        for items in self.EdgeSrcDic:
            for subitems in self.EdgeSrcDic.get(items):
                if self.EdgeSrcDic.get(items).get(subitems).Dest.id == id1:
                    #print(self.EdgeSrcDic.get(items).get(subitems))
                    TempDic[self.EdgeSrcDic.get(items).get(subitems).Src.id] = self.EdgeSrcDic.get(items).get(subitems).Weight
                    self.OperationsMC = self.OperationsMC + 1
        return TempDic
    def get_mc(self) -> int:
        return self.OperationsMC