# IGDB is a video game database operated by Twitch
# https://www.igdb.com/api

import requests
from os import environ
from json import JSONDecoder


# TODO: Implement Rate Limiting
# https://api-docs.igdb.com/#rate-limits
class IGDB:
    def __init__(self):
        self.base_url = 'https://api.igdb.com/v4'
        self.client_id = environ["TWITCH_CLIENT_ID"]

        # Initial OAuth Setup
        self.access_token = None
        self.client_secret = environ["TWITCH_CLIENT_SECRET"]
        self.oauth_form = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.oauth_url = 'https://id.twitch.tv/oauth2/token'
        self.token_expires_in = 0

    def search(self, game):
        try:
            search_url = f'{self.base_url}/search'
            data = f'search "{game}"; fields *;'
            res = requests.post(search_url, headers=self.headers(), data=data)

            # Convert into Dict since IGDB returns response as plain text
            return JSONDecoder().decode(res.text)
        except Exception as err:
            print(f"WARNING: Search request failed! {err=}, {type(err)=}")

            return {}

    def headers(self):
        # Check if OAuth token needs to be refreshed.
        one_hour = 3600
        if self.token_expires_in < one_hour:
            res = requests.post(self.oauth_url, data=self.oauth_form).json()

            self.token_expires_in = int(res['expires_in'])
            self.access_token = res["access_token"]

        return {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}'
        }