from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#/class Frame(GridLayout):
#	def __init__(self,**kwargs):
#		super(Frame,self).__init__(**kwargs)
#		self.cols=2
#		self.txt=TextInput(multiline=False)
#		self.add_widget(self.txt)

class Butn(BoxLayout):
	def __init__(self,**kwargs):
		super(Butn,self).__init__(**kwargs)
		self.layout=BoxLayout(orientation='vertical')
		self.b=Button(text="push it 1:")
		self.add_widget(self.b)
		self.b1=Button(text="push it 2:", size_hint=(.5, 1), pos=(200,20))
		self.add_widget(self.b1)
		self.b2=Button(text="push it 3:",color=(2,1,0,1))
		self.add_widget(self.b2)

class Main(App):
	def build(self):
#		return Frame()
		return Butn()

if(__name__ == '__main__'):
	Main().run()