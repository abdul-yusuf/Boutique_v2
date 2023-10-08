import importlib
from kivymd.uix.pickers import MDDatePicker
from kivy.animation import Animation
import View.ProfileScreen.profile_screen
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ProfileScreen.profile_screen)




class ProfileScreenController:
    """
    The `ProfileScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.profile_screen.ProfileScreenModel
        self.view = View.ProfileScreen.profile_screen.ProfileScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ProfileScreen.profile_screen:
        return self.view

    def editing_mode(self, *args, **kwargs):
        print(args, kwargs)
        if kwargs['edit']==True:
            for x in range(4):
                x+=1
                input = f'self.view.ids.field{x}.disabled=False' 
                # inpu= False
                exec(input)
            Animation(
                # md_bg_color='#e9dff7',
                size_hint_x=.55,
                pos_hint={'center_x':.7},
                d=.5/1,
                # text='Save'
            ).start(self.view.ids.checkout_btn)
            self.view.ids.checkout_btn.text = 'Save'
            self.view.ids.checkout_btn.md_bg_color = get_color_from_hex(colors['Green']['600'])
            Animation(
                pos_hint={'center_x':.25},
                d=.6/1
            ).start(self.view.ids.cancel_btn)

        else:
            for x in range(4):
                x+=1
                input = f'self.view.ids.field{x}.disabled=True' 
                # inpu= False
                exec(input)
            Animation(
                # md_bg_color='#e9dff7',
                size_hint_x=.9,
                pos_hint={'center_x':.56},
                d=.5/1,
                # text='Save'
            ).start(self.view.ids.checkout_btn)
            self.view.ids.checkout_btn.text = 'Edit Details'
            self.view.ids.checkout_btn.md_bg_color = self.view.app.theme_cls.primary_color
            # print(dir(self.view.app.theme_cls))
            Animation(
                pos_hint={'center_x':-1.25},
                d=.6/1
            ).start(self.view.ids.cancel_btn)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save,on_cancel=self.cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.view.ids.field4.text = str(value)


    def cancel(self, instance, value):
        pass

    # def update_scroll(self,*args):
        # perm = args[1]
        # print(perm)
        # if perm>=.94:
        #     Animation(
        #         scroll_y=1 if perm>=.97 else 0,
        #         d=0.6/1
        #         ).start(self.view.mobile_view.ids.home_refresh_layout)
        # elif perm<.99:
        #     Animation(
        #         scroll_y=0 if perm<=.98 else 1,
        #         d=0.6/1
        #         ).start(self.view.mobile_view.ids.home_refresh_layout)
