import viz 
import vizshape
import atexit
import vizinfo
import viztask
import vizact
import vizcam
import vizconnect
import vizproximity

IsThisVillanovaCAVE = True
trigger = False

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

#Chemisty Lab set-up
chemLab = viz.addChild("chemlab 50M.xyz.osgb")
chemLab.disable(viz.LIGHTING)
chemLab.setEuler(20,0,0)

#to keep track of which orbs have been visited
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

#determined by proximity sensor
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

#Sets up screen 
screen = vizshape.addPlane(size=(1.2,1.2), axis=vizshape.AXIS_X, cullFace=True)
screen.setEuler(0,0,0)
screen.setPosition(-5.12,4.49,-4.25)
screen.disable(viz.LIGHTING)
screen.visible(viz.ON)
screen.texture(viz.addTexture("Slides/Intro.jpg"))

#sets up "Next" box -- CURRENTLY NOT FUNCTIONING IN CAVE
next = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
next.setEuler(0,0,0)
next.setPosition(-5.08,4.49,-3.45)
next.disable(viz.LIGHTING)
next.visible(viz.ON)
next.texture(viz.addTexture("Slides/Next.jpg"))

#sets up "Back" box -- CURRENTLY NOT FUNCTIONING IN CAVE
back = vizshape.addPlane(size=(.32,.18), axis=vizshape.AXIS_X, cullFace=True)
back.setEuler(0,0,0)
back.setPosition(-5.08,4.49,-5.06)
back.disable(viz.LIGHTING)
back.visible(viz.ON)
back.texture(viz.addTexture("Slides/Back.jpg"))
back.visible(viz.OFF)


#rawTracker = vizconnect.getConfiguration().getRawDict("tracker")
#rawAvatar = vizconnect.getConfiguration().getRawDict("avatar")

#create equipment proximity sensors
fumeSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=fume)
eyeWashSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=eye_wash)
nozzlesSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=shower)
showerSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=shower)
fireExtinguisherSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=fire_ext)
benchSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=bench)
sinksSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=sinks)
tapsSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=taps)
floorSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=floor)
wasteSensor = vizproximity.Sensor(vizproximity.Box([.4,.4,.4],center=[0,0,0]), source=waste)
			
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


def joystick_action():
	global trigger
	global cave_view_matrix
	
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
	
	trigger = False
	
	#FLYSTICK
	if IsThisVillanovaCAVE:
		rawInput = vizconnect.getConfiguration().getRawDict("input")
		rawTracker = vizconnect.getConfiguration().getRawDict("tracker")
		rawAvatar = vizconnect.getConfiguration().getRawDict("avatar")
		BUTTON_LEFT = 4
		BUTTON_RIGHT = 1
		BUTTON_TRIGGER = 0
	else:
		BUTTON_LEFT = 'a'
		BUTTON_RIGHT = 'b'        
		BUTTON_TRIGGER = ' '
		
	def isButtonDown_Trigger():
		if IsThisVillanovaCAVE: 
			return rawInput['flystick'].isButtonDown(BUTTON_TRIGGER)
		else:
			return (key_pressed == BUTTON_TRIGGER)

	if isButtonDown_Trigger():
		trigger = True
	
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
	elif trigger and hitEyeWash:
		hitEquipment(visitedEyeWash, "Eye_Wash", eye_wash) 
	elif trigger and hitNozzles:
		hitEquipment(visitedNozzles, "Nozzles", nozzles) 
	elif trigger and hitShower:
		hitEquipment(visitedShower, "Shower", shower) 
	elif trigger == True and hitFireExtinguisher == True:
		hitEquipment(visitedFireExtinguisher, "Fire_Extinguisher", fire_ext)
	elif trigger and hitBench:
		hitEquipment(visitedBench, "Lab_Bench", bench)	
	elif trigger and hitSinks:
		hitEquipment(visitedSinks, "Sinks", sinks)
	elif trigger and hitTaps:
		hitEquipment(visitedTaps, "Taps", taps)
	elif trigger and hitFloor:
		hitEquipment(visitedFloor, "Floor", floor)
	elif trigger and hitWaste:
		hitEquipment(visitedWaste, "Waste", waste)
		print(visitedWaste)

		
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
	elif e.sensor == eyeWashSensor:
		hitEyeWash = True 
	elif e.sensor == nozzlesSensor:
		hitNozzles = True
	elif e.sensor == showerSensor:
		hitShower  = True
	elif e.sensor == fireExtinguisherSensor:
		hitFireExtinguisher = True
	elif e.sensor == benchSensor:
		hitBench = True
	elif e.sensor == sinksSensor:
		hitSinks = True
	elif e.sensor == tapsSensor:
		hitTaps = True
	elif e.sensor == floorSensor:
		hitFloor = True 
	elif e.sensor == wasteSensor:
		hitWaste = True

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

if IsThisVillanovaCAVE:
    vizact.ontimer(0.5, joystick_action)
else:
    viz.callback(viz.KEYDOWN_EVENT,onKeyDown)
