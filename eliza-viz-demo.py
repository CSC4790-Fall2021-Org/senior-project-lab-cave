import viz
import vizact
import viztracker

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#diable mouse navigation so viewpoint is never changed
viz.mouse(viz.OFF)

#viz.clearcolor(viz.SKYBLUE)
lab = viz.addChild('lab.ive')

fire = viz.addChild('crate.osgb')
ball = viz.addChild('white_ball.wrl')
flash = viz.addChild('flashlight.osgb')

fire.setPosition([-0.5,2,1.5])
ball.setPosition([0,2,1.5])
ball.setEuler([0,0,0])
flash.setPosition([0.5,2,1.5])

mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)

link = None #The handle to the link object
def grabObj():
	global link
	object = viz.pick()
	if object.valid():
		link = viz.grab( mouseTracker, object )
		
def releaseObj():
	global link
	link.remove()
	link = None
	
vizact.onmousedown(viz.MOUSEBUTTON_LEFT,grabObj)
vizact.onmouseup(viz.MOUSEBUTTON_LEFT,releaseObj)


def turn():
	turnRight = vizact.spin(0,1,0,90,1)
	flash.addAction(turnRight)
	
vizact.onkeydown('s',turn)
