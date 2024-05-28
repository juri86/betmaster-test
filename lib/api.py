from requests import Session

from core.settings import Env


class RestApi:
    def __init__(self):
        self.env = Env()
        self.session = Session()
        self.response = None
        self.response_body = None

    def get_games_in_category(self, category: str):
        url = self.env.wiremock_host + f"/api/slots/{category}"
        headers = {"Content-Type": "application/json", "Host": "localhost"}
        self.response = self.session.get(url=url, headers=headers)
        if self.response.status_code == 200:
            try:
                self.response_body = self.response.json()
            except ValueError:
                self.response_body = {}
        return self.response, self.response_body
