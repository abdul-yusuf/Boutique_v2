from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCardSwipe
from kivy.animation import Animation
from kivy.uix.recycleview.views import RecycleKVIDsDataViewBehavior
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, DictProperty, ListProperty, ColorProperty
from kivy.lang.builder import Builder
from kivy.factory import Factory
from Components import path
# from kivymd.app import MDApp

Builder.load_file(str(path / "button" / "button.kv"))

class BadgeBtnIcon(ButtonBehavior, MDFloatLayout):
    icon = StringProperty()
    badge_icon = StringProperty()

    def on_press(self):
        pass
        print(self.badge_icon)

class ImageBtn(ButtonBehavior, MDFloatLayout):
    source = StringProperty('boy.png')
    title = StringProperty()

    def on_press(self):
        pass
        print(self.title)

class BtnIcon(ButtonBehavior, MDFloatLayout):
    icon = StringProperty('menu')
    title = StringProperty('')

    def on_press(self):
        pass
        print(self.title)

class Tile(RecycleKVIDsDataViewBehavior, MDCard):
    name = StringProperty()
    price = StringProperty()
    sale_price = StringProperty()
    image = StringProperty()
    product = ObjectProperty()
    father = ObjectProperty()
    rating = StringProperty()
    absolute_url = StringProperty()
    callback_func = None
    # _is_liked = BooleanProperty(defaultvalue=False)
    is_liked = BooleanProperty()
    index = 0

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.ids.percentage_badge.clear_widgets()
        
        try:
            if data['is_liked']:
                self.ids.like_btn.icon = 'heart'
            else:
                self.ids.like_btn.icon = 'heart-outline'
        except KeyError as e:
            print(e)
        super(Tile, self).refresh_view_attrs(rv, index, data)

    def store_btn_state(self, parent):
        # print(parent)
        if self.ids.like_btn.icon == 'heart-outline':
            self.is_liked = False
        else: 
            self.is_liked = True
        parent.data[self.index]['is_liked'] = self.is_liked


    # def on_is_liked(self, *args):
    #     self._is_liked = args[1]
    
    def on_sale_price(self, *args):
        if args[1] != '':
            badge = Factory.Badge()
            badge.value = '20'
            self.ids.price_label.strikethrough = True
            self.ids.percentage_badge.add_widget(badge)
        else:
            # self.ids.percentage_badge.clear_widgets()
            # print(dir(self.ids.percentage_badge))
            self.ids.price_label.strikethrough = False
            # print(dir(self.ids.sale_price_label.text))

    def on_release(self):
        # app = MDApp.get_running_app()
        self.father.app.details_page_data = {
                            'name': self.name,
                            'price': self.price,
                            'sale_price': self.sale_price,
                            'source': self.image,
                            'unit': 'each',
                            # 'product': 'None',
                            # 'father': self,
                        }
        self.father.app.add_screen('detail screen')

    def add_2_cart_btn(self):
        self.father.model.add_item_to_cart(
                        {
                            'name': self.name,
                            'price': self.price,
                            'sale_price': self.sale_price,
                            'source': self.image,
                            'unit': 'each',
                            # 'product': 'None',
                            # 'father': self,
                        },
                        view=self.father
                    )

class CartTile(RecycleKVIDsDataViewBehavior, MDCardSwipe):
    quantity = StringProperty('1')
    price = StringProperty('12000')
    name = StringProperty('Chicken')
    unit = StringProperty('KG')
    source = StringProperty('')
    def show_trash_animate(self, widget):
        Animation(
                x=-50,
                t='out_quad',
                d=0.02/1,
                ).start(self.ids.front_box)
        self.animate_back()
    def animate_back(self):
        Animation(
                x=0,   
                t='in_quad',
                d=2.5/1,
                ).start(self.ids.front_box)



class QtyBox(MDBoxLayout):
    qty_value = StringProperty('10')
    unit = StringProperty('crate')

class OrderTile(RecycleKVIDsDataViewBehavior, MDBoxLayout):
    """
        ordered_date: None
        order_place: None
        being_delivered: None
        order_confirmed: None
        ready_for_delivery: None
        being_delivered: None
        delivered: None
        authorization: None
    """
    ref_code = StringProperty()
    is_payed = BooleanProperty()
    # products = ListProperty()
    # data = DictProperty()
    def on_is_payed(self, inst,value):
        if value=='True':
            self.ids.payment_chip.text = 'Paid'
            self.ids.payment_chip.md_bg_color = '#66bb6a'
        else:
            self.ids.payment_chip.text = 'Not Paid'
            self.ids.payment_chip.md_bg_color = '#ef5350'

class RatingBox(MDBoxLayout):
    pass

class CourierBox(MDBoxLayout):
    phone_no = StringProperty()
    rating = StringProperty()

class TrackPad(MDRelativeLayout):
    seprator_height = StringProperty()
    color = ColorProperty()

class CarouselSlide(MDRelativeLayout):
    data = ListProperty()
    radius = ListProperty([10,10,10,10])
    def on_data(self, inst, value:list):
        """
        arg:
            value: (image_src,)
        """
        from kivymd.uix.fitimage import FitImage

        for image in value:
            # print(inst.ids)
            widget = FitImage(
                source=image,
                # adaptive_height=True,
                radius=self.radius
                )
            self.ids.head.add_widget(widget)


# from kivymd.uix.screen import MDScreen

# class Home(MDScreen):
#             # Builder.load_file('button.kv')
#     pass



# if __name__ == "__main__":
#     from kivymd.tools.hotreload.app import MDApp
#     from kivy.lang.builder import Builder
#     from kivy.clock import Clock
#     from kivymd.uix.screenmanager import MDScreenManager

#     class Test(MDApp):
#         KV_FILES = ['.\\imports.kv', '.\\Components\\button\\button.kv']
#         # KV_DIRS = ['.\\']
#         # root = None
#         def build_app(self):

#             self.theme_cls.primary_palette = "Brown"
#             self.theme_cls.primary_hue = "A700"
#             self.theme_cls.material_style = "M3"
#             # Builder.load_file('button.kv')
#             self.sm = MDScreenManager()
#             view = Home()
#             view.manager_screen = self.sm
#             self.sm.add_widget(view)
#             print(self.widget_inst())            
#             # self.sm.ids.first_head.head.data = self.widget_inst()
#             return self.sm

#         def widget_inst(self) -> list:
#             # from kivymd.uix.fitimage import FitImage
#             data = [
#                 'cate-12.jpg',
#                 'cate-6.jpg',
#                 'cate-12.jpg',
#                 'cate-6.jpg',
#                 'cate-6.jpg',
#             ]
#             return data

#     Test().run()