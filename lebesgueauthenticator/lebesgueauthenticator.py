from jupyterhub.auth import Authenticator
from tornado import gen
import requests


class LebesgueAuthenticator(Authenticator):
    """JupyterHub Authenticator Based on Lebesgue"""

    def __init__(self, **kwargs):
        super(LebesgueAuthenticator, self).__init__(**kwargs)

    @staticmethod
    def _verify_password(username, password):
        try:
            data = requests.post(
                'https://lebesgue.dp.tech/account/login', json={"username": username, "password": password})
            data = data.json()
            if not data:
                return False

            if data.get('code') == '0000':
                return True

            return False
        except Exception as e:
            return False

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        passwd = data['password']

        if self._verify_password(username, passwd):
            return data['username']
        else:
            return None
