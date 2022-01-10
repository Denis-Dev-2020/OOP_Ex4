##################################### Node Data ##########################################
class SingleNode:
    id = 0
    x = 0
    y = 0
    info = 0
    tag = 0
    prevClosestNode = -1
    def __init__(self,idd,xx,yy):
        self.id = idd
        self.x = xx
        self.y = yy
    def copyConstr(self,a):
        self.id = a.id
        self.x = a.x
        self.y = a.y
        self.info = a.info
    def compare2OtherNode(self,a):
        sameID = False
        sameX = False
        sameY = False
        sameInfo = False
        sameAll = False
        if self.id == a.id:
            sameID = True
        if self.x == a.x:
            sameX = True
        if self.y == a.y:
            sameY = True
        if self.info == a.info:
            sameInfo = True
        if sameID and sameX and sameY and sameInfo and True:
            return True
        else:
            return False
    def setCoords(self,xx,yy):
        self.x = xx
        self.y = yy
    def getCoords(self):
        Vector2Coords = self.x ,self.y
        return Vector2Coords
    def setId(self,IId):
        self.id = IId
    def getId(self):
        return self.id
    def setInfo(self,iinfo):
        self.info = iinfo
    def getInfo(self):
        return self.info
    def setTag(self,ttag):
        self.tag = ttag
    def getTag(self):
        return self.tag
    def __str__(self):
        return "~~~~~~ Node #"+str(self.id)+" ~~~~~~~~~~\n"+"" \
                "(x, y) = "+str(self.getCoords())+ \
                "\nInfo = "+str(self.info)+ \
                "\nTag = "+str(self.tag)+"" \
                "\nprevClosestNode = "+str(self.prevClosestNode)+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
##########################################################################################