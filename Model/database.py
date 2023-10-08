from __future__ import annotations

import socket
import os
print(os.getcwd())

import requests
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, storage, auth


def get_connect(func, host="8.8.8.8", port=53, timeout=3):
    """Checks for an active Internet connection."""

    def wrapped(*args):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port)
            )
            return func(*args)
        except Exception as e:
            print(e)
            return False

    return wrapped


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    name = "Firebase"

    def __init__(self):
        self.DATABASE_URL = "https://boutique-eab4b-default-rtdb.firebaseio.com/"
        # Address for users collections.
        self.USER_DATA = "Userdata"
        self.STORAGE_URL = "gs://boutique-eab4b.appspot.com"
        # RealTime Database attribute.
        self.real_time_firebase = firebase.FirebaseApplication(
            self.DATABASE_URL, None
        )
        cred = credentials.Certificate("boutique-eab4b-firebase-adminsdk-ycc6c-2142a02803.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'gs://boutique-eab4b.appspot.com'
        })

        self.storage_client = storage.bucket()

    @get_connect
    def get_data_from_collection(self, name_collection: str) -> dict | bool:
        """Returns data of the selected collection from the database."""

        try:
            data = self.real_time_firebase.get(
                self.DATABASE_URL, name_collection
            )
        except requests.exceptions.ConnectionError as e:
            print(e)
            return False
        print('Returned data: ', data)
        return data


    @get_connect
    def register_user(self, email, pwd):

        try:
            data = auth.create_user(
                email=email, password=pwd
            )
        except requests.exceptions.ConnectionError as e:
            return False

        print('Returned data: ', data)
        return data
    
    @get_connect
    def authenticate_user(self, email, pwd):
        self.db = firebase.FirebaseAuthentication

        try:
            data = auth.get_user_by_email(
                            email
                        )
        except requests.exceptions.ConnectionError as e:
            print(e)
            return False
        print('Returned data: ', data)
        return data

    @get_connect
    def add_product(self):
        data_set = {
            'products':{
                        'name': 'Falmara',
                        'price': '350000',
                        'sale_price': '34000',
                        'image': 'assets/images/img/WA00031.jpg',
                        'product': 'None',
                        # 'father': self,
                        'rating': '3.5',
                        'absolute_url': 'None',
                        'callback_func': 'None',
                        'is_liked': 'true',
                        }
            }
        try:
            data = self.real_time_firebase.patch(
                self.DATABASE_URL, data_set 
            )
        except requests.exceptions.ConnectionError as e:
            print(e)
            return False
        print('Returned data: ', data)
        return data
    
    def get_file(self):
        pass
# db = DataBase()
# user = db.authenticate_user('abdul211@mail.com','da22324')
# # print(user.phone_number)
# print(db.get_data_from_collection('products'))
# print(db.register_user('abdul211@mail.com','a1asda22324'))

# user = DataBase().authenticate_user('abdul211@mail.com','a1asd2324')
# print(user.get_user())

# print(db.add_product())