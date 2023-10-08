# from kivymd.uix. import MD
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.uix.refreshlayout import MDScrollViewRefreshLayout
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.scrollview import ScrollView

from Components import path

Builder.load_file(str(path / "customscroll" / "customscroll.kv"))

class CustomScroll(MDScrollViewRefreshLayout, RecycleView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

class Tab(
    # ScrollView,
    MDFloatLayout,
    # MDBoxLayout,
    # MDRecycleView, 
    MDTabsBase
    ):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    pass
