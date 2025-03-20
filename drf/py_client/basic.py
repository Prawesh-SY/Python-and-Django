import requests

endpoint = 'http://localhost:8000/'

get_response = requests.get(endpoint)
print(get_response.text)    # print raw text response
print(get_response.status_code) # 

endpoint_api = "http://localhost:8000/api/"