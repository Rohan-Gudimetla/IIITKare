from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard

kv = Builder.load_file('loginsignup.kv')

class ls_window(Screen):
    pass
class MD3Card(MDCard):
    pass

# class LoginSignup(App):
#     def build(self):
#         return kv

# shit = LoginSignup()
# shit.run()