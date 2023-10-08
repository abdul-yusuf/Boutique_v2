from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.HomeScreen.components import (
    HomeMobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView
from kivy.properties import ListProperty


class HomeScreenView(MDResponsiveLayout, BaseScreenView):
    _data = ListProperty()
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = HomeMobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()
        # print(self.model.data)
        # print(self.mobile_view.name)
        for x in self.model._data:
            x['father'] = self
        self.mobile_view.ids.home_tile.data = self.model.data
        self.mobile_view.ids.home_tile.bind(scroll_y=self.controller.update_scroll)
        # print(self.ids.home_refresh_layout.ids)
        # print(self.mobile_view.ids)



    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print('model is changed home')
    
    def testing(self) -> None:
        print('home screen testing new model modifiers method')
