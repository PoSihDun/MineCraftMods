from math import e
import threading
import time

from mcpi.minecraft import Minecraft
from mcpi import entity


mc = Minecraft.create(address="#.#.#.#", port=4711)

players_ids = mc.getPlayerEntityIds()
print(len(players_ids), " entities available.")
number = len(players_ids)
mc.postToChat(  "%s entities available." %number)

for id in players_ids:
    mc.postToChat("Entity : %s" %id)


def playerEntity1(player):
    #from mcLogListener import on_press
    import time
    from classSummon import ArrowTrap, DiamondTrap, EnderWarrior, FallingSky
    from jutsu import amenotejikara, allMightyPush, stillWater, lavaFlow, portalDoor, oakPlank, darkMatter, fireAShot
    from mcpi.minecraft import Minecraft

    #mc = Minecraft.create(address="50.65.208.115", port=8990, name="S0frosty")
    mc = Minecraft.create(address="192.168.0.142", port=4711)

    chatPost = "0"
    while True:
        
        for chatPost in mc.entity.pollChatPosts(players_ids[0]):
            if chatPost.message.lower() == "6":
                mc.postToChat("Amenotejikara is activated")
                chatPost = "6"
            elif chatPost.message.lower() == "7":
                mc.postToChat("All Mighty Push is activated")
                chatPost = "7"
            elif chatPost.message.lower() == "1":
                mc.postToChat("Water Pool jutsu!")
                chatPost = "1"
            elif chatPost.message.lower() == "2":
                mc.postToChat("Flowing Lava Jutsu!")
                chatPost = "2"
            elif chatPost.message.lower() == "3":
                mc.postToChat("Portal Summoning Jutsu")
                chatPost = "3"
            elif chatPost.message.lower() == "4":
                mc.postToChat("Oak Wood Jutsu")
                chatPost = "4"
            elif chatPost.message.lower() == "5":
                mc.postToChat("Obsidian Forbidin Jutsu")
                chatPost = "5"
            elif chatPost.message.lower() == '8':
                mc.postToChat("Fireball Jutsu")
                chatPost = "8"
            elif chatPost.message.lower() == '11':
                mc.postToChat("Arrow Glass Prism Jutsu")
                chatPost = "11"
            elif chatPost.message.lower() == '12':
                mc.postToChat("Diamond Prism Jutsu")
                chatPost = "12"
            elif chatPost.message.lower() == '13':
                mc.postToChat("Ender Tools Jutsu")
                chatPost = "13"
            elif chatPost.message.lower() == '14':
                mc.postToChat("Mighty Sand Trap")
                chatPost = "14"
            elif chatPost.message.lower() == '0':
                mc.postToChat("test")
                chatPost = "0"

                '''Listener for arrow shots'''   
            
        for blockhit in mc.entity.pollProjectileHits(players_ids[0]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "6":
                amenotejikara(players_ids[0])#Teleporting Arrow 
            elif chatPost == "7":
                allMightyPush(players_ids[0])#Air Arrow
            elif chatPost == "8":
                fireAShot(players_ids[0])#Fire Arrow
            elif chatPost == "11":
                trapArrow = ArrowTrap(x, y, z, 3)#Trap arrow class
                trapArrow.build()#Pyramid1
                trapArrow.bottom()#Pyramid2
            elif chatPost == "14":
                fArrow = FallingSky(x, y, z, 1)#FallingSky class
                fArrow.garvelPyramidHole()#Mob pit
                fArrow.garvelPyramidTop()#Falling sand
                fArrow.garvelPyramid()#falling sand
                fArrow.garvelPyramidBottom()#falling sand
            else:
                mc.events.clearAll()

                '''Sword block Listener'''
        for blockhit in mc.entity.pollBlockHits(players_ids[0]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "1":
                stillWater(players_ids[0])#Water block sword block
            elif chatPost == "2":
                lavaFlow(players_ids[0])#Lava block sword block
            elif chatPost == "3":
                portalDoor(players_ids[0])# 1*3 nether portal block
            elif chatPost == "4":
                oakPlank(players_ids[0])#Wood block sword block
                
            elif chatPost == "5":
                darkMatter(players_ids[0])#Obsidian block sword block
            elif chatPost == "12":
                glassDiamond = DiamondTrap(x,y,z,3) #DiamondTrap class
                glassDiamond.buildB()
            elif chatPost == "13":
                endLoot = EnderWarrior(x, y, z, 2)#EnderWarrior class
                endLoot.enderOre()
                endLoot.enderPumpkin()
                endLoot.crafting()

def playerEntity2(player):
    #from mcLogListener import on_press
    import time
    from classSummon import ArrowTrap, DiamondTrap, EnderWarrior, FallingSky
    from jutsu import amenotejikara, allMightyPush, stillWater, lavaFlow, portalDoor, oakPlank, darkMatter, fireAShot
    from mcpi.minecraft import Minecraft

    #mc = Minecraft.create(address="50.65.208.115", port=8990, name="S0frosty")
    mc = Minecraft.create(address="192.168.0.142", port=4711)

    chatPost = "0"
    while True:
        
        for chatPost in mc.entity.pollChatPosts(players_ids[1]):
            if chatPost.message.lower() == "6":
                mc.postToChat("Amenotejikara is activated")
                chatPost = "6"
            elif chatPost.message.lower() == "7":
                mc.postToChat("All Mighty Push is activated")
                chatPost = "7"
            elif chatPost.message.lower() == "1":
                mc.postToChat("Water Pool jutsu!")
                chatPost = "1"
            elif chatPost.message.lower() == "2":
                mc.postToChat("Flowing Lava Jutsu!")
                chatPost = "2"
            elif chatPost.message.lower() == "3":
                mc.postToChat("Portal Summoning Jutsu")
                chatPost = "3"
            elif chatPost.message.lower() == "4":
                mc.postToChat("Oak Wood Jutsu")
                chatPost = "4"
            elif chatPost.message.lower() == "5":
                mc.postToChat("Obsidian Forbidin Jutsu")
                chatPost = "5"
            elif chatPost.message.lower() == '8':
                mc.postToChat("Fireball Jutsu")
                chatPost = "8"
            elif chatPost.message.lower() == '11':
                mc.postToChat("Arrow Glass Prism Jutsu")
                chatPost = "11"
            elif chatPost.message.lower() == '12':
                mc.postToChat("Diamond Prism Jutsu")
                chatPost = "12"
            elif chatPost.message.lower() == '13':
                mc.postToChat("Ender Tools Jutsu")
                chatPost = "13"
            elif chatPost.message.lower() == '14':
                mc.postToChat("Mighty Sand Trap")
                chatPost = "14"
            elif chatPost.message.lower() == '0':
                mc.postToChat("test")
                chatPost = "0"

                '''Listener for arrow shots'''   
            
        for blockhit in mc.entity.pollProjectileHits(players_ids[1]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "6":
                amenotejikara(players_ids[1])#Teleporting Arrow 
            elif chatPost == "7":
                allMightyPush(players_ids[1])#Air Arrow
            elif chatPost == "8":
                fireAShot(players_ids[1])#Fire Arrow
            elif chatPost == "11":
                trapArrow = ArrowTrap(x, y, z, 3)#Trap arrow class
                trapArrow.build()#Pyramid1
                trapArrow.bottom()#Pyramid2
            elif chatPost == "14":
                fArrow = FallingSky(x, y, z, 1)#FallingSky class
                fArrow.garvelPyramidHole()#Mob pit
                fArrow.garvelPyramidTop()#Falling sand
                fArrow.garvelPyramid()#falling sand
                fArrow.garvelPyramidBottom()#falling sand
            else:
                mc.events.clearAll()

                '''Sword block Listener'''
        for blockhit in mc.entity.pollBlockHits(players_ids[1]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "1":
                stillWater(players_ids[1])#Water block sword block
            elif chatPost == "2":
                lavaFlow(players_ids[1])#Lava block sword block
            elif chatPost == "3":
                portalDoor(players_ids[1])# 1*3 nether portal block
            elif chatPost == "4":
                oakPlank(players_ids[1])#Wood block sword block
                
            elif chatPost == "5":
                darkMatter(players_ids[1])#Obsidian block sword block
            elif chatPost == "12":
                glassDiamond = DiamondTrap(x,y,z,3) #DiamondTrap class
                glassDiamond.buildB()
            elif chatPost == "13":
                endLoot = EnderWarrior(x, y, z, 2)#EnderWarrior class
                endLoot.enderOre()
                endLoot.enderPumpkin()
                endLoot.crafting()
    
def playerEntity3(player):
    #from mcLogListener import on_press
    import time
    from classSummon import ArrowTrap, DiamondTrap, EnderWarrior, FallingSky
    from jutsu import amenotejikara, allMightyPush, stillWater, lavaFlow, portalDoor, oakPlank, darkMatter, fireAShot
    from mcpi.minecraft import Minecraft

    #mc = Minecraft.create(address="50.65.208.115", port=8990, name="S0frosty")
    mc = Minecraft.create(address="192.168.0.142", port=4711)

    chatPost = "0"
    while True:
        
        for chatPost in mc.entity.pollChatPosts(players_ids[2]):
            if chatPost.message.lower() == "6":
                mc.postToChat("Amenotejikara is activated")
                chatPost = "6"
            elif chatPost.message.lower() == "7":
                mc.postToChat("All Mighty Push is activated")
                chatPost = "7"
            elif chatPost.message.lower() == "1":
                mc.postToChat("Water Pool jutsu!")
                chatPost = "1"
            elif chatPost.message.lower() == "2":
                mc.postToChat("Flowing Lava Jutsu!")
                chatPost = "2"
            elif chatPost.message.lower() == "3":
                mc.postToChat("Portal Summoning Jutsu")
                chatPost = "3"
            elif chatPost.message.lower() == "4":
                mc.postToChat("Oak Wood Jutsu")
                chatPost = "4"
            elif chatPost.message.lower() == "5":
                mc.postToChat("Obsidian Forbidin Jutsu")
                chatPost = "5"
            elif chatPost.message.lower() == '8':
                mc.postToChat("Fireball Jutsu")
                chatPost = "8"
            elif chatPost.message.lower() == '11':
                mc.postToChat("Arrow Glass Prism Jutsu")
                chatPost = "11"
            elif chatPost.message.lower() == '12':
                mc.postToChat("Diamond Prism Jutsu")
                chatPost = "12"
            elif chatPost.message.lower() == '13':
                mc.postToChat("Ender Tools Jutsu")
                chatPost = "13"
            elif chatPost.message.lower() == '14':
                mc.postToChat("Mighty Sand Trap")
                chatPost = "14"
            elif chatPost.message.lower() == '0':
                mc.postToChat("test")
                chatPost = "0"

                '''Listener for arrow shots'''   
            
        for blockhit in mc.entity.pollProjectileHits(players_ids[2]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "6":
                amenotejikara(players_ids[2])#Teleporting Arrow 
            elif chatPost == "7":
                allMightyPush(players_ids[2])#Air Arrow
            elif chatPost == "8":
                fireAShot(players_ids[2])#Fire Arrow
            elif chatPost == "11":
                trapArrow = ArrowTrap(x, y, z, 3)#Trap arrow class
                trapArrow.build()#Pyramid1
                trapArrow.bottom()#Pyramid2
            elif chatPost == "14":
                fArrow = FallingSky(x, y, z, 1)#FallingSky class
                fArrow.garvelPyramidHole()#Mob pit
                fArrow.garvelPyramidTop()#Falling sand
                fArrow.garvelPyramid()#falling sand
                fArrow.garvelPyramidBottom()#falling sand
            else:
                mc.events.clearAll()

                '''Sword block Listener'''
        for blockhit in mc.entity.pollBlockHits(players_ids[2]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "1":
                stillWater(players_ids[2])#Water block sword block
            elif chatPost == "2":
                lavaFlow(players_ids[2])#Lava block sword block
            elif chatPost == "3":
                portalDoor(players_ids[2])# 1*3 nether portal block
            elif chatPost == "4":
                oakPlank(players_ids[2])#Wood block sword block
            elif chatPost == "5":
                darkMatter(players_ids[2])#Obsidian block sword block
            elif chatPost == "12":
                glassDiamond = DiamondTrap(x,y,z,3) #DiamondTrap class
                glassDiamond.buildB()
            elif chatPost == "13":
                endLoot = EnderWarrior(x, y, z, 2)#EnderWarrior class
                endLoot.enderOre()
                endLoot.enderPumpkin()
                endLoot.crafting()

def playerEntity4(player):
    #from mcLogListener import on_press
    import time
    from classSummon import ArrowTrap, DiamondTrap, EnderWarrior, FallingSky
    from jutsu import amenotejikara, allMightyPush, stillWater, lavaFlow, portalDoor, oakPlank, darkMatter, fireAShot
    from mcpi.minecraft import Minecraft

    #mc = Minecraft.create(address="50.65.208.115", port=8990, name="S0frosty")
    mc = Minecraft.create(address="192.168.0.142", port=4711)

    chatPost = "0"
    while True:
        
        for chatPost in mc.entity.pollChatPosts(players_ids[3]):
            if chatPost.message.lower() == "6":
                mc.postToChat("Amenotejikara is activated")
                chatPost = "6"
            elif chatPost.message.lower() == "7":
                mc.postToChat("All Mighty Push is activated")
                chatPost = "7"
            elif chatPost.message.lower() == "1":
                mc.postToChat("Water Pool jutsu!")
                chatPost = "1"
            elif chatPost.message.lower() == "2":
                mc.postToChat("Flowing Lava Jutsu!")
                chatPost = "2"
            elif chatPost.message.lower() == "3":
                mc.postToChat("Portal Summoning Jutsu")
                chatPost = "3"
            elif chatPost.message.lower() == "4":
                mc.postToChat("Oak Wood Jutsu")
                chatPost = "4"
            elif chatPost.message.lower() == "5":
                mc.postToChat("Obsidian Forbidin Jutsu")
                chatPost = "5"
            elif chatPost.message.lower() == '8':
                mc.postToChat("Fireball Jutsu")
                chatPost = "8"
            elif chatPost.message.lower() == '11':
                mc.postToChat("Arrow Glass Prism Jutsu")
                chatPost = "11"
            elif chatPost.message.lower() == '12':
                mc.postToChat("Diamond Prism Jutsu")
                chatPost = "12"
            elif chatPost.message.lower() == '13':
                mc.postToChat("Ender Tools Jutsu")
                chatPost = "13"
            elif chatPost.message.lower() == '14':
                mc.postToChat("Mighty Sand Trap")
                chatPost = "14"
            elif chatPost.message.lower() == '0':
                mc.postToChat("test")
                chatPost = "0"

                '''Listener for arrow shots'''   
            
        for blockhit in mc.entity.pollProjectileHits(players_ids[3]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "6":
                amenotejikara(players_ids[3])#Teleporting Arrow 
            elif chatPost == "7":
                allMightyPush(players_ids[3])#Air Arrow
            elif chatPost == "8":
                fireAShot(players_ids[3])#Fire Arrow
            elif chatPost == "11":
                trapArrow = ArrowTrap(x, y, z, 3)#Trap arrow class
                trapArrow.build()#Pyramid1
                trapArrow.bottom()#Pyramid2
            elif chatPost == "14":
                fArrow = FallingSky(x, y, z, 1)#FallingSky class
                fArrow.garvelPyramidHole()#Mob pit
                fArrow.garvelPyramidTop()#Falling sand
                fArrow.garvelPyramid()#falling sand
                fArrow.garvelPyramidBottom()#falling sand
            else:
                mc.events.clearAll()

                '''Sword block Listener'''
        for blockhit in mc.entity.pollBlockHits(players_ids[3]):
            pos = blockhit.pos
            x = pos.x
            y = pos.y
            z = pos.z
            
            if chatPost == "1":
                stillWater(players_ids[3])#Water block sword block
            elif chatPost == "2":
                lavaFlow(players_ids[3])#Lava block sword block
            elif chatPost == "3":
                portalDoor(players_ids[3])# 1*3 nether portal block
            elif chatPost == "4":
                oakPlank(players_ids[3])#Wood block sword block
                
            elif chatPost == "5":
                darkMatter(players_ids[3])#Obsidian block sword block
            elif chatPost == "12":
                glassDiamond = DiamondTrap(x,y,z,3) #DiamondTrap class
                glassDiamond.buildB()
            elif chatPost == "13":
                endLoot = EnderWarrior(x, y, z, 2)#EnderWarrior class
                endLoot.enderOre()
                endLoot.enderPumpkin()
                endLoot.crafting()


if number == 1:
    thread1 = threading.Thread(target=playerEntity1, args=(players_ids[0],))
    thread1.start()
elif number == 2:
    thread1 = threading.Thread(target=playerEntity1, args=(players_ids[0],))
    thread2 = threading.Thread(target=playerEntity2, args=(players_ids[1],))
    thread1.start()
    thread2.start()
elif number == 3:
    thread1 = threading.Thread(target=playerEntity1, args=(players_ids[0],))
    thread2 = threading.Thread(target=playerEntity2, args=(players_ids[1],))
    thread3 = threading.Thread(target=playerEntity3, args=(players_ids[2],))
    thread1.start()
    thread2.start()
    thread3.start()
elif number == 4:
    thread1 = threading.Thread(target=playerEntity1, args=(players_ids[0],))
    thread2 = threading.Thread(target=playerEntity2, args=(players_ids[1],))
    thread3 = threading.Thread(target=playerEntity3, args=(players_ids[2],))
    thread4 = threading.Thread(target=playerEntity4, args=(players_ids[3],))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
