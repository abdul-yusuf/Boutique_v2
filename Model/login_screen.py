from Model.base_model import BaseScreenModel


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
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
        self.notify_observers("login screen")

    def check_(self, data):
        """
        validates data
        """

        if isinstance(data, dict):
            print(data)
            self.notify_observers('login screen')
            self.notify_observers('home screen')

    def authenticate(self, email, pwd):
        print(email, pwd) 
