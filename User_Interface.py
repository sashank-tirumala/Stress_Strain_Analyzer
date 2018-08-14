from BeamClass import*
import funcs_for_user_interface
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def __init__(self):
        self.beam=0
        self.pin_joint=True
        self.cantilever=False
        self.circle = True
        self.rectangle = False
        self.ibeam = False
        self.areatype = 'circle'
    def on_Create_New_Beam_Button_clicked(self,button):
        print('Create New Button has been clicked')
        print(self.radius)
        newBeam=funcs_for_user_interface.getValuesForNewBeam(builder,self.pin_joint,self.cantilever)
        self.beam=Beam(newBeam['Length'],newBeam['Support-Type'],self.areatype,newBeam['E'],0,0,self.radius,self.length,self.breadth,self.Ia,self.Ib,self.IH,self.Ih)
        print(newBeam['E'])
        print(self.radius)
        if(self.pin_joint):
            support_window.show_all()
        if(self.circle):
            circle_window.show_all()
        if(self.rectangle):
            rectangle_window.show_all()
        if(self.ibeam):
            ibeam_window.show_all()
        print(self.cantilever)
        print(self.beam)
    def on_Discrete_Force_Button_clicked(self, button):
        print("Discrete button has been clicked")
        ForceValues=funcs_for_user_interface.getValuesForDiscreteForce(builder)
        self.beam.getDiscreteForce(ForceValues['Distance'],ForceValues['Magnitude'])
    def on_Display_Graphs_clicked(self,button):
        print('Display Graphs button has been clicked')
        self.beam.calcShearForceEq()
        self.beam.calcBendingMomentEq()
        self.beam.calcSupportReac()
        self.beam.calcShearForceEq()
        self.beam.calcBendingMomentEq()
        self.beam.calcDeflection()
        self.beam.maxDeflection()
        self.beam.maxBendingStress()
        self.beam.printLoadEquation()
        self.beam.printShearForceEquation()
        self.beam.printBendingMomentEquation()
        self.beam.plotLoadEq()
        self.beam.plotShearEq()
        self.beam.plotBendingMomentEq()
        self.beam.plotDeflection()
    def on_Continuous_Force_Button_clicked(self,button):
        print('Continuous button has been clicked')
        resValues=funcs_for_user_interface.getValuesForContinuousForce(builder)
        resValues['Equation'].replace('-','+-')
        resValues['Equation']=resValues['Equation'].split('+')
        for everypart in resValues['Equation']:
            self.beam.getContinuousForce(resValues['Left Distance'],resValues['Right Distance'],everypart)
    def on_Moment_Button_clicked(self,button):
        print('Moment button has been clicked')
        ForceValues=funcs_for_user_interface.getValuesForMoment(builder)
        self.beam.getBendingMoment(ForceValues['Distance'],ForceValues['Magnitude'])
    def on_gtk_quit_activate(self,button):
        Gtk.main_quit()
    def on_Support_Type_Cantilever_clicked(self,button):
        self.cantilever=True
        self.pin_joint=False
        print(self.cantilever)
    def on_Support_Type_Pin_Joint_clicked(self,button):
        self.cantilever=False
        self.pin_joint=True
    def on_Support_Submit_clicked(self,button):
        self.beam.support1=float(builder.get_object('Support_X_Distance').get_text())
        self.beam.support2=float(builder.get_object('Support_Y_Distance').get_text())
        support_window.destroy()
    def on_circle_submit_clicked(self,button):
        self.beam.circleradius=float(builder.get_object('Radius').get_text())
        circle_window.destroy()
    def on_rectangle_submit_clicked(self,button):
        self.beam.rectlength = float(builder.get_object('Length').get_text())
        self.beam.rectbreadth = float(builder.get_object('Breadth').get_text())
        rectangle_window.destroy()
    def on_ibeam_submit_clicked(self,button):
        self.beam.Ia = float(builder.get_object('Ia').get_text())
        self.beam.Ib = float(builder.get_object('Ib').get_text())
        self.beam.Ih = float(builder.get_object('Ih').get_text())
        self.beam.IH = float(builder.get_object('IH').get_text())
        ibeam_window.destroy()
    def on_Area_Type_Circle_clicked(self,button):
        self.circle = True
        self.rectangle = False
        self.ibeam  = False
    def on_Area_Type_Rectangle_clicked(self,button):
        self.areatype = 'rectangle'
        self.circle = Falsepu
        self.rectangle = True 
        self.ibeam = False
    def on_Area_Type_IBeam_clicked(self,button):
        self.areatype = 'ibeam'
        self.circle = False
        self.rectangle = False
        self.ibeam = True 
   
    
    




builder = Gtk.Builder()
builder.add_from_file("user_interface.glade")
builder.connect_signals(MyWindow())
distance=builder.get_object('Distance_Of_Discrete_Force')
magnitude=builder.get_object('Magnitude_Of_Discrete_Force')
window = builder.get_object("window1")
circle_window = builder.get_object('CircleWindow')
rectangle_window = builder.get_object('RectangleWindow')
ibeam_window = builder.get_object('IbeamWindow')
support_window=builder.get_object('support_window')

window.show_all()


Gtk.main()