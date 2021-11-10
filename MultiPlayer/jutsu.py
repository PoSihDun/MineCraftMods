'''There is 3 different scripts. script #1 calls the functions of script2/3
so when using these scripts run scripts #1- This is script2.'''

'''Script #2 save as jutsu'''
from mcpi.minecraft import Minecraft

mc = Minecraft.create(address="#.#.#.#", port=4711)

import time

def amenotejikara(player): #Teleporting with arrow shots
    for blockhit in mc.entity.pollProjectileHits(player):
        pos = blockhit.pos
        teleport = mc.entity.setPos(player,pos.x, pos.y, pos.z)
       

def fireAShot(player): #Fire arrows
    for blockhit in mc.entity.pollProjectileHits(player):
        pos = blockhit.pos
        fireB = 51 #Fire block
        fireblock = mc.setBlocks(pos.x, pos.y, pos.z,
                                pos.x, pos.y, pos.z,
                                fireB)
       
   
def allMightyPush(player): #Arrow that creates blocks of air
    for blockhit in mc.entity.pollProjectileHits(player):
        clearBlock = 0 #Air block
        pos = blockhit.pos
        space = mc.setBlocks(pos.x + 4, pos.y + 2, pos.z + 4,
                            pos.x - 4, pos.y - 2, pos.z - 4,
                            clearBlock)
       
                     
def stillWater(player): #Turning blocks into still water with sword blocks.
    for blockhit in mc.entity.pollBlockHits(player):
        waterBlock = 9 #Still Water block
        pos = blockhit.pos
        waterPool = mc.setBlock(pos.x, pos.y, pos.z,
                                waterBlock)
       
                   
def lavaFlow(player): #Turning blocks into still lava with sword blocks.
    for blockhit in mc.entity.pollBlockHits(player):
        flowingLava = 11 #Still Lava block    
        pos = blockhit.pos
        lavaBurst = mc.setBlock(pos.x, pos.y, pos.z,
                                flowingLava)
       
       
def portalDoor(player): #Creates a 1*3 door for nether portal
    for blockhit in mc.entity.pollBlockHits(player):
        netherPortal = 90 #Nether Portal block
        pos = blockhit.pos
        opening = mc.setBlocks(pos.x, pos.y+2, pos.z,
                               pos.x, pos.y, pos.z,
                               netherPortal)
       

def oakPlank(player): #Truns blocks into wood
    for blockhit in mc.entity.pollBlockHits(player):
        oakWood =17 #Wood block
        pos = blockhit.pos
        woodBlock = mc.setBlocks(pos.x, pos.y, pos.z,
                                pos.x, pos.y, pos.z,
                                 oakWood)
       

def darkMatter(player):#Turns block into obsidian stone
    for blockhit in mc.entity.pollBlockHits(player):
        darkM =49 # Obsidian block
        pos = blockhit.pos
        materia = mc.setBlocks(pos.x, pos.y, pos.z,
                               pos.x, pos.y, pos.z,
                                 darkM)
