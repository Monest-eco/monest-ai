import requests
import json

class Request():
    def __init__(self):
        pass

    def get_request(self, url, params=None, headers=None, auth=None, data=None):
        response = requests.get(url, params=params, headers=headers, auth=auth, data=data)
        if response.ok:
            value = json.loads(response.text)
            return value
        else:
            return {}

    def post_request(self, url, params=None, headers=None, auth=None, data=None):
        response = requests.post(url, params=params, headers=headers, auth=auth, data=data)
        if response.ok:
            value = json.loads(response.text)
            return value
        else:
            return {}

    def put_request(self, url, params=None, headers=None, auth=None, data=None):
        response = requests.put(url, params=params, headers=headers, auth=auth, data=data)
        if response.ok:
            value = json.loads(response.text)
            return value
        else:
            return {}

    def patch_request(self, url, params=None, headers=None, auth=None, data=None):
        response = requests.patch(url, params=params, headers=headers, auth=auth, data=data)
        if response.ok:
            value = json.loads(response.text)
            return value
        else:
            return {}

    def delete_request(self, url, params=None, headers=None, auth=None, data=None):
        response = requests.delete(url, params=params, headers=headers, auth=auth, data=data)
        if response.ok:
            value = json.loads(response.text)
            return value
        else:
            return {}