import configparser

class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("configurations/config.ini")

    def get_url(self):
        return self.config.get("BBC", "BASE_URL")

    def get_username(self):
        return self.config.get("BBC","USERNAME")

    def get_password(self):
        return self.config.get("BBC","PASSWORD")
