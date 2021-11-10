# MineCraftMods
Making modes with python. Using mcpi and raspberryjuice api/pluggin
Objectives

This is a quick description on how to set up the spigot server to run a python API in Minecraft.

I had to learn recursion and I had to learn python. On the course of my journey I happened to find a book called “Learn to Program with Minecraft”, which happens to go teach Python and go in-depth on multiple data structures and algorithms, including recursion. This tutorial will teach you how to mod Minecraft using python. It will demonstrate a basic set up, using a linux machine for the server which can run the Minecraft api from any machine. In this tutorial you will learn the basic setup, you can download some of the mods I created on my page. If you want to learn more I recommend purchasing “Learn to Program with Minecraft-By Craig Richardson”, check out his web site “https://www.stuffaboutcode.com/”, or the RaspberryJuice repo “https://github.com/zhuowei/RaspberryJuice” for more in depth documentations. 

Before we go any further we will need to download the following;

1)Minecraft
-You can buy a copy from here “https://minecraft.net/download”

2)Python3
-You can install Python3 from here “https://www.python.org”

3)Java Development Kit
-A Java Development Kit(JDK) is required to set up our spigot server.
You can download it from here from the  “https://www.oracle.com/java/technologies/javase-jre8-downloads.html”
-Or use the command “sudo apt-get install git openjdk-8-jre-headless”(This command gets both git and Java) 

4)Minecraft Python API – MCPI
-https://github.com/martinohanlon/mcpi.git 
This API should be downloaded into your python3 Lib folder.

5)Spigot Minecraft Server/BuildTools
-Make a folder and make sure its easy to access. The next steps you will need to download everything into this folder. Below covers how to download via command line.
a) curl -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar  
or 
b) wget -O BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar 
Run BuildTools.jar from the terminal (Do not double-click BuildTools.jar) by doing the following:
    1. On linux run git config --global --unset core.autocrlf, then run java -jar BuildTools.jar in bash or another appropriate shell.

Running spigot
1) Create a startup script called “start.sh” by typing the command in the console(This should all be done in the folder you created and downloaded everything into)

nano start.sh

Now use type in these lines of code changes.

#!/bin/sh

java -Xms#G -Xmx#G -XX:+UseG1GC -jar spigot.jar nogui 

save the file by pressing ctrl+x and then press “y” to confirm and save.

-# is your allocated memory for the server. For example this is my script on my server java -Xms1G -Xmx4G -XX:+UseG1GC -jar spigot-1.16.4.jar nogui

2)In the following terminal run this command after the file was created 
chmod +x start.sh 

3)To start the server run this script
./start.sh 

Post-Installation
After the spigot.jar has been run the first time, the following should be created, and eula.txt needs to be edited for everything to work properly.
-server.properties
-bukkit.yml
-spigot.yml
-server icons

nano into eula.txt and change false to true and run ./start.sh again. A minute or so the server should be up and running and you can connect to the multiplayer server.

Server Address will be your servers IP and port.
10.0.0.1:25565
port:25565 is default and can be changed in the properties.server file.


Follow my tutorial on how to get spigot booted and rooted. Once that is done you can run this script. There is two other scripts required in order to make this one work. You can download both from here.

Once the script is running, go into Minecraft and type the corresponding # into the chat to activate the mod.
1 :Water Pool jutsu!
2 :Flowing Lava Jutsu!
3 :Portal Summoning Jutsu
4 :Oak Wood Jutsu
5 :Obsidian Forbidin Jutsu
6 :Amenotejikara 
7 :All Mighty Push
8 :Fireball Jutsu
11 :Arrow Glass Prism Jutsu
12 :Diamond Prism Jutsu
13 :Ender Tools Jutsu
14 :Mighty Sand Trap
