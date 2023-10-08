from kivy import Logger
from json import dumps
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
class Api_request:
    def __init__(self, url=None, auth=None):
        self.app = MDApp.get_running_app()
        self.base_url = url
        self.user_auth = auth

    @property
    def is_authenticated(self):
        return self.app.is_authenticated

    def request(self, *args, **kwargs):
        """
        Args:
            headers (kv_class): headers needed for request
        Kwargs:
            instance (_type_): instance of trigger
        """

        view_class = kwargs.get('instance')
        url = self.base_url+kwargs.get('url')
        req = UrlRequest(
            url,
            on_success=view_class.model.notify_observers(view_class.name)
        )

    def auth_request(self, headers=None, *args, **kwargs):
        """
        Args:
            headers (kv_class): headers needed for request
        Kwargs:
            instance (_type_): instance of trigger
        """
        instance = kwargs.get('instance')
        url = self.base_url+kwargs.get('url')
        method = self.view.app.request_parm.method('user_detail')['GET']
        req = UrlRequest(
                        url,
                        on_success=instance,
                        method=method,
                        on_error=self.got_error,
                        req_headers=headers,
                        on_failure=self.got_failure,
                        on_redirect=self.got_redirect
                        )

    def got_error(self, req, result):
        Logger.critical("---got_error---")

    def got_failure(self, req, result):
        Logger.critical("---got_failure---")

    def got_redirect(self, req, result):
        Logger.critical("---got_redirect---")


