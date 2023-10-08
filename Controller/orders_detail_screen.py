import importlib
import View.OrdersDetailScreen.orders_detail_screen

from kivy.factory import Factory
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.metrics import dp
from kivymd.uix.button import MDTextButton
from kivy.clock import Clock
# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.OrdersDetailScreen.orders_detail_screen)




class OrdersDetailScreenController:
    """
    The `OrdersDetailScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.orders_detail_screen.OrdersDetailScreenModel
        self.view = View.OrdersDetailScreen.orders_detail_screen.OrdersDetailScreenView(controller=self, model=self.model)
        Clock.schedule_once(self.check_btn,2)
        TrackPad_1 = Factory.TrackPad()
        TrackPad_2 = Factory.TrackPad()
        TrackPad_3 = Factory.TrackPad()
        TrackPad_4 = Factory.TrackPad()
        self.track_pad_parent = MDExpansionPanel(
                content = MDBoxLayout(
                    # TrackPad(
                    #     color=get_color_from_hex(colors['Green']['300']),
                    # ),
                    # TrackPad(
                    #     # text='Order Confirmed',
                    #     # secondary_text='It has been confirmed',
                    #     # tertiary_text = 'on 28-Dec-22',
                    #     # color=get_color_from_hex(colors['Green']['300']) if args[0]['order_confirmed']['read'] else self.app.theme_cls.primary_light,
                    # ),
                    # TrackPad(
                    #     text='Ready for Delivery',
                    #     secondary_text='Your order is ready for shipping',
                    #     tertiary_text = 'on 28-Dec-22',
                    #     color=get_color_from_hex(colors['Green']['300']) if args[0]['ready_for_delivery']['read'] else self.app.theme_cls.primary_light,
                    # ),
                    # # text: 'Out For Delivery'
                    # # secondary_text: 'Your order is out fro delivery'
                    # # tertiary_text: ''
                    # # color: get_color_from_hex(colors['Green']['300'])
                    # # seprator_height:0
                    # TrackPad(
                    #     text='Out For Delivery',
                    #     secondary_text='Your order is out for delivery',
                    #     tertiary_text = 'on 28-Dec-22',
                    #     color=get_color_from_hex(colors['Green']['300']) if args[0]['out_for_delivery']['read'] else self.app.theme_cls.primary_light,
                    #     ),
                    # TrackPad(
                    #     seprator_height = '0',
                    #     text='Delivered',
                    #     secondary_text='Your order is out for delivery',
                    #     tertiary_text = str(self.track_data),
                    #     color=get_color_from_hex(colors['Green']['300']) if args[0]['delivered']['read'] else self.app.theme_cls.primary_light,
                    #     ),
                    TrackPad_1,
                    TrackPad_2,
                    TrackPad_3,
                    TrackPad_4,
                    orientation= 'vertical',
                    adaptive_height = True,
                    padding = [dp(0),dp(20),0,0],
                    spacing = dp(10)
                ),
                panel_cls = MDExpansionPanelOneLine(text='Track Order')
            )

        self.compile()

    def get_view(self) -> View.OrdersDetailScreen.orders_detail_screen:
        return self.view

    def compile(self):
        # statment depends on data from server
        if True:
            courier_tile = Factory.CourierBox()
            Clock.schedule_once(lambda x='':self.view.ids.courier_parent_box.add_widget(courier_tile),1.5)
            Clock.schedule_once(lambda x='':self.view.ids.trackpad_box.add_widget(self.track_pad_parent),2)
        # statment depends on data of is_payed
        # or [completed order and not closed]
    def check_btn(self, *args):
        if True:
            btn = MDTextButton(
                    color=get_color_from_hex(colors['Green']['400']),
                    # color=get_color_from_hex(colors['Red']['600']),
                    text= 'Confirm Recieved',# or "Pay",
                    pos_hint={'top':.5},
                    on_release=lambda x='':self.view.app.add_screen('scan screen')
                    # on_release=lambda x=authorization:self.webview_create()
                )
            self.view.ids.payment_btn_box.add_widget(btn)
            # pass