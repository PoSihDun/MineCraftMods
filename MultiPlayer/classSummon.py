'''There are three different scripts. script #1 calls the functions of script2/3
so when using these scripts run scripts #1- This is script3.'''

'''Script #3 save as classSummon.py'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create(address="192.168.0.142", port=4711)


import time

class ArrowTrap(object):
    def __init__(self, x, y, z, pHeight):
        self.x = x
        self.y = y
        self.z = z

        self.x2 = x
        self.y2 = y
        self.z2 = z

        self.pHeight = pHeight

    def build(self):
        for level in reversed(list(range(self.pHeight))):#Pyramid algorithm
            mc.setBlocks(self.x - level, self.y, self.z - level,
                         self.x + level, self.y, self.z + level, 95)#Glass
            time.sleep(0.25)
            self.y += 1

    def bottom(self):
        for level in reversed(list(range(self.pHeight))):#Pyramid algorithm
            mc.setBlocks(self.x - level, self.y-self.pHeight, self.z - level,
                         self.x2 + level, self.y2, self.z2 + level, 95, 1)#Glass
            time.sleep(0.25)
            self.y += 1

        mc.setBlocks(self.x+1 , self.y-6, self.z+1, self.x-1, self.y-6, self.z-1, 51)#Fire floor

class DiamondTrap(object):
    def __init__(self, x, y, z, pHeight):
        self.x = x
        self.y = y
        self.z = z

        self.pHeight = pHeight

    def buildB(self):
        for level in range(self.pHeight):#Pyramid Algorithm
            mc.setBlocks(self.x - level, self.y, self.z - level,
                         self.x + level, self.y, self.z + level, 95, 4)#Glass
            self.y += 1
            time.sleep(0.05)

        for level in reversed(list(range((self.pHeight-1)))):#Pyramid Algorithm
            mc.setBlocks(self.x - level, self.y, self.z - level,
                         self.x + level, self.y, self.z + level, 95, 4)#Glass
            self.y += 1
            time.sleep(0.05)

        #mc.setBlocks(self.x+1 , self.y-4, self.z+1, self.x-1, self.y-3, self.z-1, 51) #Fire Floor

class EnderWarrior(object):
    def __init__(self, x, y, z, pHeight):
        self.x = x
        self.y = y
        self.z = z

        self.x2 = x
        self.y2 = y
        self.z2 = z

        self.pHeight = pHeight

    def enderOre(self):
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :enderOre x y start")
        for level in range(self.pHeight):#Pyramid Algorthm
            mc.setBlocks(self.x - level, self.y, self.z - level,
                         self.x + level, self.y, self.z + level, 17) #Oak Wood
            self.y += 1
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :enderOre x y finish")

    def enderPumpkin(self):
       
        mc.setBlock(self.x , self.y , self.z, 86) #Pumpkin
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :enderPumpkin x2 y2 finish")
   
    def crafting(self):
    #------------------------------------------------------Crafting table side---------------------------------------------------------------------------#
        mc.setBlock(self.x2 - 2, self.y2 + 1, self.z2, 58)#Crafting Table
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :crafting Table" )

        mc.setBlock(self.x2 - 2, self.y2 + 1, self.z2 + 1, 17)#Oak Wood
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Oak Wood")

        mc.setBlock(self.x2 - 2, self.y2 + 1, self.z2 - 1, 173) #Coal
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :coal")
    #-----------------------------------------------------------Furnace side----------------------------------------------------------------------#
        mc.setBlock(self.x2 + 2, self.y2 + 1, self.z2, 62) #Frunace
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :furnace" )

        mc.setBlock(self.x2 + 2, self.y2 + 1, self.z2 + 1, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Stone")

        mc.setBlock(self.x2 + 2, self.y2 + 1, self.z2 - 1, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Stone")
    #------------------------------------------------------------Chest side---------------------------------------------------------------------#
        mc.setBlock(self.x2, self.y2 + 1, self.z2 + 2, 54) #Chest
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :chest" )

        mc.setBlock(self.x2 + 1, self.y2 + 1, self.z2 + 2, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Oak Wood")

        mc.setBlock(self.x2 - 1, self.y2 + 1, self.z2 + 2, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Stone")
    #-------------------------------------------------------------Enchanting table side--------------------------------------------------------------------#
        mc.setBlock(self.x2, self.y2 + 1, self.z2 - 2, 116)#Enchanting table
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Enchanting table")

        mc.setBlock(self.x2+1, self.y2 + 1, self.z2 - 2, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Stone")

        mc.setBlock(self.x2-1, self.y2 + 1, self.z2 - 2, 1) #Stone
        #mc.postToChat( str(self.x) + " " + str(self.y2) + " :Stone")
    #---------------------------------------------------------------------------------------------------------------------------------#

class FallingSky(object):
    def __init__(self, x, y, z, pHeight):
        self.x = x
        self.y = y
        self.z = z

        self.x2 = x
        self.y2 = y
        self.z2 = z

        self.pHeight = pHeight

    def garvelPyramid(self):#Pyramid algorithm
        for level in range(self.pHeight):
            mc.setBlocks(self.x - level, self.y+5, self.z - level,
                         self.x + level, self.y+5, self.z + level, 13) #Gravel
            self.y += 1
            time.sleep(0.05)

    def garvelPyramidTop(self):#Pyramid algorithm
        for level in range((self.pHeight + 1)):
            mc.setBlocks(self.x - level, self.y+6, self.z - level,
                         self.x + level, self.y+6, self.z + level,  12, 1) #Red Sand
            self.y -= 1
            time.sleep(0.05)

    def garvelPyramidBottom(self):#Pyramid algorithm
        for level in range((self.pHeight + 2)):
            mc.setBlocks(self.x - level, self.y+7, self.z - level,
                         self.x + level, self.y+7, self.z + level,  12) #Sand
            self.y -= 1
            time.sleep(0.05)
   
    def garvelPyramidHole(self):#Mob pit
        mc.setBlocks(self.x2 + 1, self.y2, self.z2 + 1,
                     self.x2 - 1 , self.y2 - 5, self.z2 - 1 , 0) #Pit
