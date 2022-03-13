import requests

header = {
    'Content-Type': 'application/json',
    'Application-Key': 'key from TU'
}

body = {"UserName" : "un","PassWord" : "pw"}

response = requests.post("https://restapi.tu.ac.th/api/v1/auth/Ad/verify", headers= header, json= body)

print(response.status_code)
print(response.json())
