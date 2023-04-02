from pymongo import MongoClient
import json

# open the config file
with open('Model/config.json') as f:
    config = json.load(f)


class Model:
    static_c = 0

    def __init__(self):
        try:
            self.client = MongoClient(
                config["model"]["connection_url"]
            )
            self.db = self.client.url_shortener
            self.urls = self.db.urls
            self.client.server_info()
        except:
            print("Not success")
        else:
            print("connected")

    def insert_one(self, url_details):
        if isinstance(url_details, dict):
            self.urls.insert_one(url_details)

    def Is_Available(self, url):
        data = None
        if isinstance(url, dict):
            data = self.urls.find_one(filter=url)
            return data
        return data

    def find(self, short_url):

        if isinstance(short_url, dict):
            return self.urls.find_one(filter=short_url)
        return 300
