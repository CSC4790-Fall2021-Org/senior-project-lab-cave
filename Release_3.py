import viz 
import vizshape
import atexit
import vizinfo
import viztask
import vizact


viz.go()

#Add info panel to display messages to participant
instructions = vizinfo.InfoPanel(align=viz.ALIGN_CENTER,fontSize=60,icon=False,key=None)

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


sphere.disable(viz.PICKING)

visitedFumeHood = False
visitedEyeWash = False
visitedNozzles = False
visitedShower = False
visitedFireExtinguisher = False

fume = viz.addChild('white_ball.wrl')
fume.color( viz.RED )

eye_wash = viz.addChild('white_ball.wrl')
eye_wash.color( viz.RED )

nozzles = viz.addChild('white_ball.wrl')
nozzles.color( viz.RED )

shower = viz.addChild('white_ball.wrl')
shower.color( viz.RED )

fire_ext = viz.addChild('white_ball.wrl')
fire_ext.color( viz.RED )

fume.setPosition([-2,-10,-13])
eye_wash.setPosition([0,-12,-10])
nozzles.setPosition([3,-13,-7])
shower.setPosition([8.5,-7,13])
fire_ext.setPosition([-5,-10,15])

textScreen = viz.addText('Screen Text',viz.SCREEN)
textScreen.alignment(viz.ALIGN_RIGHT_BOTTOM)
textScreen.color(viz.GREEN)
textScreen.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
textScreen.setBackdropColor(viz.BLACK)
textScreen.setPosition([0.95,0.05,0])

screen = vizshape.addPlane(size=(5,5), axis=vizshape.AXIS_X, cullFace=True)
screen.setEuler(-180,0,0)
screen.setPosition(15,-8,-2)
screen.disable(viz.LIGHTING)
screen.visible(viz.ON)



textScreen.message('')

# Action for hiding/showing text\\
DelayHide = vizact.sequence( vizact.waittime(10), vizact.method.visible(False) )
Show = vizact.method.visible(True)\



def updateScreenText():
	global visitedFumeHood
	global visitedEyeWash 
	global visitedNozzles 
	global visitedShower 
	global visitedFireExtinguisher
	object = viz.pick()
	if object == fume: 
		textScreen.message('FUME HOOD')
		screen.texture(viz.addTexture("Fume_Hood.jpg"))
		visitedFumeHood = True
		fume.color( viz.GREEN )
	elif object == eye_wash:
		textScreen.message('EYE WASH STATION')
		instructions.runAction(Show)
		instructions.setText("An eye wash station is available at some (but not all) of the wash sinks.  \n"
		"These will be pointed out on the first day, and you should be aware of which one is closest to your lab bench.  \n"
		"To operate, push forward and down on the handle, and place your eyes over the two nozzles.  Keep your eyes open to \n"
		"the gentle stream of water in order to wash out the irritants.  Make sure to get attention from someone to help you.  \n"
		"If you see someone else using the eye wash station, alert a TA or Instructor.")
		instructions.runAction(DelayHide)
		visitedEyeWash = True
		eye_wash.color( viz.GREEN )
	elif object == nozzles:
		textScreen.message('OUTLETS & NOZZLES')
		instructions.runAction(Show)
		instructions.setText("Notice that the back of the bench features electrical outlets as well as several nozzles. \n"  
		"The nozzles are connections for: \n \n"
		"1: Vacuum (for use with a Buchner vacuum filtration funnel)\n"
		"2: Pressurized air (useful to speed up the drying of glassware)\n"
		"3: Natural gas (for use with a Bunsen burner)")
		instructions.runAction(DelayHide)
		visitedNozzles = True
		nozzles.color( viz.GREEN )
	elif object == shower:
		viz.window.displayHTML( 'hw1.html' )
		vizact.onkeydown(' ', viz.window.hideHTML )
		#textScreen.message('SAFETY SHOWER')
		#instructions.setText("A safety shower is also available in the lab.  These are only to be used for large volume spills on your body, \n"
		#"or should a part of your clothing catch fire.  To operate, pull down on the handle to douse yourself in water.")
		#instructions.runAction(DelayHide)
		#visitedShower = True
		shower.color( viz.GREEN )
	elif object == fire_ext:
		textScreen.message('FIRE EXTINGUISHER')
		visitedFireExtinguisher = True 
		screen.texture(viz.addTexture("Slides/Fire_Extinguisher.jpg"))
		view.setEuler([90,0,0])
		fire_ext.color( viz.GREEN )
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