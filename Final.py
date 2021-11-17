﻿import viz 
import vizshape
import atexit
import vizinfo
import viztask
import vizact
import vizcam


viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

chemLab = viz.addChild('chemlab50M.xyz.osgb')
chemLab.disable(viz.LIGHTING)
chemLab.setEuler(20,0,0)

view = viz.MainView
view.setPosition([-0.5,4.4,-3.5])
view.setEuler([-90,0,0])

#Defines boolean variables
#Equipment section
visitedFumeHood = False
visitedEyeWash = False
visitedNozzles = False
visitedShower = False
visitedFireExtinguisher = False
visitedBench = False
visitedSinks = False
visitedTaps = False
visitedFloor = False
visitedWaste = False
visitedToProcedure = False

#back = vizshape.addPlane(size=(15,3), axis=vizshape.AXIS_X, cullFace=True)
#back.setPosition(-6,4,-4)
#left = vizshape.addPlane(size=(20,3), axis=vizshape.AXIS_Z, cullFace=True)
#left.setPosition(0,4,)


#Sets up screen 
screen = vizshape.addPlane(size=(1.2,1.2), axis=vizshape.AXIS_X, cullFace=True)
screen.setEuler(0,0,0)
screen.setPosition(-5.12,4.49,-4.25)
screen.disable(viz.LIGHTING)
screen.visible(viz.ON)
screen.texture(viz.addTexture("Slides/Intro.jpg"))

#creates equipment orbs
fume = viz.addChild('white_ball.wrl')
eye_wash = viz.addChild('white_ball.wrl')
nozzles = viz.addChild('white_ball.wrl')
shower = viz.addChild('white_ball.wrl')
fire_ext = viz.addChild('white_ball.wrl')
bench = viz.addChild('white_ball.wrl')
sinks = viz.addChild('white_ball.wrl')
taps = viz.addChild('white_ball.wrl')
floor = viz.addChild('white_ball.wrl')
waste = viz.addChild('white_ball.wrl')
toProcedure = viz.addChild('white_ball.wrl')
		

#Sets orbs to red
fume.color( viz.RED )
eye_wash.color( viz.RED )
nozzles.color( viz.RED )
shower.color( viz.RED )
fire_ext.color( viz.RED )
bench.color( viz.RED )
sinks.color( viz.RED )
taps.color( viz.RED )
floor.color( viz.RED )
waste.color( viz.RED )
toProcedure.color( viz.RED )
toProcedure.visible(viz.OFF)
		

#positions orbs
fume.setPosition([-3.5,5,.85])
eye_wash.setPosition([-2.5,4,-8.3])
nozzles.setPosition([-1.2,4,-7.5])
shower.setPosition([2,5,-11])
fire_ext.setPosition([-4.2,4.1,-9.8])
bench.setPosition([-0.5,3.9,-7.5])
sinks.setPosition([-2.7,4.1,-4.8])
taps.setPosition([-0.5,3.9,-7.5])
floor.setPosition([-0.5,3.9,-7.5])
waste.setPosition([-0.5,3.9,-7.5])
toProcedure.setPosition([-5,5,-5])

def safetyTutorial():
	if visitedToProcedure == True:
		proceduresTutorial()
	else:
		equipmentTutorial()

def equipmentTutorial():
	global visitedFumeHood
	global visitedEyeWash 
	global visitedNozzles 
	global visitedShower 
	global visitedFireExtinguisher
	global visitedBench	
	global visitedSinks
	global visitedTaps
	global visitedFloor
	global visitedWaste
	global visitedToProcedure
	object = viz.pick()
	if object == fume: 
		screen.texture(viz.addTexture("Slides/Fume_Hood.jpg"))
		visitedFumeHood = True
		fume.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == eye_wash:
		screen.texture(viz.addTexture("Slides/Eye_Wash.jpg"))
		visitedEyeWash = True
		eye_wash.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == nozzles:
		screen.texture(viz.addTexture("Slides/Nozzles.jpg"))
		visitedNozzles = True
		nozzles.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == shower:
		screen.texture(viz.addTexture("Slides/Shower.jpg"))
		visitedShower = True
		shower.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == fire_ext:
		visitedFireExtinguisher = True 
		screen.texture(viz.addTexture("Slides/Fire_Extinguisher.jpg"))
		fire_ext.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == bench:
		visitedBench = True 
		viz.window.displayHTML( 'www.google.com' )
		vizact.onkeydown(' ', viz.window.hideHTML )
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		bench.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == sinks:
		visitedSinks = True 
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		sinks.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == taps:
		visitedTaps = True 
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		taps.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == floor:
		visitedFloor = True 
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		floor.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == waste:
		visitedWaste = True 
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		waste.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == toProcedure: 
		visitedToProcedure = True
		screen.texture(viz.addTexture("Slides/Intro.jpg"))
		toProcedure.color( viz.GREEN )
		view.setEuler([-90,0,0])
		vizact.onmousedown(viz.MOUSEBUTTON_LEFT,proceduresTutorial)
		proceduresTutorial()
	if visitedFumeHood == True and visitedEyeWash == True and visitedNozzles == True and visitedShower == True and visitedFireExtinguisher == True and visitedBench == True:
		toProcedure.visible(viz.ON)
		
		
		
def proceduresTutorial():
	#disables equipment orbs
	fume.visible(viz.OFF)
	eye_wash.visible(viz.OFF)
	shower.visible(viz.OFF)
	nozzles.visible(viz.OFF)
	fire_ext.visible(viz.OFF)
	bench.visible(viz.OFF)
	toProcedure.visible(viz.OFF)
	object = viz.pick()
	if object == fume: 
		screen.texture(viz.addTexture("Slides/Eye_Wash.jpg"))
		visitedFumeHood = True
		fume.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == eye_wash:
		screen.texture(viz.addTexture("Slides/Fume_Hood.jpg"))
		visitedEyeWash = True
		eye_wash.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == nozzles:
		screen.texture(viz.addTexture("Slides/Shower.jpg"))
		visitedNozzles = True
		nozzles.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == shower:
		screen.texture(viz.addTexture("Slides/Nozzles.jpg"))
		visitedShower = True
		shower.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == fire_ext:
		visitedFireExtinguisher = True 
		screen.texture(viz.addTexture("Slides/Fire_Extinguisher.jpg"))
		fire_ext.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
	elif object == bench:
		visitedBench = True 
		viz.window.displayHTML( 'www.google.com' )
		vizact.onkeydown(' ', viz.window.hideHTML )
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		bench.color( viz.GREEN )
		view.setPosition([-0.5,4.4,-3.5])
		view.setEuler([-90,0,0])
		
def tourOutput():
	print('Equipment Checklist:')
	print('FUME HOOD: ', visitedFumeHood)
	print('EYE WASH STATION: ', visitedEyeWash)
	print('OUTLETS & NOZZLES: ', visitedNozzles)
	print('SAFETY SHOWER: ', visitedShower)
	print('FIRE EXTINGUISHER: ', visitedFireExtinguisher)
	print('LAB BENCH: ', visitedBench)
	print('PROCEDURE SECTION: ', visitedToProcedure)
	
#def onMouseDown(button):
#    if button == viz.MOUSEBUTTON_LEFT:
#        print('you hit the left mouse button')
#viz.callback(viz.MOUSEDOWN_EVENT,onMouseDown)


vizact.onmousedown(viz.MOUSEBUTTON_LEFT,safetyTutorial)

atexit.register(tourOutput)