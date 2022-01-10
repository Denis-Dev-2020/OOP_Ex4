from tkinter import *
from GraphAlgo import *
from Graph import *



class RunGUI:
    #~~~~~~~~~~~` windows parameters ~~~~~~~~~~~~~~~~~~~~~~~~~#
    aTemp = GraphAlgo()
    GraphAlgorr = aTemp.GraphAlgoInstance()
    root = Tk()
    root.title('GUI - Python Directed Graph'+str(GraphAlgorr))
    root.geometry("1000x900")
    wwwidth = 1000
    hhheight = 900
    Can = Canvas(root, width=wwwidth, height=hhheight, bg="black")
    boolLoad = False

    MainGraph = DiGraph()
    MainGraphAlgo = GraphAlgo()

    MainGraphAlgo.load_from_json("P0.json")
    #ShowGraph(MainGraphAlgo.nGraph)

    #### ~~~~~~~~~ controls for input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
    LoadFromPPPATHjson = Entry(root,
                               bg="#FFB6C1",
                               cursor="arrow",
                               fg="blue",
                               highlightcolor="black",
                               justify="right",
                               width=10,
                               xscrollcommand="scrollbar",
                               )
    LoadFromPPPATHjson.pack()
    LoadFromPPPATHjson.place(width=100, height=20, x=500)
    #####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def ShowGraph(self,asd):
        GGraph = self.MainGraphAlgo.nGraph
        GGraph.printEntireGraph()
        ##~~~~~~~~~~~` basic canvas setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.Can.pack(pady=20)
        self.Can.create_line(0,self.hhheight/2,self.wwwidth,self.hhheight/2,fill="orange")
        self.Can.create_line(self.wwwidth/2,0,self.wwwidth/2,self.hhheight,fill="orange")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ## ~~~~~~~~~~~~~~~` draw th graph ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        TempNodeDic = GGraph.NodeDic
        TempEdgeDic = GGraph.EdgeSrcDic
        for items in TempNodeDic: ## ~~~~ Nodes first
            NodeX = int(   80000*(float(TempNodeDic.get(items).x)%0.01)   )
            NodeY = int(   80000*(float(TempNodeDic.get(items).y)%0.01)   )
            NodeXsize = NodeX+60
            NodeYsize = NodeY+60
            #print(str(NodeX)+"     "+str(NodeY))
            self.Can.create_oval(NodeX, NodeY,NodeXsize ,NodeYsize , width=3,outline="#FF1493",fill="#551A8B")
        for itemI in TempEdgeDic: ## ~~~~~~ then Edges
            for itemJ in TempEdgeDic.get(itemI):
                RealNodeX1 = TempEdgeDic.get(itemI).get(itemJ).Src.x
                RealNodeY1 = TempEdgeDic.get(itemI).get(itemJ).Src.y
                #print(str(RealNodeX1)+","+str(RealNodeY1))
                NodeX1 = int(80000 * (float(RealNodeX1) % 0.01))+30
                NodeY1 = int(80000 * (float(RealNodeY1) % 0.01))+30
                RealNodeX2 = TempEdgeDic.get(itemI).get(itemJ).Dest.x
                RealNodeY2 = TempEdgeDic.get(itemI).get(itemJ).Dest.y
                NodeX2 = int(80000 * (float(RealNodeX2) % 0.01))+30
                NodeY2 = int(80000 * (float(RealNodeY2) % 0.01))+30
                self.Can.create_line(NodeX1,NodeY1,NodeX2,NodeY2,arrow="last",width=5,fill="#3A5FCD")
        for items in TempNodeDic: ## ~~~~~ then Node Text
            NodeX = int(   80000*(float(TempNodeDic.get(items).x)%0.01)   )
            NodeY = int(   80000*(float(TempNodeDic.get(items).y)%0.01)   )
            self.Can.create_text(NodeX+30,NodeY+30,text = "Node "+str(TempNodeDic.get(items).id),fill="white", font=('Arial','8','bold'))
        self.Can.pack(pady=20)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



        #####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ buttons setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
        buttonLoad = Button(self.root, command=self.LoadFromJSONButt, text="Load From", bg="grey", font=('Arial', '7', 'bold'))
        buttonLoad.pack()
        buttonLoad.place(width=70, height=20, x=420)
        ###########~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
        if self.boolLoad == False:
            self.Can.pack(pady=20)
            self.Can.create_rectangle(0,0,3000,3000,fill="black")
            self.Can.create_line(0, self.hhheight / 2, self.wwwidth, self.hhheight / 2, fill="orange")
            self.Can.create_line(self.wwwidth / 2, 0, self.wwwidth / 2, self.hhheight, fill="orange")
        #print(self.MainGraphAlgo.nGraph.OperationsMC)

        self.root.mainloop()


    def LoadFromJSONButt(self):
        if self.boolLoad == False:
            self.boolLoad = True
            self.Can.delete('all')
            self.MainGraphAlgo = None
            self.MainGraphAlgo = GraphAlgo()
            self.MainGraphAlgo.load_from_json("P0.json")
            self.ShowGraph(self.MainGraphAlgo.nGraph)
        else:
            self.boolLoad = False
            self.Can.delete('all')
            self.ShowGraph(self.MainGraphAlgo.nGraph)