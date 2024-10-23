import requests

url = 'http://127.0.0.1:8000/hello'  # Replace with your actual API URL

response = requests.get(url)

print(response.json())  # Print the response