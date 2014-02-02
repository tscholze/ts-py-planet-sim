from PyQt4 import QtCore, QtGui, uic
import vtk
import os
from distributed_computing.Master import Master
from distributed_computing.Movement import Movement

class PlanetSimulation(QtGui.QDialog):
    '''
    Haupt- und Startklasse der Planetensimulation
    '''
    __timer = QtCore.QTimer()
    __renderer = vtk.vtkRenderer()
    __list_of_planets = []
    __list_of_actors = []
    
    __scale_sun_radius = 0.00000006
    __scale_planet_radius = 0.000001
    __scale_planet_orbit_inner = 0.000000001
    
    __correction_factor = 1e9
    __delta_t = 1
    
    #__master = object()
    #__movement = object()
    def __init__(self):
        '''
        Konstruktor welche alle globalen Daten initialisiert.
        - timer
        - vtk init
        - camera
        - vtk connectors
        '''
        self.__time = 0.0
        self.__timer.setInterval(1000 / 25)
        self.connect(self.__timer, QtCore.SIGNAL('timeout()'),
            self.__doAnimationStep)
        
        self.__master = Master()
        self.__movement = Movement(self.__master)
        
        self.__status = 'FINISHED'

        QtGui.QDialog.__init__(self)

        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__),"planetSim.ui"))
        self.ui.show()

        self.ui.vtkWidget.Initialize()
        self.ui.vtkWidget.Start()
        
        cam = self.__renderer.GetActiveCamera()
        cam.SetPosition(1, 0, -400)
        cam.SetFocalPoint(0, 0, 0)
        cam.SetClippingRange(.1, 40)
        cam.SetViewUp(0, 1, 0)
        cam.SetViewAngle(50)
        self.__renderer.SetActiveCamera(cam)
        
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(self.__renderer)
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.ui.vtkWidget.SetInteractorStyle(style)
        self.connect(self.ui.startButton, QtCore.SIGNAL('clicked()'),
                    self.__startAnimation)
        self.connect(self.ui.stopButton, QtCore.SIGNAL('clicked()'),
                    self.__stopAnimation)

        self.connect(self.ui.btn_sunsystem, QtCore.SIGNAL('clicked()'),
                     self.__load_sunsystem)
        
        self.connect(self.ui.btn_custom_system, QtCore.SIGNAL('clicked()'),
                     self.__load_custom_sunsystem)
        
        self.connect(self.ui.slider_amount_bodies, QtCore.SIGNAL('valueChanged(int)'),
                     self.__update_amount_of_bodies)
        
        self.connect(self.ui.slider_sun_mass_factor, QtCore.SIGNAL('valueChanged(int)'),
                     self.__update_sun_mass_factor)
               
        self.connect(self.ui.dail_planet_mass_min, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_mass_min)
        
        self.connect(self.ui.dail_planet_mass_max, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_mass_max)
        
        self.connect(self.ui.dail_planet_radius_min, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_radius_min)
        
        self.connect(self.ui.dail_planet_radius_max, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_radius_max)
        
        self.connect(self.ui.dail_planet_orbit_min, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_orbit_min)
        
        self.connect(self.ui.dail_planet_orbit_max, QtCore.SIGNAL('valueChanged(int)'), 
                     self.__update_planet_orbit_max)
              
        self.connect(self.ui.slider_animation_speed, QtCore.SIGNAL('valueChanged(int)'), 
                    self.__update_speed)
        
        self.connect(self.ui.slider_delta_t, QtCore.SIGNAL('valueChanged(int)'),  
                     self.___update_delta_t)
        
        self.connect(self.ui.slider_correction_factor, QtCore.SIGNAL('valueChanged(int)'),
                     self.__update_correction_factor)

    def __init_renderer(self, list_of_planets):
        '''
        Generiert den Renderer fuer eine uebergebene Liste von Objekten
        @param list_of_planets Liste der zu rendernden Objekte
        '''
        for planet in list_of_planets:
            actor = vtk.vtkActor()
            #sphere = vtk.vtkSphereSource()
            sphere = vtk.vtkTexturedSphereSource()
            mapper = vtk.vtkPolyDataMapper()
            sphere.SetPhiResolution(20)
            sphere.SetThetaResolution(20)
            scaled_radius = planet.get_radius() * self.__scale_planet_radius 
            if(planet.id == 0):
                scaled_radius = planet.get_radius() * self.__scale_sun_radius
            
            sphere.SetRadius(scaled_radius)
            mapper.SetInput(sphere.GetOutput())
            graphic_name = os.path.join(os.path.dirname(__file__))+"/../textures/"+planet.get_name()+".jpg"
            graphic_reader = vtk.vtkJPEGReader()
            graphic_reader.SetFileName(graphic_name)
            graphic_texture = vtk.vtkTexture()
            graphic_texture.SetInputConnection(graphic_reader.GetOutputPort())
            graphic_texture.InterpolateOn()
            actor.SetTexture(graphic_texture)
            actor.SetMapper(mapper)
            actor.SetScale(1,1,1)
            actor.SetPosition(int(self.__scale_planet_orbit_inner*planet.get_posVector_x()), 
                              int(self.__scale_planet_orbit_inner*planet.get_posVector_y()), 
                              int(self.__scale_planet_orbit_inner*planet.get_posVector_z()))
            self.__renderer.AddActor(actor)
            self.__list_of_actors.append(actor)

    def __update_renderer(self, list_of_planets):
        '''
        updated den Renderer mit neuen Positionswerten der uebergebenen Objekte
        @param list_of_planets Liste von zu aktualisierenden Objekten
        '''
        i = 0
        while i < len(list_of_planets):
            planet = list_of_planets[i]
            self.__list_of_actors[i].SetPosition(self.__scale_planet_orbit_inner*planet.get_posVector_x(), 
                                                   self.__scale_planet_orbit_inner*planet.get_posVector_y(), 
                                                   self.__scale_planet_orbit_inner*planet.get_posVector_z())
            i = i + 1
        self.__list_of_planets = list_of_planets   

    def __update_amount_of_bodies(self):
        '''
        Updated GUI Element tf_amount_of_bodies
        '''
        self.ui.tf_amout_bodies.setText(str(self.ui.slider_amount_bodies.value()))
        
    def __update_sun_mass_factor(self):
        '''
        Updated GUI Element tf_sun_mass_factor
        '''
        self.ui.tf_sun_mass_factor.setText(str(self.ui.slider_sun_mass_factor.value()))
    
    def __update_planet_mass_min(self):
        '''
        Updated GUI Element tf_planet_mass_min
        '''
        self.ui.tf_planet_mass_min.setText(str(self.ui.dail_planet_mass_min.value()))
        
    def __update_planet_mass_max(self):
        '''
        Updated GUI Element tf_planet_mass_max
        '''
        self.ui.tf_planet_mass_max.setText(str(self.ui.dail_planet_mass_max.value()))
        
    def __update_planet_radius_min(self):
        '''
        Updated GUI Element tf_planet_radius_min
        '''
        self.ui.tf_planet_radius_min.setText(str(self.ui.dail_planet_radius_min.value()))
    
    def __update_planet_radius_max(self):
        '''
        Updated GUI Element tf_planet_radius_max
        '''
        self.ui.tf_planet_radius_max.setText(str(self.ui.dail_planet_radius_max.value()))
    
    def __update_planet_orbit_min(self):
        '''
        Updated GUI Element tf_planet_orbit_min
        '''
        self.ui.tf_planet_orbit_min.setText(str(self.ui.dail_planet_orbit_min.value()))
    
    def __update_planet_orbit_max(self):
        '''
        Updated GUI Element tf_planet_orbit_max
        '''
        self.ui.tf_planet_orbit_max.setText(str(self.ui.dail_planet_orbit_max.value()))
        
    def ___update_delta_t(self):
        '''
        Updated globale Variable __delta_t inklusive Faktor 1e3
        '''
        self.__delta_t = self.ui.slider_delta_t.value() * 1e3
        
    def __update_speed(self):
        '''
        setzt das Interval des Timer neu mit Werten von slider_animation_speed
        '''
        self.__timer.setInterval(1000 / self.ui.slider_animation_speed.value())
        
    def __update_correction_factor(self):
        '''
        setzt den Korrekturfaktor neu mit dem Wert von slider_correction_factor inklusive Faktor 1e7
        '''
        self.__correction_factor = self.ui.slider_correction_factor.value() * 1e7
        
    def __doAnimationStep(self):
        '''
        fuert einen Animationsstep aus.
        '''
        self.__time = self.__time + .01
        if self.__status == 'FINISHED':
            self.__status = 'WORKING'
            self.__renderer = self.__update_renderer(self.__movement.updateSunsystem(self.__list_of_planets, self.__delta_t, self.__correction_factor))
            self.__status = 'FINISHED'
            #print self.__status, " at ", self.__time
        self.ui.vtkWidget.update()

    def __startAnimation(self):
        '''
        startet die Animation in dem der Timer gestartet wird.
        '''
        self.__timer.start()

    def __stopAnimation(self):
        '''
        stopt die Animation in dem der Timer gestoppt wird.
        '''
        self.__timer.stop()
     
    def __load_sunsystem(self):
        '''
        generiert ein Sonnensystem welches des unseren gleicht.
        '''
        from EarthSunsystemCalc import generate_our_sunsystem
        self.__list_of_planets = generate_our_sunsystem()
        self.__init_renderer(self.__list_of_planets)
    
    def __load_custom_sunsystem(self):
        '''
        generiert ein durch den Benutzer eingestellten Wertebereiche festgelegtes
        Sonnensystem
        '''
        from RandomSunsystemCalc import generate_random_system
        self.__list_of_planets = generate_random_system(int(self.ui.tf_amout_bodies.toPlainText()) , 
                                                        int(self.ui.tf_sun_mass_factor.toPlainText()), 
                                                        int(self.ui.tf_planet_mass_min.toPlainText()), 
                                                        int(self.ui.tf_planet_mass_max.toPlainText()), 
                                                        int(self.ui.tf_planet_radius_min.toPlainText()), 
                                                        int(self.ui.tf_planet_radius_max.toPlainText()), 
                                                        int(self.ui.tf_planet_orbit_min.toPlainText()), 
                                                        int(self.ui.tf_planet_orbit_max.toPlainText()))
        self.__init_renderer(self.__list_of_planets)