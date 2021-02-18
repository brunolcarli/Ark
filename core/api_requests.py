import requests
from core.queries import (query_capsules, query_capsule, query_company,
                          query_histories, query_history, query_rockets, query_rocket)




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


def get_company():
    """
    Requests company (SpaceX) data from API.
    """
    response = requests.post(URL, json={'query': query_company()})

    return response.json()


def get_histories():
    """
    Requests histories data from API.
    """
    response = requests.post(URL, json={'query': query_histories()})

    return response.json()


def get_history(id):
    """
    Requests single history data from API.
    """
    response = requests.post(URL, json={'query': query_history(id)})

    return response.json()
def get_rockets():
    """
    request rockets information
    """
    response = requests.post(URL, json={'query': query_rockets()})
    return response.json()
def get_rocket(id):
    """
    request single rocket information
    """
    response = requests.post(URL, json={'query': query_rocket(id)})
    return response.json()