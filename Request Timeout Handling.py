import requests

def handle_request_timeout(api_url, timeout):
    try:
        response = requests.get(api_url, timeout=timeout)
        # Process the response as needed
        return response
    except requests.exceptions.Timeout:
        # Handle timeout error
        raise Exception("API request timed out")
    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        raise Exception(f"Error occurred during the API request: {str(e)}")
