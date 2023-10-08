from Model.base_model import BaseScreenModel


class OrdersScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.orders_screen.OrdersScreen.OrdersScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None 
        self._data_in_transit = []
        self._data_complete = []
        self.data = [
            {
                'name': 'Chicken Wings',
                'ordered_date': 'None',
                'order_place': 'None',
                'being_delivered': 'None',
                'order_confirmed': 'None',
                'ready_for_delivery': 'None',
                'being_delivered': 'None',
                'delivered': 'None',
                'authorization': 'None',
                'status': 'None',
                'ref_code': 'None',
                'is_payed': 'False',
            },
            {
                'name': 'Chicken Wings',
                'ordered_date': 'None',
                'order_place': 'None',
                'being_delivered': 'None',
                'order_confirmed': 'None',
                'ready_for_delivery': 'None',
                'being_delivered': 'None',
                'delivered': 'None',
                'authorization': 'None',
                'status': 'in_transit',
                'ref_code': 'None',
                'is_payed': 'True',
            },
            {
                'name': 'Chicken Wings',
                'ordered_date': 'None',
                'order_place': 'None',
                'being_delivered': 'None',
                'order_confirmed': 'None',
                'ready_for_delivery': 'None',
                'being_delivered': 'None',
                'delivered': 'None',
                'authorization': 'None',
                'status': 'in_transit',
                'ref_code': 'None',
                'is_payed': 'False',
            },
            {
                'name': 'Chicken Wings',
                'ordered_date': 'None',
                'order_place': 'None',
                'being_delivered': 'None',
                'order_confirmed': 'None',
                'ready_for_delivery': 'None',
                'being_delivered': 'None',
                'delivered': 'None',
                'authorization': 'None',
                'status': 'complete',
                'ref_code': 'None',
                'is_payed': 'True',
            }
        ]

        # print(self.data, self._data_in_transit)
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        for orders in self._data:
            if orders['status'] == 'in_transit':
                self._data_in_transit.append(orders)
            if orders['status'] == 'complete':
                self._data_complete.append(orders)

        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("orders screen")
