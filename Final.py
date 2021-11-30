import viz 
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

whatToWearSlideCount = 0
videoCount = 0
playNow = True
playBackgroundNow = True

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
screen.texture(viz.addTexture("Slides/Transition/Intro.jpg"))

#sets up "Next" box
next = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
next.setEuler(0,0,0)
next.setPosition(-5.08,4.49,-3.45)
next.disable(viz.LIGHTING)
next.visible(viz.ON)
next.texture(viz.addTexture("Slides/Transition/Next.jpg"))

#sets up "Back" box
back = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
back.setEuler(0,0,0)
back.setPosition(-5.08,4.49,-5.06)
back.disable(viz.LIGHTING)
back.visible(viz.ON)
back.texture(viz.addTexture("Slides/Transition/Back.jpg"))
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
bench.setPosition([-0.5,3.9,-7.5])
sinks.setPosition([-2.7,4.1,-4.8])
taps.setPosition([-3,4,-1])
floor.setPosition([2,3.2,-3.1])
waste.setPosition([-4.5,3.6,-4])
toProcedure.setPosition([-5,5,-5])

def safetyTutorial():
	global playBackgroundNow
	if playBackgroundNow==True:
		background = viz.addAudio('Sounds/Background.wav') 
		background.loop(viz.ON) 
		background.volume(.5) 
		background.setTime(1) 
		bachground.play() 
		playBackgroundNow=False
	if visitedToProcedure == True:
		Juice()
	elif visitedToEquipment == True:
		equipmentTutorial()
	elif toWhatToWear == True:
		whatToWear()
	else:
		introduction()
		
def introduction():
	print('running introduction')
	global toWhatToWear
	object = viz.pick()
	if object == next:
		screen.texture(viz.addTexture("Slides/Transition/WhatToWear.jpg"))
		toWhatToWear = True
		back.visible(viz.ON)
	
def whatToWear():
	global visitedToEquipment
	print('running what to wear')
	global whatToWearSlideCount
	#disables equipment orbs
	whatToWearSlideshow = ['Slides/Transition/WhatToWear.jpg', 'Slides/WhatToWear/Footwear.jpg','Slides/WhatToWear/Pants.jpg', 'Slides/WhatToWear/Shirts.jpg','Slides/WhatToWear/Hair.jpg','Slides/WhatToWear/Eyes.jpg','Slides/WhatToWear/SafetyGear.jpg','Slides/Transition/WhatToWearExit.jpg']
	object = viz.pick()
	if object == next:
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
	elif object == back:
		if whatToWearSlideCount == 0:
			whatToWearSlideCount = 0
		else:
			whatToWearSlideCount = whatToWearSlideCount - 1 
			print(whatToWearSlideCount)
	print(whatToWearSlideshow[whatToWearSlideCount])
	screen.texture(viz.addTexture(whatToWearSlideshow[whatToWearSlideCount]))

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
	if visitedFumeHood == True and visitedEyeWash == True and visitedNozzles == True and visitedShower == True and visitedFireExtinguisher == True and visitedBench == True and visitedSinks == True and visitedTaps == True and visitedFloor == True and visitedWaste == True:
		toProcedure.visible(viz.ON)
		
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
		video = viz.addVideo('sounds/'+videos[videoCount])
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
	
		
def tourOutput():
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
	print('PROCEDURE SECTION: ', visitedToProcedure)
	
#def onMouseDown(button):
#    if button == viz.MOUSEBUTTON_LEFT:
#        print('you hit the left mouse button')
#viz.callback(viz.MOUSEDOWN_EVENT,onMouseDown)


vizact.onmousedown(viz.MOUSEBUTTON_LEFT,safetyTutorial)

atexit.register(tourOutput)