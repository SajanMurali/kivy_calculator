from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon="unnamed.png"
        self.operators=["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main.layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black",forground_color = "white")
  
        main_layout.add_widget(self.solution)
if __name__ =="__main__":
    app = MainApp()
    app.run()
