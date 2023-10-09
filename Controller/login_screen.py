import importlib

import View.LoginScreen.login_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)




class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> View.LoginScreen.login_screen:
        return self.view

    def get_request(self):
        email = self.view.mobile_view.ids.username.text
        pwd = self.view.mobile_view.ids.password.text
        if self.model.authenticate(email, pwd):
            self.view.app.add_screen("email verification screen", first=True)
        else:
            print('Error authenticating')
    
    def authenticate(self):
        from kivymd.toast import toast
        pwd = self.view.mobile_view.ids.password.text
        email = self.view.mobile_view.ids.username.text
        succ = False
        for user in self.view.app.reg_users:
            if user['pwd'] == pwd and user['email'] == email: 
                toast('Login Successfully')
                self.view.app.add_screen('home screen')
                succ = True
                self.view.app.authenticated=True
                self.view.app.login_details = {
                    'email': email,
                    'mobile': user['mobile'] 
                } 
                break
            # else: 
        if not succ:
            toast('Wrong Email or Password')

    
    def check_email_or_phone_no(self, data, instance, instance_name=None):

        if instance_name == 'pswd':
            if data == '':
                instance.text = "Password can't be Empty"
                self.view.mobile_view.ids.login_btn.disabled = True
            elif len(data) <= 7:
                instance.text = 'Enter at least 8 characters'
                self.view.mobile_view.ids.login_btn.disabled = True
            else:
                self.view.mobile_view.ids.login_btn.disabled = False
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