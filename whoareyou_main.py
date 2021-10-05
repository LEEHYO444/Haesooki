from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput



# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<FirstScreen>:
    BoxLayout:
        Button:
            text: 'Who Are You?'
            on_press: root.manager.current = 'menu'

<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Record and Save'
            on_press: root.manager.current = 'recording'
        Button:
            text: 'Recognize'
            on_press: root.manager.current = 'recognizing'

<RecordingScreen>:
    BoxLayout:
   #     Label:
   #        text:
        Button:
            text: 'Start recording'
            size_hint: 0.001,0.2
            pos_hint: {'center_x':0.7,'center_y':0.1}
            on_press: root.manager.current = 'naming'
    
<RecognzingScreen>:
    BoxLayout:
        
        Button:
            text: 'Start recognizing'

<NamingScreen>:
    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Name: "

            TextInput:
                id: name
                multiline: False
            
        Button:
            text: "Save"
            on_press: root.manager.current = 'complete'

<SaveCompleteScreen>:
    BoxLayout:

        Label:
            text: "Save Complete!"



""")

# Declare both screens
class FirstScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class RecordingScreen(Screen):
    pass

class RecognizingScreen(Screen):
    pass

class NamingScreen(Screen):
    pass

class SaveCompleteScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(RecordingScreen(name='recording'))
        sm.add_widget(RecognizingScreen(name='recognizing'))
        sm.add_widget(NamingScreen(name='naming'))
        sm.add_widget(SaveCompleteScreen(name='complete'))

        return sm

if __name__ == '__main__':
    TestApp().run()