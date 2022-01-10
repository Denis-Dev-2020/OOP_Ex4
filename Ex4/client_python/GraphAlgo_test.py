import unittest
from GraphAlgo import *
from Graph import *

class test_GraphAlgos(unittest.TestCase):
    def test_BasicInput(self):
        newGraph1 = DiGraph()
        newGraphAlgo = GraphAlgo(newGraph1)
        newGraphAlgo.load_from_json("data/A6.json")

        pos = (35.18958953510896,32.10785303529412)
        self.assertTrue(newGraphAlgo.nGraph.add_node(1,pos)==False)

        pos = (35.18958953510896,32.10785303529412)
        self.assertTrue(newGraphAlgo.nGraph.add_node(1,pos)==False)

        pos = (35.197528356739305,32.1053088)
        self.assertTrue(newGraphAlgo.nGraph.add_node(3,pos)==False)

        pos = (35.20582803389831,32.10625380168067)
        self.assertTrue(newGraphAlgo.nGraph.add_node(5,pos)==False)

        pos = (35.18910131880549,32.103618700840336)
        self.assertTrue(newGraphAlgo.nGraph.add_node(6,pos)==False)

        pos = (35.18910131880549,32.103618700840336)
        self.assertTrue(newGraphAlgo.nGraph.add_node(5,pos)==False)

        pos = (2,3)
        self.assertTrue(newGraphAlgo.nGraph.add_node(5,pos)==False)

        pos = (22,3)
        self.assertTrue(newGraphAlgo.nGraph.add_node(5,pos)==False)

        pos = (2,33)
        self.assertTrue(newGraphAlgo.nGraph.add_node(5,pos)==False)

        pos = (2,33)
        self.assertTrue(newGraphAlgo.nGraph.add_node(7,pos)==True)

        pos = (2,33)
        self.assertTrue(newGraphAlgo.nGraph.add_node(8,pos)==True)

        pos = (2,33)
        self.assertTrue(newGraphAlgo.nGraph.add_node(9,pos)==True)

        pos = (2,33)
        self.assertTrue(newGraphAlgo.nGraph.add_node(10,pos)==True)


    def test_ShortestPath(self):
        newGraph1 = DiGraph()
        newGraphAlgo = GraphAlgo(newGraph1)
        newGraphAlgo.load_from_json("data/A2.json")
        ShortestPath = newGraphAlgo.shortest_path(1,3)[0]
        print(ShortestPath==2.8647559158521916)
        self.assertAlmostEqual(ShortestPath,2.8647559158521916)

        ShortestPath = newGraphAlgo.shortest_path(7,3)[0]
        print(ShortestPath==4.48917342727725)
        self.assertAlmostEqual(ShortestPath,4.48917342727725)

        ShortestPath = newGraphAlgo.shortest_path(7,20)[0]
        print(ShortestPath==6.868079076521861)
        self.assertAlmostEqual(ShortestPath,6.868079076521861)

        ShortestPath = newGraphAlgo.shortest_path(7,23)[0]
        self.assertAlmostEqual(ShortestPath,6.868079076521861)
        print(ShortestPath==6.868079076521861)

    def test_TSP(self):
        newGraph1 = DiGraph()
        newGraphAlgo = GraphAlgo(newGraph1)
        newGraphAlgo.load_from_json("data/A6.json")
        ListAnswer = [5,1,2,6,3,4]
        ListInput = [1,2,3,4,5,6]
        ListTemp = newGraphAlgo.TSP(ListInput)[0]
        self.assertAlmostEqual(ListAnswer[0],ListTemp[0])
        self.assertAlmostEqual(ListAnswer[1],ListTemp[1])
        self.assertAlmostEqual(ListAnswer[2],ListTemp[2])
        self.assertAlmostEqual(ListAnswer[3],ListTemp[3])
        self.assertAlmostEqual(ListAnswer[4],ListTemp[4])
        self.assertAlmostEqual(ListAnswer[5],ListTemp[5])

    def test_Center(self):

        newGraph1 = DiGraph()
        newGraphAlgo1 = GraphAlgo(newGraph1)
        newGraphAlgo1.load_from_json("data/A1.json")
        self.assertAlmostEqual(newGraphAlgo1.centerPoint()[0],0)

        newGraph2 = DiGraph()
        newGraphAlgo2 = GraphAlgo(newGraph2)
        newGraphAlgo2.load_from_json("data/A2.json")
        self.assertAlmostEqual(newGraphAlgo2.centerPoint()[0],27)

        newGraph3 = DiGraph()
        newGraphAlgo3 = GraphAlgo(newGraph3)
        newGraphAlgo3.load_from_json("data/A3.json")
        self.assertAlmostEqual(newGraphAlgo3.centerPoint()[0],29)

        newGraph4 = DiGraph()
        newGraphAlgo4 = GraphAlgo(newGraph4)
        newGraphAlgo4.load_from_json("data/A4.json")
        self.assertAlmostEqual(newGraphAlgo4.centerPoint()[0],0)

        newGraph5 = DiGraph()
        newGraphAlgo5 = GraphAlgo(newGraph5)
        newGraphAlgo5.load_from_json("data/A5.json")
        self.assertAlmostEqual(newGraphAlgo5.centerPoint()[0],47)

        newGraph6 = DiGraph()
        newGraphAlgo6 = GraphAlgo(newGraph6)
        newGraphAlgo6.load_from_json("data/A6.json")
        self.assertAlmostEqual(newGraphAlgo6.centerPoint()[0],3)
