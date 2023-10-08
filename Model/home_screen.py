from Model.base_model import BaseScreenModel
import random

class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        nevaons
        self.value = []
        liked = []
        for x in range(20):
            liked.append(random.randint(1,20))
        for x in range(20):
            if x in liked:
                is_liked=True
                sale_price = ''
            else:
                is_liked=False
                sale_price = str(random.randint(1100,250000))
            self.value.append(
            {
            'name': 'Falmara',
            'price': f'{random.randint(2400,350000)}',
            'sale_price': sale_price,
            'image': f'assets/images/img/WA0003{random.randint(1,9)}.jpg',
            'product': 'None',
            'father': self,
            'rating': '3.5',
            'absolute_url': 'None',
            'callback_func': 'None',
            'is_liked': is_liked,
            }
        )

        self.data = self.value
        self.notify_observers("home screen")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("home screen")

    def refresh_callback(self, data):
        print('refresh callback')

    def add_item_to_cart(self, *args, **kwargs):
        self.notify_observers('home screen', 'testing')