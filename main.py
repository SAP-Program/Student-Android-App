from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from database_handler import check_identity

KV = '''
ScreenManager:
    LoginScreen:
        name: "login"
    HomeScreen:
        name: "home"

<LoginScreen>:

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

<HomeScreen>:
    md_bg_color: 0.2, 0.2, 0.2, 1

    MDLabel:
        text: "Welcome!"
        halign: "center"
        pos_hint: {"center_y": 0.85}
        font_style: "H4"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

    MDRaisedButton:
        text: "Start"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        text_color: 1, 1, 1, 1
        md_bg_color: 0.2, 0.6, 1, 1

'''

class LoginScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
    pass

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)
    
    def login(self):
        login_screen = self.root.get_screen("login")
        nc = login_screen.ids.nc_field.text
        password = login_screen.ids.password_field.text

        if check_identity(nc=nc, password=password):
            self.root.current = 'home'

Main().run()
