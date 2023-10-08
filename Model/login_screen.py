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

    def check_email_or_phone_no(self, data, instance, instance_name=None):

        if instance_name == 'pswd':
            if data == '':
                instance.text = "Password can't be Empty"
            elif len(data) <= 7:
                instance.text = 'Enter Correct Password'
            else:
                instance.text = ''
        else:
            import re

            phone_regex = r'^\+?\d{1,3}[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}$'
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            def validate_phone_number(data):
                if re.match(phone_regex, data):
                    return True
                elif re.match(email_regex, data):
                    return True
                return False
            instance.text = 'Enter Email or Phone no'
