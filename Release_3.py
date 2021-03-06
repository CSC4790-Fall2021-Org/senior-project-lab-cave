import viz 
import vizshape
import atexit
import vizinfo
import viztask
import vizact
import vizcam


viz.go()


filename = "VUCEET013.jpg"
sphere = vizshape.addSphere(radius=20, pos=[0,0,0])
this_texture = viz.addTexture(filename)

#More configuration of the sphere
sphere.texture(this_texture)
sphere.disable(viz.LIGHTING) #make the image appear full color, do not render shadows for sphere

#Flip normals to make texture go on the inside of sphere
sphere.enable(viz.FLIP_POLYGON_ORDER)

view = viz.MainView
view.setPosition([0,-10,-1])
view.setEuler([90,0,0])

vizact.onkeydown(' ',view.setPosition([0,-10,-1]))

sphere.disable(viz.PICKING)

visitedFumeHood = False
visitedEyeWash = False
visitedNozzles = False
visitedShower = False
visitedFireExtinguisher = False
visitedBench = False

#creates equipment orbs
fume = viz.addChild('white_ball.wrl')
eye_wash = viz.addChild('white_ball.wrl')
nozzles = viz.addChild('white_ball.wrl')
shower = viz.addChild('white_ball.wrl')
fire_ext = viz.addChild('white_ball.wrl')
bench = viz.addChild('white_ball.wrl')

#Sets orbs to red
fume.color( viz.RED )
eye_wash.color( viz.RED )
nozzles.color( viz.RED )
shower.color( viz.RED )
fire_ext.color( viz.RED )
bench.color( viz.RED )


#positions orbs
fume.setPosition([-2,-10,-13])
eye_wash.setPosition([0,-12,-10])
nozzles.setPosition([3,-13,-7])
shower.setPosition([8.5,-7,13])
fire_ext.setPosition([-5,-10,15])
bench.setPosition([12,-12,-7])

#Sets up screen 
screen = vizshape.addPlane(size=(5,5), axis=vizshape.AXIS_X, cullFace=True)
screen.setEuler(-180,0,0)
screen.setPosition(15,-8,-2)
screen.disable(viz.LIGHTING)
screen.visible(viz.ON)
screen.texture(viz.addTexture("Slides/Intro.jpg"))


def updateScreenText():
	global visitedFumeHood
	global visitedEyeWash 
	global visitedNozzles 
	global visitedShower 
	global visitedFireExtinguisher
	global visitedBench
	object = viz.pick()
	if object == fume: 
		screen.texture(viz.addTexture("Slides/Fume_Hood.jpg"))
		visitedFumeHood = True
		fume.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])
	elif object == eye_wash:
		screen.texture(viz.addTexture("Slides/Eye_Wash.jpg"))
		visitedEyeWash = True
		eye_wash.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])
	elif object == nozzles:
		screen.texture(viz.addTexture("Slides/Nozzles.jpg"))
		visitedNozzles = True
		nozzles.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])
	elif object == shower:
		screen.texture(viz.addTexture("Slides/Shower.jpg"))
		visitedShower = True
		shower.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])
	elif object == fire_ext:
		visitedFireExtinguisher = True 
		screen.texture(viz.addTexture("Slides/Fire_Extinguisher.jpg"))
		fire_ext.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])
	elif object == bench:
		visitedBench = True 
		viz.window.displayHTML( 'www.google.com' )
		vizact.onkeydown(' ', viz.window.hideHTML )
		screen.texture(viz.addTexture("Slides/Lab_Bench.jpg"))
		bench.color( viz.GREEN )
		view.setPosition([0,-10,-1])
		view.setEuler([90,0,0])	
		
	
	
		
		
	
def tourOutput():
	print('FUME HOOD: ', visitedFumeHood)
	print('EYE WASH STATION: ', visitedEyeWash)
	print('OUTLETS & NOZZLES: ', visitedNozzles)
	print('SAFETY SHOWER: ', visitedShower)
	print('FIRE EXTINGUISHER: ', visitedFireExtinguisher)
	print('LAB BENCH: ', visitedBench)
	
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,updateScreenText)

atexit.register(tourOutput)