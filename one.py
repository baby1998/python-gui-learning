from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
class A(GridLayout):
	def __init__(self,**kwargs):
		super(A,self).__init__(**kwargs)
		self.cols=2
		self.add_widget(Label(text="hello"))
		self.user=TextInput(multiline=True)
		self.add_widget(self.user)
		self.btn=Button(text="Push It")
		self.add_widget(self.btn)
class MyApp(App):
	def build(self):
		return A()
		
if(__name__ == '__main__'):
	MyApp().run()