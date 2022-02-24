import requests

id = input("Which employee id do you want to get? ")
response = requests.get(f"http://localhost:5000/employees/{id}")
print(response.json())
print(response.status_code)