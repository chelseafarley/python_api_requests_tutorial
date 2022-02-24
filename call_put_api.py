import requests

id = input("Which employee id would you like to be updated? ")
name = input("What would you like your employee's name to be changed to? ")
employee = { "name": name }
headers = {"Content-type": "application/json"}
response = requests.put(f"http://localhost:5000/employees/{id}", json=employee, headers=headers)
print(response.json())
print(response.status_code)