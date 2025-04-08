from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.lang import Builder

KV = '''
MDScreen:
    md_bg_color: 0.1, 0.1, 0.1, 1

    BoxLayout:
        orientation: "vertical"
        padding: "24dp"
        spacing: "16dp"
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDLabel:
            text: "Login to Your Account"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: None

        MDTextField:
            id: nc_field
            hint_text: "National Code"
            icon_right: "account"
            mode: "rectangle"
            size_hint_x: 1

        MDTextField:
            id: password_field
            hint_text: "Password"
            icon_right: "lock"
            password: True
            mode: "rectangle"
            size_hint_x: 1

        MDRaisedButton:
            text: "Login"
            on_release: app.login()
            md_bg_color: 0.2, 0.6, 1, 1
            text_color: 1, 1, 1, 1
            size_hint_x: 1
'''

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

LoginApp().run()
