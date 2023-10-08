from View.base_screen import BaseScreenView
from kivy.clock import Clock


class EmailVerificationScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.app.add_screen("home screen", first=True)
        Clock.schedule_once(self.app.dialog.dismiss,1)
