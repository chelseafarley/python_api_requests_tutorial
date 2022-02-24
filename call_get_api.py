import requests

response = requests.get("http://localhost:5000/employees")
print(response.json())
print(response.status_code)