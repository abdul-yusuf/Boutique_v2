from View.base_screen import BaseScreenView
from kivy.properties import StringProperty, ListProperty 

class CartScreenView(BaseScreenView):
    total = StringProperty('___.__')
    items_price = StringProperty('___.__')
    items_qty = StringProperty()
    shipping_fee = StringProperty('Free')
    order_id = StringProperty('********')
    

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
    def testing(self) -> None:
        print('cart screen testing new model modifiers method')

    def on_pre_enter(self, *args, **kwargs):
        items_list = self.app.cart_items
        self.items_qty = str(len(items_list))
        price = 0
        for i in items_list:
            price += int(i['price'])
        self.items_price = str(price)
        self.total = str(price)