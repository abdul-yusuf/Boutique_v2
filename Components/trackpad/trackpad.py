from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, DictProperty, ListProperty, ColorProperty

# from Components import path

# Builder.load_file(str(path / "trackpad" / "trackpad.kv"))




class CourierBox(MDBoxLayout):
    phone_no = StringProperty()
    rating = StringProperty()

class TrackPad(MDRelativeLayout):
    seprator_height = StringProperty()
    color = ColorProperty()

from kivymd.uix.screen import MDScreen

class Home(MDScreen):
            # Builder.load_file('button.kv')
    pass



if __name__ == "__main__":
    from kivymd.tools.hotreload.app import MDApp
    from kivy.lang.builder import Builder
    from kivy.clock import Clock
    from kivymd.uix.screenmanager import MDScreenManager
    from .button import button
    class Test(MDApp):
        KV_FILES = ['.\\imports.kv', '.\\Components\\button\\button.kv', '.\\Components\\trackpad\\trackpad.kv']
        # KV_DIRS = ['.\\']
        # root = None

        def build_app(self):

            self.theme_cls.primary_palette = "Brown"
            self.theme_cls.primary_hue = "A700"
            self.theme_cls.material_style = "M3"
            # Builder.load_file('button.kv')
            self.sm = MDScreenManager()
            view = Home()
            view.manager_screen = self.sm
            self.sm.add_widget(view)

            return self.sm
    Test().run()