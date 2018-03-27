from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
class Get(App):
	def build(self):
		b=GridLayout(orientation='vertical')
		b.cols=2
		txt=TextInput(multiline=True,size_hint_x=None,height=500,width=1000)
		b.add_widget(txt)
		Btn=Button(text="One")
		b.add_widget(Btn)
		btn2=Button(text="Two")
		b.add_widget(btn2)
		return b

if __name__=='__main__':
	Get().run()