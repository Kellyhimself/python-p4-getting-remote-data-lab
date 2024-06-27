# Import the requests and json libraries
import requests
import json

# Define a class to make GET requests
class GetRequester:
    # Initialize the class with a URL
    def __init__(self, url):
        self.url = url

    # Make a GET request and return the response body
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # Load the response body as JSON and return the data
    def load_json(self):
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data