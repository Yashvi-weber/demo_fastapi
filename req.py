import requests

#url = 'http://127.0.0.1:8000/hello'  # Replace with your actual API URL
quote = 'https://ankit5125.github.io/Json-API/quotes.json'

#response = requests.get(url)
response1 = requests.get(quote)

#print(response.json())  # Print the response
print(response1.json())