from web3 import Web3, HTTPProvider
import requests

# Set up the authorization token
# auth_token = "f566838dee114a483bde06cef6a2705b12b1291eedb0b2308a8f50ce9b72a396"

# # Define a custom HTTPProvider class that adds the authorization header to each request
# class AuthHTTPProvider(HTTPProvider):
#     def make_request(self, method, params):
#         headers = {'Authorization': f'Bearer {auth_token}'}
#         response = requests.post(self.endpoint_uri, json={'jsonrpc': '2.0', 'method': method, 'params': params}, headers=headers)
#         return response.json()

# # Create a new instance of the AuthHTTPProvider class
# provider = AuthHTTPProvider(endpoint_uri=f"http://192.168.0.128:9090")

# # Create a new Web3 instance using the custom provider
# w3 = Web3(provider)
# print(w3.isConnected())


w3 = Web3(Web3.HTTPProvider(
            f"http://192.168.0.128:9090"))
print(f"Connection: {w3.isConnected()}")
