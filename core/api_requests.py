import requests
from core.queries import Query

URL = 'https://api.spacex.land/graphql/'

class APIRequest:
    """
    Contains backend http request methods.
    """

    @staticmethod
    def get_capsules():
        """
        Requests capsules data from API.
        """
        response = requests.post(URL, json={'query': Query.query_capsules()})

        return response.json()

    @staticmethod
    def get_capsule(id):
        """
        Requests single capsule data from API.
        """
        response = requests.post(URL, json={'query': Query.query_capsule(id)})

        return response.json()

    @staticmethod
    def get_company():
        """
        Requests company (SpaceX) data from API.
        """
        response = requests.post(URL, json={'query': Query.query_company()})

        return response.json()

    @staticmethod
    def get_histories():
        """
        Requests histories data from API.
        """
        response = requests.post(URL, json={'query': Query.query_histories()})

        return response.json()

    @staticmethod
    def get_history(id):
        """
        Requests single history data from API.
        """
        response = requests.post(URL, json={'query': Query.query_history(id)})

        return response.json()

    @staticmethod
    def get_rockets():
        """
        request rockets information
        """
        response = requests.post(URL, json={'query': Query.query_rockets()})

        return response.json()

    @staticmethod
    def get_rocket(id):
        """
        request single rocket information
        """
        response = requests.post(URL, json={'query': Query.query_rocket(id)})

        return response.json()

    @staticmethod
    def get_missions():
        """
        Requests missions data from API
        """
        response = requests.post(URL, json={'query': Query.query_missions()})

        return response.json()

    @staticmethod
    def get_mission(id):
        """
        Requests a single mission data from API by ID
        """
        response = requests.post(URL, json={'query': Query.query_mission(id)})

        return response.json()
