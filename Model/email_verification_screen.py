from Model.base_model import BaseScreenModel
from kivymd.app import MDApp

class EmailVerificationScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.email_verification_screen.EmailVerificationScreen.EmailVerificationScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.app = MDApp.get_running_app()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.app.dialog.open()
        self.notify_observers("email verification screen")

    def code_check(self, instance1, instance2, instance3, instance4):
        inst1 = instance1.text
        inst2 = instance2.text
        inst3 = instance3.text
        inst4 = instance4.text
        print(inst1.isdigit(), inst2.isdigit(), inst3.isdigit(), inst4.isdigit())
        if inst1.isdigit() and inst2.isdigit() and inst3.isdigit() and inst4.isdigit():
            print('pass')
            value = inst1+inst2+inst3+inst4
            self.data = value
            print(self.data)
        else:
            print('fail')
            inst1 = ''
            inst2 = ''
            inst3 = ''
            inst4 = ''

