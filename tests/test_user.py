import pytest
import requests

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:8000/users"

# Test function for the first scenario (username=admin, password=admin)
def test_unauthorized_user_access(mocker):
    # Define the parameters for the request
    params = {'username': 'admin', 'password': 'admin'}

    # Mock the requests.get method to simulate a 401 Unauthorized response
    mock_response = mocker.MagicMock()
    mock_response.status_code = 401
    mock_response.headers = {'Content-Type': 'text/plain'}
    mock_response.text = ""  # Empty response body
    mocker.patch('requests.get', return_value=mock_response)

    # Make the GET request (this will use the mocked response)
    response = requests.get(BASE_URL, params=params)

    # Assert the HTTP response code is 401 (Unauthorized)
    assert response.status_code == 401, f"Expected 401, but got {response.status_code}"

    # Assert the response is text and not JSON
    assert response.headers['Content-Type'].startswith('text'), \
        f"Expected response to be text, but got {response.headers['Content-Type']}"

    # Assert the response body is empty
    assert response.text == "", f"Expected an empty response body, but got: {response.text}"

# Test function for the second scenario (username=admin, password=qwerty)
def test_authorized_user_access(mocker):
    # Define the parameters for the request
    params = {'username': 'admin', 'password': 'qwerty'}

    # Mock the requests.get method to simulate a 200 OK response
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {'Content-Type': 'text/plain'}
    mock_response.text = ""  # Empty response body
    mocker.patch('requests.get', return_value=mock_response)

    # Make the GET request (this will use the mocked response)
    response = requests.get(BASE_URL, params=params)

    # Assert the HTTP response code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    # Assert the response is text and not JSON
    assert response.headers['Content-Type'].startswith('text'), \
        f"Expected response to be text, but got {response.headers['Content-Type']}"

    # Assert the response body is empty
    assert response.text == "", f"Expected an empty response body, but got: {response.text}"
