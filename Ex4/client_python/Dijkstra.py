from math import inf
from Graph import *

def sortSecond(val):
    return val[1]
def Dijekstra(Graph,src,dest):
    if Graph.all_in_edges_of_node(src)!=None:
        ################################## initialization ################################
        DijekstraPath = []
        white = 0
        red = 1
        TempDic = Graph.get_all_v()
        KeySet = list(TempDic.keys())
        PriorityQueue = []
        for items in TempDic:
            TempDic[items].info = float(inf)
            TempDic[items].tag = white
            if src == items:
                TempDic[items].info = 0
            else:
                PriorityQueue.append((TempDic[items].id, TempDic[items].info))
        DijekstraPath.append(src)
        ####################################################################################
        PriorityQueue.append((TempDic[src].id, TempDic[src].info))
        PriorityQueue.sort(key=sortSecond, reverse=True)
        # print(PriorityQueue)
        # ~~~~~~~~ my p.queue is a list and I go backwards so pop() is like the first variable ~~~~~~#
        while len(PriorityQueue) > 0:
            workingOn = PriorityQueue.pop()[0]
            Neibors = Graph.all_in_edges_of_node(workingOn)
            if TempDic[workingOn].tag != red and Neibors != None:
                TempKeySet = list(Neibors.keys())  # Just a conviniate convertion
                #print(TempKeySet)
                for i in range(0, len(TempKeySet)):  # looping through neibors of "workingOn" node
                    # print(TempKeySet[i])
                    if Neibors.get(TempKeySet[i]) + TempDic[workingOn].info < TempDic[TempKeySet[i]].info:
                        # print("if "+str(Neibors.get(TempKeySet[i]))+"+"+str(TempDic[workingOn].info)+"<"+str(TempDic[TempKeySet[i]].info))
                        TempDic[TempKeySet[i]].info = Neibors.get(TempKeySet[i]) + TempDic[workingOn].info
                        TempDic[TempKeySet[i]].prevClosestNode = workingOn
                PriorityQueue.sort(key=sortSecond, reverse=True)  ## always prioritise shortest
            TempDic[workingOn].tag = red
        if TempDic[dest].prevClosestNode > -1:
            ####### ~~~~ Tracing this path ~~~~~~~~ #########
            trace = []
            tempDest = dest
            trace.append(dest)
            while tempDest != src:
                trace.append(TempDic[tempDest].prevClosestNode)
                tempDest = TempDic[tempDest].prevClosestNode
            trace.reverse()
            totalDist = 0
            ###~~~~~~~~~~ colecting dist from trace ~~~~~~~~~~~~~~~~~~~~~~~~~###
            for i in range(0, len(trace) - 1):
                # print(Graph.EdgeSrcDic.get(trace[i]).get(trace[i+1]))
                if Graph.EdgeSrcDic.get(trace[i]).get(trace[i + 1]) != None:
                    totalDist = totalDist + Graph.EdgeSrcDic.get(trace[i]).get(trace[i + 1]).Weight
            ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
            ####~~~~~~~~ Cleaning original nodes ~~~~~~~~~~~~`###
            for items in TempDic:
                TempDic[items].info = 0
                TempDic[items].tag = 0
                TempDic[items].prevClosestNode = 0
            ####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
            tupleAnswer = (totalDist, trace)
            # print(trace)
            # print(totalDist)
            # Graph.printNodesDic()
            return tupleAnswer
        else:
            FalseTuple = (float('inf'), [])
            return FalseTuple
    else:
        FalseTuple = (float('inf'), [])
        return FalseTuple