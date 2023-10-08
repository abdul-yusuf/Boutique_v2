from Model.base_model import BaseScreenModel


class ScanScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.scan_screen.ScanScreen.ScanScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("scan screen")