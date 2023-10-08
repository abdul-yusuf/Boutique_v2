import importlib
from kivy.animation import Animation

import View.HomeScreen.home_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.HomeScreen.home_screen)




class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = View.HomeScreen.home_screen.HomeScreenView(controller=self, model=self.model)

    def get_view(self) -> View.HomeScreen.home_screen:
        return self.view

    def update_scroll(self,*args):
        perm = args[1]
        if perm>=.94:
            Animation(
                scroll_y=1 if perm>=.97 else 0,
                # scroll_y=perm*2.1,
                d=0.6/1
                ).start(self.view.mobile_view.ids.home_refresh_layout)
        elif perm<.93:
            Animation(
                # scroll_y=perm/1.1,
                scroll_y=0 if perm<=.98 else 1,
                d=0.6/1
                ).start(self.view.mobile_view.ids.home_refresh_layout)
