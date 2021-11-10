import viz
import vizshape
import atexit

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


sphere.disable(viz.PICKING)

visitedFumeHood = False
visitedEyeWash = False
visitedNozzles = False
visitedShower = False
visitedFireExtinguisher = False

fume = viz.addChild('white_ball.wrl')
eye_wash = viz.addChild('white_ball.wrl')
back = viz.addChild('white_ball.wrl')
shower = viz.addChild('white_ball.wrl')
fire_ext = viz.addChild('white_ball.wrl')

fume.setPosition([-2,-10,-13])
eye_wash.setPosition([0,-12,-10])
back.setPosition([3,-13,-7])
shower.setPosition([8.5,-7,13])
fire_ext.setPosition([-5,-10,15])

textScreen = viz.addText('Screen Text',viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.setPosition([0.95,0.05,0])

textScreen.message('')

def updateScreenText():
	global visitedFumeHood
	global visitedEyeWash 
	global visitedNozzles 
	global visitedShower 
	global visitedFireExtinguisher
	object = viz.pick()
	if object == fume: 
		textScreen.message('FUME HOOD')
		visitedFumeHood = True
	elif object == eye_wash:
		textScreen.message('EYE WASH STATION')
		visitedEyeWash = True
	elif object == back:
		textScreen.message('OUTLETS & NOZZLES')
		visitedNozzles = True
	elif object == shower:
		textScreen.message('SAFETY SHOWER')
		visitedShower = True
	elif object == fire_ext:
		textScreen.message('FIRE EXTINGUISHER')
		visitedFireExtinguisher = True 
	else:
		textScreen.message('')
		
	
def tourOutput():
	print('FUME HOOD: ', visitedFumeHood)
	print('EYE WASH STATION: ', visitedEyeWash)
	print('OUTLETS & NOZZLES: ', visitedNozzles)
	print('SAFETY SHOWER: ', visitedShower)
	print('FIRE EXTINGUISHER: ', visitedFireExtinguisher)
	
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,updateScreenText)

atexit.register(tourOutput)