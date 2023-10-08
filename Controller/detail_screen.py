import importlib

import View.DetailScreen.detail_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.DetailScreen.detail_screen)




class DetailScreenController:
    """
    The `DetailScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.detail_screen.DetailScreenModel
        self.view = View.DetailScreen.detail_screen.DetailScreenView(controller=self, model=self.model)

    def get_view(self) -> View.DetailScreen.detail_screen:
        return self.view