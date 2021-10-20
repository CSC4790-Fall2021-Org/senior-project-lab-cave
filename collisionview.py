import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.addChild('playground.wrl')
viz.clearcolor(viz.SLATE)

viz.MainView.setPosition( [5, 1.82, -15] )

#Start collision detection.
viz.MainView.collision( viz.ON )
#Make gravity weaker.
viz.MainView.gravity(2)

viz.stepsize(0.5)

quad = viz.addTexQuad()
quad.setScale([2,8.5,1])
quad.setEuler([0,79,0])
quad.setPosition([10,1.2,-1.22])

quad.alpha(0.4)