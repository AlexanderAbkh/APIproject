import requests

class BaseApi:
    def __init__(self, session):
        self.session = session
        self.request = requests

    def get_wrapper(self):
        pass

