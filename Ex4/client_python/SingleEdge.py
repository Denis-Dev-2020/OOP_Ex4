##################################### Edge Data ##########################################
class SingleEdge:
    info = ''
    tag = ''
    def __init__(self,SSrc,DDest,WWeight):
        self.Src = SSrc
        self.Dest = DDest
        self.Weight = WWeight
    def setSrcAndDest(self,SSrc,DDest):
        self.Src = SSrc
        self.Dest = DDest
    def getSrcAndDest(self):
        Vector2Nodes = self.Src ,self.Dest
        return Vector2Nodes
    def PrintEdge(self):
        print("^^^^^^^^^^^^^^^^ Edge ^^^^^^^^^^^^^^^^^^\n=== From :\n"\
                +str(self.Src)+"\n=== To :\n"+str(self.Dest)+"\n=== Weight :"\
               +str(self.Weight)+"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    def __str__(self):
        return "Edge = {src:"+str(self.Src.id)+" ,dest:"+str(self.Dest.id)+"" \
                        " ,weight:"+str(self.Weight)+" ,info:"+str(self.info)+"}"
##########################################################################################