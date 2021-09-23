﻿import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

viz.move([0,0,-8])

#import 3D model
piazza = viz.addChild('piazza.osgb')

#build male avatar
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])

#build female avatar
female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0])

#Set the male and female to the talking state
male.state(14)
female.state(14)

import random

pigeons = []
for i in range(10):

    #Generate random values for position and orientation
    x = random.randint(-4,3)
    z = random.randint(4,8)
    yaw = random.randint(0,360)

    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')

    #Set position, orientation, and state
    pigeon.setPosition([x,0,z])
    pigeon.setEuler([yaw,0,0])
    pigeon.state(1)

    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon)

#press w key to make avatars move
def walkAvatars():
    walk1 = vizact.walkTo([4.5, 0,-40])
    vizact.ontimer2(0.5,0,female.addAction,walk1)

    walk2 = vizact.walkTo([3.5,0,-40])
    male.addAction(walk2)

vizact.onkeydown('w',walkAvatars)

def pigeonsFeed():

    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)

vizact.onkeydown('p',pigeonsFeed)

#plants = []
#for x in [-3, -1, 1, 3]:
	#for z in [4, 2, 0, -2, -4]:
		#plant = viz.addChild('plant.osgb',cache=viz.CACHE_CLONE)
		#plant.setPosition([x,0,z])
		#plants.append(plant)
		
#import vizact
#spin = vizact.spin(0,1,0,15)

#plants start spinning at different times
#def spinPlant(plant):
    #plant.addAction(spin)
#vizact.ontimer2(0.5,19,spinPlant,vizact.choice(plants))

#make all plants spin
#for plant in plants:
	#plant.addAction(spin)
		
#display model of the coordinate axis 
#import vizshape
#vizshape.addAxes()

#add plant next to right lamp post 
#plant = viz.addChild('plant.osgb')
#plant.setPosition([4,0,6])

#move viewpoint relative to current position
#viz.MainView.move([3,0,-7])

#place viepooint in world coordinates
#viz.MainView.setPosition([0,15,-15])

#change viewpoint orientation
#viz.MainView.setEuler([0,30,0])