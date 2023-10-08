#
# """
# Script for managing hot reloading of the project.
# For more details see the documentation page -
#
# https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/
#
# To run the application in hot boot mode, execute the command in the console:
# DEBUG=1 python main.py
# """
#
# import importlib
# import os
#
# from kivy import Config
#
# from PIL import ImageGrab
#
# # TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size
#
# # Change the values of the application window size as you need.
# Config.set("graphics", "height", resolution[1])
# Config.set("graphics", "width", "400")
#
# from kivy.core.window import Window
#
# # Place the application window on the right side of the computer screen.
# Window.top = 0
# Window.left = resolution[0] - Window.width
#
# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
#
#
# class EmroideryApp(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]
#
#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#
#         import View.screens
#
#         self.manager_screens = MDScreenManager()
#         Window.bind(on_key_down=self.on_keyboard_down)
#         importlib.reload(View.screens)
#         screens = View.screens.screens
#
#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)
#
#         return self.manager_screens
#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.
#
#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """
#
#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()
#
#
# EmroideryApp().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""


import importlib
import os

from kivy import Config



#800,400

# from kivymd.uix.transition import MDFadeSlideTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from View.screens import screens
from kivy.clock import Clock
from kivy.lang import Builder
from Utility.api_request import Api_request
from Components.factory import register_factory
from kivymd.toast import toast

# from Model.database import DataBase

register_factory()

class EmroideryApp(MDApp):
    cart_items = ListProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("imports.kv")
        # self.database = DataBase()

        # This is the screen manager that will contain all the screens of your
        # application.
        # self.manager_screens = MDScreenManager()
        self.database = Api_request()
        # self.theme_cls.theme_style = 'Dark' #'Light'
        self.root = MDScreenManager()
        self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.material_style= "M3"
        self.theme_cls.accent_palette= "Red"
        self._recent_screen = []
        spinner = Factory.MDSpinner(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        self.dialog.add_widget(spinner)
        self.add_screen("home screen", first=True)
        Window.bind(on_key_down=self.go_back)

        # for x in range(1):
        #     self.cart_items.append(
        #         {
        #         'name':'Falmara',
        #         'price': '1300',
        #         'quantity': f'{x+2}',
        #         'unit': 'pieces',
        #         'source': 'assets/images/img/WA00032.jpg'
        #         }
        #     )
    def add_item_to_cart(self, product):
        added = False
        for items in self.cart_items:
            if product['name'] in items.values():
                items['quantity'] = str(int(items['quantity'])+1)
                items['price'] = str(int(items['price_tag'])*int(items['quantity']))
                added = True
            # else:
        if not added:
            self.cart_items.append(
                    {
                        'name':product['name'],
                        'price': product['price'],
                        'price_tag': product['price'],
                        'quantity': '1',
                        'unit': product['unit'],
                        'source': product['source']
                    }
                )
        toast("Product Added")
        print(self.cart_items)

    def add_screen(self, name_screen, switch=True, first=False):
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not self.root.has_screen(name_screen):
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first=True), 1)
        elif switch:
            self.recent_screen = name_screen
            self.root.current = name_screen


    def load_screen(self, name_screen, switch, first):
        Builder.load_file(screens[name_screen]["kv"])
        model = screens[name_screen]["model"](self.database)
        controller = screens[name_screen]["controller"](model)

        view = controller.get_view()
        view.name = name_screen
        self.root.add_widget(view)
        if switch:
            self.recent_screen = name_screen
            self.root.current = name_screen
        if first:
            self.dialog.dismiss()

    @property
    def recent_screen(self):
        return self._recent_screen

    @recent_screen.setter
    def recent_screen(self, value):
        if len(self._recent_screen)==0:
            self._recent_screen.append('home screen')
            self._recent_screen.append(value)
        else:
            if value in self._recent_screen:
                self._recent_screen.remove(value)
                self._recent_screen.append(value)
            else:
                self._recent_screen.append(value)

    @recent_screen.deleter
    def recent_screen(self):
        if len(self._recent_screen)==0:
            if 'home screen' not in self._recent_screen:
                self._recent_screen.append('home screen')
            else:
                self.root.current = 'home screen'
        else:
            self._recent_screen.pop()
    def go_back(self, window, key, *args):
        if key == 27:
            print(self.recent_screen)
            if len(self.recent_screen) < 1:
                self.stop()
                return True     
            self.go_to_recent_screen()
            return True
        else:
            return False
    def go_to_recent_screen(self, *args):
        try:
            del self.recent_screen
            self.add_screen(self.recent_screen[-1])
            if len(self.recent_screen) == 1:
                print('press twice to exit App')
        except IndexError:
            print('App exiting')
    # def generate_application_screens(self) -> None:
    #     """
    #     Creating and adding screens to the screen manager.
    #     You should not change this cycle unnecessarily. He is self-sufficient.
    #
    #     If you need to add any screen, open the `View.screens.py` module and
    #     see how new screens are added according to the given application
    #     architecture.
    #     """
    #
    #     for i, name_screen in enumerate(screens.keys()):
    #         model = screens[name_screen]["model"]()
    #         controller = screens[name_screen]["controller"](model)
    #         view = controller.get_view()
    #         view.manager_screens = self.manager_screens
    #         view.name = name_screen
    #         self.manager_screens.add_widget(view)


EmroideryApp().run()
