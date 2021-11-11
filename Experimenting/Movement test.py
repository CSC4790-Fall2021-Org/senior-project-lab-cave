import viz
import vizact
import vizproximity
import viztask
import vizinfo

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Move the viewpoint to the starting location
viz.MainView.move([10.5,0,20.5])
viz.MainView.setEuler([-90,0,0])
viz.MainView.collision( viz.ON )

piazza = viz.add('piazza.osgb')

#Add plant marker for participant to walk to
plantMarker = viz.addChild('plant.osgb',pos=[-10.3,0,20.6],scale=[0.5,0.5,0.5])

#Add crates marker for participant to walk to
crate1 = viz.addChild('crate.osgb',pos=[-9.9,0.3,5.7],scale=[0.6,0.6,0.6])
crate2 = crate1.clone(pos=[-9.8,0.3,5.05],euler=[5,0,0],scale=[0.6,0.6,0.6])
crate3 = crate1.clone(pos=[-9.8,0.9,5.35],euler=[-5,0,0],scale=[0.6,0.6,0.6])


#Create sensors for destinations 
plantSensor = vizproximity.Sensor(vizproximity.Box([4,5,5],center=[0,2.5,0]),source=plantMarker)
cratesSensor = vizproximity.Sensor(vizproximity.Box([5,4,4],center=[0,1.7,0]),source=crate1)
cafeSensor = vizproximity.Sensor(vizproximity.Box([5,4,10]),source=viz.Matrix.translate(12,2,7.5))


viz.MainView.moveTo([0,0,25],speed=2)
