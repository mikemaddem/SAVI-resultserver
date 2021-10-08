from requests import get, post
from urllib.parse import urljoin

from requests.api import request

from .config import BALLOTSERVER_URL


def post_to_ballotserver(endpoint: str, data: dict) -> dict:
    """
    Make a POST request to a ballotserver endpoint and return the requested JSON data.

    Args:
        endpoint: endpoint to request on the ballotserver
        data: JSON blob to send to ballotserver
    Returns:
        JSON returned by ballotserver
    Raises:
        AssertionError if response is not an OK response
    """
    url = urljoin(BALLOTSERVER_URL, endpoint)
    request = post(url, json=data)
    assert request.ok
    response_json = request.json()
    return response_json


def get_from_ballotserver(endpoint: str) -> dict:
    """
    Make a GET request to a ballotserver endpoint and return the requested JSON data.

    Args:
        endpoint: endpoint to request on the ballotserver
    Returns:
        JSON returned by ballotserver
    Raises:
        AssertionError if response is not an OK response
    """
    url = urljoin(BALLOTSERVER_URL, endpoint)
    request = get(url)
    assert request.ok
    response_json = request.json()
    return response_json


def challenge_ballot(verification_code: str) -> dict:
    """
    Challenge the ballot with the provided verification code

    Args:
        verification_code: voter ballot verification code
    Returns:
        Challenged ballot information received from ballotserver challenge endpoign
    """
    data = {"verification_code": verification_code}
    challenged_ballot = post_to_ballotserver("/ballot/challenge", data)
    return challenged_ballot


def get_election_results() -> dict:
    """
    Get the results of the election from the ballotserver

    Returns:
        JSON data received from querying the ballotserver results endpoint
    """
    return get_from_ballotserver("/election/result")    
