import importlib

import View.SignupScreen.signup_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SignupScreen.signup_screen)
from kivymd.toast import toast




class SignupScreenController:
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.signup_screen.SignupScreenModel
        self.view = View.SignupScreen.signup_screen.SignupScreenView(controller=self, model=self.model)

    def get_view(self) -> View.SignupScreen.signup_screen:
        return self.view

    def server_request(self, *args):
        data = {
            'mobile': self.view.mobile_view.ids.phone_no.text,
            'email': self.view.mobile_view.ids.email.text,
            'pwd': self.view.mobile_view.ids.password.text
        }

        toast('user created succesfully')
        self.view.app.reg_users.append(data)
        self.view.app.add_screen('login screen')
    
    def check_email_or_phone_no(self, data, instance, instance_name=None):

        if instance_name == 'pswd':
            if data == '':
                instance.text = "Password can't be Empty"
                self.view.mobile_view.ids.signup_btn.disabled = True
            elif len(data) <= 7:
                instance.text = 'Enter at least 8 characters'
                self.view.mobile_view.ids.signup_btn.disabled = True
            else:
                self.view.mobile_view.ids.signup_btn.disabled = False
                instance.text = ''
        else:
            import re

            # phone_regex = r'^\+?\d{1,3}[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}$'
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            # def validate_phone_number(data):
                # if re.match(phone_regex, data):
                #     return True
                # el
            if re.match(email_regex, data):
                instance.text = ''
                # return True
                # return False
            else:
                instance.text = 'Enter Email address'