﻿import viz 
import vizshape
import atexit
import vizinfo
import viztask
import vizact
import vizcam
import vizconnect
import vizproximity

def IsThisVillanovaCAVE():
	cave_host_names = ["exx-PC","render-PC"]
	import socket
	if socket.gethostname() in cave_host_names:
		return True
	else:
		return False

if IsThisVillanovaCAVE():
	#CAVE and FLYSTICK set-up
	CONFIG_FILE = "E:\\VizardProjects\\_CaveConfigFiles\\vizconnect_config_CaveFloor+ART_headnode.py"
	vizconnect.go(CONFIG_FILE)
	cave_view_matrix = [ -0.260936, 0.000000, 0.965356, 0.000000,
	0.000000, 1.000000, -0.000000, 0.000000,
	-0.965356, -0.000000, -0.260936, 0.000000,
	-0.731557, 2.822117, -4.915627, 1.000000 ]
	vizconnect.getTransport('wandmagiccarpet').getNode3d().setMatrix(cave_view_matrix)
	viz.fov(60)
	viz.clearcolor(viz.GRAY)
else:
    viz.go()



#Increase the Field of View
viz.MainWindow.fov(60)

chemLab = viz.addChild('chemlab 50M.xyz.osgb')
chemLab.disable(viz.LIGHTING)
chemLab.setEuler(20,0,0)

view = viz.MainView
view.setPosition([-0.5,4.4,-3.5])
view.setEuler([-90,0,0])

#Defines boolean variables
toWhatToWear = False

#What to Wear section
visitedToEquipment = False

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

hitFumeHood = False
hitEyeWash = False
hitNozzles = False
hitShower = False
hitFireExtinguisher = False
hitBench = False	
hitSinks = False
hitTaps = False
hitFloor = False
hitWaste = False


checkpoint = 0
whatToWearSlideCount = 0
videoCount = 0
playNow = True

#back = vizshape.addPlane(size=(15,3), axis=vizshape.AXIS_X, cullFace=True)
#back.setPosition(-6,4,-4)
#left = vizshape.addPlane(size=(20,3), axis=vizshape.AXIS_Z, cullFace=True)
#left.setPosition(0,4,)


#Sets up screen 
screen = vizshape.addPlane(size=(1.2,1.2), axis=vizshape.AXIS_X, cullFace=True)
screen.setEuler(0,0,0)
screen.setPosition(-5.12,4.49,-4.27)
screen.disable(viz.LIGHTING)
screen.visible(viz.ON)
screen.texture(viz.addTexture("Slides/Intro.jpg"))

#sets up "Next" box
next = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
next.setEuler(0,0,0)
next.setPosition(-5.08,4.49,-3.45)
next.disable(viz.LIGHTING)
next.visible(viz.ON)
next.texture(viz.addTexture("Slides/Next.jpg"))

#sets up "Back" box
back = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
back.setEuler(0,0,0)
back.setPosition(-5.08,4.49,-5.06)
back.disable(viz.LIGHTING)
back.visible(viz.ON)
back.texture(viz.addTexture("Slides/Back.jpg"))
back.visible(viz.OFF)

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

#turns orbs invisible
fume.visible(viz.OFF)
eye_wash.visible(viz.OFF)
shower.visible(viz.OFF)
nozzles.visible(viz.OFF)
fire_ext.visible(viz.OFF)
bench.visible(viz.OFF)
sinks.visible(viz.OFF)
taps.visible(viz.OFF)
floor.visible(viz.OFF)
waste.visible(viz.OFF)
toProcedure.visible(viz.OFF)		

#positions orbs
fume.setPosition([-3.5,5,.85])
eye_wash.setPosition([-2.5,4,-8.3])
nozzles.setPosition([-1.2,4,-7.5])
shower.setPosition([2,5,-11])
fire_ext.setPosition([-4.2,4.1,-9.8])
bench.setPosition([1,3.9,-7.5])
sinks.setPosition([-3,4.1,-4.8])
taps.setPosition([-3,4,-1])
floor.setPosition([-4.3,3.2,-2.])
waste.setPosition([-4.5,3.6,-4])
toProcedure.setPosition([-5,5,-5])

#create equipment proximity sensors
fumeSensor = vizproximity.Sensor(vizproximity.Box([1.5,4,1.5],center=[0,0,0]), source= fume)
eyeWashSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=eye_wash)
nozzlesSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=nozzles)
showerSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=shower)
fireExtinguisherSensor = vizproximity.Sensor(vizproximity.Box([2,4,1],center=[.5,0,.2]), source=fire_ext)
benchSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=bench)
sinksSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=sinks)
tapsSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=taps)
floorSensor = vizproximity.Sensor(vizproximity.Box([1,4,1],center=[0,0,0]), source=floor)
wasteSensor = vizproximity.Sensor(vizproximity.Box([1.5,4,1.5],center=[0,0,0]), source=waste)
			
#set target as MainView
#TRY TO SET TARGET TO FLYSTICK HAND			
target = vizproximity.Target(viz.MainView)

manager = vizproximity.Manager()
manager.addSensor(fumeSensor)
manager.addSensor(eyeWashSensor)
manager.addSensor(nozzlesSensor)
manager.addSensor(showerSensor)
manager.addSensor(fireExtinguisherSensor)
manager.addSensor(benchSensor)
manager.addSensor(sinksSensor)
manager.addSensor(tapsSensor)
manager.addSensor(floorSensor)
manager.addSensor(wasteSensor)
manager.addTarget(target)

#make proximity sensor boxes visible
manager.setDebug(viz.ON)

		
def introduction():
	global checkpoint
	global toWhatToWear
	if checkpoint == 0:
		print('running introduction')
		checkpoint += 1
	if trigger:
		print("pressing")
	if left:
		print("left")
	if right:
		print("right")
		
	#object = viz.pick()
	#if object == next:
	if right:
		screen.texture(viz.addTexture("Slides/WhatToWear/WhatToWear.jpg"))
		toWhatToWear = True
		back.visible(viz.ON)
	
def whatToWear():
	global visitedToEquipment
	print('running what to wear')
	global whatToWearSlideCount
	#disables equipment orbs
	whatToWearSlideshow = ['Slides/WhatToWear/WhatToWear.jpg', 'Slides/WhatToWear/Footwear.jpg','Slides/WhatToWear/Pants.jpg', 'Slides/WhatToWear/Shirts.jpg','Slides/WhatToWear/Hair.jpg','Slides/WhatToWear/Eyes.jpg','Slides/WhatToWear/SafetyGear.jpg','Slides/WhatToWear/WhatToWearExit.jpg']
	object = viz.pick()
	#if object == next:
	if right:
		if whatToWearSlideCount == 7:
			fume.visible(viz.ON)
			eye_wash.visible(viz.ON)
			shower.visible(viz.ON)
			nozzles.visible(viz.ON)
			fire_ext.visible(viz.ON)
			bench.visible(viz.ON)
			sinks.visible(viz.ON)
			taps.visible(viz.ON)
			floor.visible(viz.ON)
			waste.visible(viz.ON)
			visitedToEquipment = True
			next.visible(viz.OFF)
			back.visible(viz.OFF)
		else:
			whatToWearSlideCount = whatToWearSlideCount + 1
			print(whatToWearSlideCount)
	#elif object == back:
	elif left:
		if whatToWearSlideCount == 0:
			whatToWearSlideCount = 0
		else:
			whatToWearSlideCount = whatToWearSlideCount - 1 
			print(whatToWearSlideCount)
	print(whatToWearSlideshow[whatToWearSlideCount])
	screen.texture(viz.addTexture(whatToWearSlideshow[whatToWearSlideCount]))

def equipmentTutorial():
	
	global hitFumeHood
	global hitEyeWash 
	global hitNozzles 
	global hitShower 
	global hitFireExtinguisher
	global hitBench	
	global hitSinks
	global hitTaps
	global hitFloor
	global hitWaste
	
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
	
	if IsThisVillanovaCAVE():
		#Sets orbs to red
		if visitedFumeHood == False and hitFumeHood == False:
			fume.color( viz.RED )
		if visitedEyeWash == False and hitEyeWash == False:
			eye_wash.color( viz.RED )
		if visitedNozzles == False and hitNozzles == False:
			nozzles.color( viz.RED )
		if visitedShower == False and hitShower == False:
			shower.color( viz.RED )
		if visitedFireExtinguisher == False and hitFireExtinguisher == False:
			fire_ext.color( viz.RED )
		if visitedBench == False and hitBench == False:
			bench.color( viz.RED )
		if visitedSinks == False and hitSinks == False:
			sinks.color( viz.RED )
		if visitedTaps == False and hitTaps == False:
			taps.color( viz.RED )
		if visitedFloor == False and hitFloor == False:
			floor.color( viz.RED )
		if visitedWaste == False and hitWaste == False:
			waste.color( viz.RED )
		
		#toProcedure.color( viz.RED )
		
			#changes orb color to green, updates whiteboard, resets view to look at whiteboard
		def hitEquipment(visited, file, orb):
			visited = True
			screen.texture(viz.addTexture("Slides/Equipment/"+file+".jpg"))
			orb.color( viz.GREEN )
			cave_view_matrix = [ -0.260936, 0.000000, 0.965356, 0.000000,
							0.000000, 1.000000, -0.000000, 0.000000,
							-0.965356, -0.000000, -0.260936, 0.000000,
							-0.731557, 2.822117, -4.915627, 1.000000 ]
			vizconnect.getTransport('wandmagiccarpet').getNode3d().setMatrix(cave_view_matrix)

		#checks if trigger is pressed while inside a proximity sensor, if so calls hitEquipment to update room
		if trigger and hitFumeHood:
			hitEquipment(visitedFumeHood, "Fume_Hood", fume)
			visitedFumeHood = True
		if trigger and hitEyeWash:
			hitEquipment(visitedEyeWash, "Eye_Wash", eye_wash)
			visitedEyeWash = True
		elif trigger and hitNozzles:
			hitEquipment(visitedNozzles, "Nozzles", nozzles) 
			visitedNozzles = True
		elif trigger and hitShower:
			hitEquipment(visitedShower, "Shower", shower) 
			visitedShower = True
		elif trigger == True and hitFireExtinguisher == True:
			hitEquipment(visitedFireExtinguisher, "Fire_Extinguisher", fire_ext)
			visitedFireExtinguisher = True
		elif trigger and hitBench:
			hitEquipment(visitedBench, "Lab_Bench", bench)
			visitedBench = True
		elif trigger and hitSinks:
			hitEquipment(visitedSinks, "Sinks", sinks)
			visitedSinks = True
		elif trigger and hitTaps:
			hitEquipment(visitedTaps, "Taps", taps)
			visitedTaps = True
		elif trigger and hitFloor:
			hitEquipment(visitedFloor, "Floor", floor)
			visitedFloor = True
		elif trigger and hitWaste:
			hitEquipment(visitedWaste, "Waste", waste)
			visitedWaste = True
		
		if visitedFumeHood == True and visitedEyeWash == True and visitedNozzles == True and visitedShower == True and visitedFireExtinguisher == True and visitedBench == True and visitedSinks == True and visitedTaps == True and visitedFloor == True and visitedWaste == True:
			toProcedure.visible(viz.ON)
	else:
		object = viz.pick()
		if visitedFumeHood == True and visitedEyeWash == True and visitedNozzles == True and visitedShower == True and visitedFireExtinguisher == True and visitedBench == True and visitedSinks == True and visitedTaps == True and visitedFloor == True and visitedWaste == True:
			toProcedure.visible(viz.ON)
		if object == fume: 
			screen.texture(viz.addTexture("Slides/Equipment/Fume_Hood.jpg"))
			visitedFumeHood = True
			fume.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == eye_wash:
			screen.texture(viz.addTexture("Slides/Equipment/Eye_Wash.jpg"))
			visitedEyeWash = True
			eye_wash.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == nozzles:
			screen.texture(viz.addTexture("Slides/Equipment/Nozzles.jpg"))
			visitedNozzles = True
			nozzles.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == shower:
			screen.texture(viz.addTexture("Slides/Equipment/Shower.jpg"))
			visitedShower = True
			shower.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == fire_ext:
			visitedFireExtinguisher = True 
			screen.texture(viz.addTexture("Slides/Equipment/Fire_Extinguisher.jpg"))
			fire_ext.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == bench:
			visitedBench = True 
			#viz.window.displayHTML( 'www.google.com' )
			#vizact.onkeydown(' ', viz.window.hideHTML )
			screen.texture(viz.addTexture("Slides/Equipment/Lab_Bench.jpg"))
			bench.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == sinks:
			visitedSinks = True 
			screen.texture(viz.addTexture("Slides/Equipment/Sinks.jpg"))
			sinks.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == taps:
			visitedTaps = True 
			screen.texture(viz.addTexture("Slides/Equipment/Taps.jpg"))
			taps.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == floor:
			visitedFloor = True 
			screen.texture(viz.addTexture("Slides/Equipment/Floor.jpg"))
			floor.color( viz.GREEN )
			view.setPosition([0,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == waste:
			visitedWaste = True 
			screen.texture(viz.addTexture("Slides/Equipment/Waste.jpg"))
			waste.color( viz.GREEN )
			view.setPosition([-0.5,4.4,-3.5])
			view.setEuler([-90,0,0])
		elif object == toProcedure: 
			visitedToProcedure = True
			toProcedure.color( viz.GREEN )
			view.setEuler([-90,0,0])
			#turn off previous orbs
			fume.visible(viz.OFF)
			eye_wash.visible(viz.OFF)
			shower.visible(viz.OFF)
			nozzles.visible(viz.OFF)
			fire_ext.visible(viz.OFF)
			bench.visible(viz.OFF)
			sinks.visible(viz.OFF)
			taps.visible(viz.OFF)
			floor.visible(viz.OFF)
			waste.visible(viz.OFF)
			toProcedure.visible(viz.OFF)
			proceduresTutorial()
		
	
		
def proceduresTutorial():
	print('running procedures')	
		
def Juice():
	print('running procedures')	
	global videoCount
	global playNow
	global video
	videos = ['Robbery.mpg','Legends.mpg']
	
	print(videoCount)
	print(playNow)
		
	
	if playNow == True:
		playNow = False
		video = viz.addVideo(videos[videoCount])
		screen.texture(video)
		video.setRate(1)
		video.play()
		
	vizact.waittime(video.getDuration)
	
	if video.getState() == viz.MEDIA_STOPPED:
		videoCount = videoCount = videoCount + 1
		playNow = True
	
	print(videoCount)
	print(playNow)
		
	#video2 = viz.addVideo('Legends.mpg')
	#screen.texture(video)
	#video.play()
	#video.getDuration()
	#screen.texture(video2)
	#video2.play()#Create an action that will fade an object in, wait for 2 seconds, then fade it back out.
	

	
	#fadeAlpha = vizact.fadeTo(1,time=1)
	#setScreen = screen.texture(video)
	#fadeColor = vizact.waittime(video.getDuration)
	#setScreen2 = screen.texture(video2)
	#fadeout = vizact.fadeTo(0,time=1)
	#fadeInOut = vizact.sequence(fadeAlpha, setScreen, video.play(), fadeColor, setScreen2, video2.play(), fadeout)

	#screen.addAction(fadeInOut)

def safetyTutorial():
	global trigger
	global left
	global right
	
	global cave_view_matrix
	
	global fume
	global eye_wash 
	global nozzles 
	global shower 
	global fire_ext 
	global bench
	global sinks 
	global taps 
	global floor 
	global waste 
	
	print(visitedWaste)
	trigger = False
	left = False
	right = False
	
	#FLYSTICK
	if IsThisVillanovaCAVE():
		rawInput = vizconnect.getConfiguration().getRawDict("input")
		rawTracker = vizconnect.getConfiguration().getRawDict("tracker")
		rawAvatar = vizconnect.getConfiguration().getRawDict("avatar")
		BUTTON_LEFT = 4
		BUTTON_RIGHT = 3
		BUTTON_TRIGGER = 0
	else:
		BUTTON_LEFT = 'a'
		BUTTON_RIGHT = 'b'        
		BUTTON_TRIGGER = ' '
		
	def isButtonDown_Trigger():
		if IsThisVillanovaCAVE(): 
			return rawInput['flystick'].isButtonDown(BUTTON_TRIGGER)
		else:
			return (key_pressed == BUTTON_TRIGGER)
	def isButtonDown_Left():
		if IsThisVillanovaCAVE(): 
			return rawInput['flystick'].isButtonDown(BUTTON_LEFT)
		else:
			return (key_pressed == BUTTON_LEFT)
	def isButtonDown_Right():
		if IsThisVillanovaCAVE(): 
			return rawInput['flystick'].isButtonDown(BUTTON_RIGHT)
		else:
			return (key_pressed == RIGHT)

	if isButtonDown_Trigger():
		trigger = True
	if isButtonDown_Left():
		left = True
	if isButtonDown_Right():
		right = True
	
	if visitedToProcedure == True:
		Juice()
	elif visitedToEquipment == True:
		equipmentTutorial()
	elif toWhatToWear == True:
		whatToWear()
	else:
		introduction()

	#if hitFumeHood == True:
		
def tourOutput():
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
	
	print('Equipment Checklist:')
	print('FUME HOOD: ', visitedFumeHood)
	print('EYE WASH STATION: ', visitedEyeWash)
	print('OUTLETS & NOZZLES: ', visitedNozzles)
	print('SAFETY SHOWER: ', visitedShower)
	print('FIRE EXTINGUISHER: ', visitedFireExtinguisher)
	print('LAB BENCH: ', visitedBench)
	print('SINK: ', visitedSinks)
	print('TAPS: ', visitedTaps)
	print('FLOOR: ', visitedFloor)
	print('WASTE: ', visitedWaste)

#sets corresponding hit variable to true if proximity sensor is entered
def EnterProximity(e):
	global hitFumeHood
	global hitEyeWash 
	global hitNozzles 
	global hitShower 
	global hitFireExtinguisher
	global hitBench	
	global hitSinks
	global hitTaps
	global hitFloor
	global hitWaste
	
	global fumeSensor
	global eyeWashSensor
	global nozzlesSensor
	global showerSensor
	global fireExtinguisherSensor
	global benchSensor
	global sinksSensor 
	global tapsSensor 
	global floorSensor 
	global wasteSensor
		
	if e.sensor == fumeSensor:
		hitFumeHood = True
		if visitedFumeHood == False:
			fume.color(viz.BLUE)
	elif e.sensor == eyeWashSensor:
		hitEyeWash = True
		if visitedEyeWash == False:
			eye_wash.color(viz.BLUE)
	elif e.sensor == nozzlesSensor:
		hitNozzles = True
		if visitedNozzles == False:
			nozzles.color(viz.BLUE)
	elif e.sensor == showerSensor:
		hitShower  = True
		if visitedShower == False:
			shower.color(viz.BLUE)
	elif e.sensor == fireExtinguisherSensor:
		hitFireExtinguisher = True
		if visitedFireExtinguisher == False:
			fire_ext.color(viz.BLUE)
	elif e.sensor == benchSensor:
		hitBench = True
		if visitedBench == False:
			bench.color(viz.BLUE)
	elif e.sensor == sinksSensor:
		hitSinks = True
		if visitedSinks == False:
			sinks.color(viz.BLUE)
	elif e.sensor == tapsSensor:
		hitTaps = True
		if visitedTaps == False:
			taps.color(viz.BLUE)
	elif e.sensor == floorSensor:
		hitFloor = True 
		if visitedFloor == False:
			floor.color(viz.BLUE)
	elif e.sensor == wasteSensor:
		hitWaste = True
		if visitedWaste == False:
			waste.color(viz.BLUE)

#sets corresponding hit variable to false if proximity sensor is left
def ExitProximity(e):
	global hitFumeHood
	global hitEyeWash 
	global hitNozzles 
	global hitShower 
	global hitFireExtinguisher
	global hitBench	
	global hitSinks
	global hitTaps
	global hitFloor
	global hitWaste
	hitFumeHood = False
	hitEyeWash = False
	hitNozzles = False
	hitShower = False
	hitFireExtinguisher = False
	hitBench = False	
	hitSinks = False
	hitTaps = False
	hitFloor = False
	hitWaste = False
	
#handle entering and exiting proximity sensors 
manager.onEnter(None,EnterProximity)
manager.onExit(None, ExitProximity)

#prints status of visited equipment 
atexit.register(tourOutput)

if IsThisVillanovaCAVE():
    vizact.ontimer(0.5, safetyTutorial)
else:
	#vizact.onmousedown(viz.MOUSEBUTTON_LEFT,joystick_action)
	viz.callback(viz.KEYDOWN_EVENT,onKeyDown)