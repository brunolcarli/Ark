import requests
from core.queries import query_capsules, query_capsule


URL = 'https://api.spacex.land/graphql/'


def get_capsules():
    """
    Requests capsules data from API.
    """
    response = requests.post(URL, json={'query': query_capsules()})

    return response.json()


def get_capsule(id):
    """
    Requests single capsule data from API.
    """
    response = requests.post(URL, json={'query': query_capsule(id)})

    return response.json()
