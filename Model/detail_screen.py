from Model.base_model import BaseScreenModel


class DetailScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.detail_screen.DetailScreen.DetailScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.data = {
            'images':[
                'assets/images/img/WA00031.jpg',
                'assets/images/img/WA00032.jpg',
                'assets/images/img/WA00033.jpg',
            ]
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("detail screen")

