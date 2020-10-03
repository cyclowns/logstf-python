import aiohttp
import requests

class LogsTF:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_data(self, log_id):
        """Returns object LogData for a given log ID"""
        j = requests.get(f'https://logs.tf/json/{log_id}')

    def search(self, title=None, map=None, uploader=None,
                     players=[], limit=1000, offset=0):
        """Returns list of log IDs that match the given parameters,
        up to the limit and starting at the offset"""
        pass

    def upload(self, title=None, map=None,
                     log=None, uploader=None, updatelog=None):
        pass
