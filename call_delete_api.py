import requests

id = input("Which employee id do you want to delete? ")
response = requests.delete(f"http://localhost:5000/employees/{id}")
print(response.json())
print(response.status_code)