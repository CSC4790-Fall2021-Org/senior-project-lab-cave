"""
Use the mouse and arrow keys to fly around the proximity sensors
Press spacebar to toggle debug shapes
"""
import viz
import vizact
import vizcam
import vizproximity

viz.go()
viz.fov(60)
viz.add('dojo.osgb')

import vizinfo
vizinfo.InfoPanel()

# Setup fly navigator
cam = vizcam.FlyNavigate()
viz.cam.setHandler(cam)

# Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(True)

# Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

# Create sphere sensor attached to static matrix
sensor = vizproximity.Sensor(vizproximity.Sphere(1.0),source=viz.Matrix.translate(2,1.5,1))
manager.addSensor(sensor)

# Create composite sensor attached to a node
group = viz.addGroup()
group.setPosition(0,1.5,5)
action = vizact.sequence( vizact.moveTo([-4,1.5,5],speed=1), vizact.moveTo([4,1.5,5],speed=1), viz.FOREVER)
group.addAction( action)
shapes = []
shapes.append(vizproximity.Box([1,1,1]))
shapes.append(vizproximity.Sphere(0.5,center=[0,1,0]))
sensor = vizproximity.Sensor(vizproximity.CompositeShape(shapes),group)
manager.addSensor(sensor)

# Create box sensor attached to tracker
tracker = viz.add('testtrack_all.dls')
trackerLink = viz.link(tracker,viz.NullLinkable,offset=(0,1,0))
sensor = vizproximity.Sensor(vizproximity.Box([0.5,0.5,0.5]),trackerLink)
manager.addSensor(sensor)

# Create sensor using bounding box of node
node = viz.addChild('plant.osgb',pos=(8,0,6))
node.addAction(vizact.spin(0,1,0,45,viz.FOREVER))
sensor = vizproximity.addBoundingBoxSensor(node)
manager.addSensor(sensor)

# Create sensor using bounding sphere of node
node = viz.addChild('beachball.osgb',pos=(-8,1.5,6))
action = vizact.sequence( vizact.sizeTo([2,2,2],speed=1), vizact.sizeTo([1,1,1],speed=1), viz.FOREVER)
node.addAction(action)
sensor = vizproximity.addBoundingSphereSensor(node)
manager.addSensor(sensor)

# Create sensor using bounding box of sub-node
node = viz.addChild('logo.ive',pos=(-4,0,7))
action = vizact.sequence( vizact.moveTo([-4,1,7],speed=1), vizact.moveTo([-4,0,7],speed=1), viz.FOREVER)
node.addAction(action)
sensor = vizproximity.addBoundingBoxSensor(node,name='Sphere01-FACES')
manager.addSensor(sensor)

# Create sensor using avatar bone
avatar = viz.addAvatar('vcc_male2.cfg',pos=[4, 0, 7],euler=[180,0,0])
avatar.state(5)
head = avatar.getBone('Bip01 Head')
sensor = vizproximity.Sensor(vizproximity.Sphere(0.3,center=[0,0.1,0]),head)
manager.addSensor(sensor)

# Register callbacks for proximity sensors
def EnterProximity(e):
	print 'Entered',e.sensor

def ExitProximity(e):
	print 'Exited',e.sensor

manager.onEnter(None, EnterProximity)
manager.onExit(None, ExitProximity)

# Press spacebar to toggle debug shapes
vizact.onkeydown(' ',manager.setDebug,viz.TOGGLE)
