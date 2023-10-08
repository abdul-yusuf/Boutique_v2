from kivymd.uix.textfield import MDTextField
from kivy.utils import platform
from kivy.lang import Builder
from Components import path

Builder.load_file(str(path / "gentextinput" / "gentextinput.kv"))

class GenTextField(MDTextField):
    def on_focus(self, *args):
        if platform=='android':
            from android.runnable import run_on_ui_thread
            # print(args)

            @run_on_ui_thread
            def fix():
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)
            if not args[1]:
                fix()

