import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Add a ground plane and set the background color
ground = viz.addChild('ground.osgb')
viz.clearcolor(viz.SLATE)

#Add some text objects
text3D = viz.addText3D('3D Text',pos=[0,2.5,6],align=viz.ALIGN_CENTER_BOTTOM)
text2D = viz.addText('2D Text',pos=[0,1,6],align=viz.ALIGN_CENTER_BOTTOM)
textScreen = viz.addText('Screen Text',parent=viz.ORTHO,pos=[20,20,0],fontSize=50)

#Spin the text
text3D.addAction(vizact.spin(0,1,0,15))
text2D.addAction(vizact.spin(0,1,0,-15))

#Set backdrop for the 2D text, increase resolution, and disable lighting
text2D.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
text2D.resolution(1)
text2D.disable(viz.LIGHTING)

#Make 3D text thickness adjustable
import vizconfig
cfg = vizconfig.BasicConfigurable('3D Text')
cfg.addFloatRangeItem('Thickness',[0.01,0.5],fset=text3D.setThickness,fget=text3D.getThickness)
vizconfig.register(cfg)
vizconfig.getConfigWindow().setWindowVisible(True)