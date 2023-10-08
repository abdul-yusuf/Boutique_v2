from Model.base_model import BaseScreenModel
import random

class SearchScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.search_screen.SearchScreen.SearchScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

        self.value = [
        ]
        liked = []
        for x in range(20):
            liked.append(random.randint(1,20))
        for x in range(50):
            if x in liked:
                is_liked=True
                sale_price = ''
            else:
                is_liked=False
                sale_price = str(random.randint(1100,250000))
            self.value.append(
            {
            'name': 'Chicken Wings Wings',
            'price': f'{random.randint(2400,350000)}',
            'sale_price': sale_price,
            'image': f'assets/images/cate-{random.randint(5,13)}.jpg',
            'product': 'None',
            # 'father': self,
            'rating': '3.5',
            'absolute_url': 'None',
            'callback_func': 'None',
            'is_liked': is_liked,
            }
        )

        self.data = self.value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("search screen")