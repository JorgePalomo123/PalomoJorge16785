import requests

#url = "https://jsonplaceholder.typicode.com/todos/1"
url = "https://dragonball-api.com/api/characters/38"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud exitosa')
else:
    print('Error en la solicitud' , response.text)

print("Dragon ball super:")
print("Numero de peleador",data["id"])
print("Nombre de peleador",data["name"])
print("Poder del peleador",data["ki"])
print("Genero del peleador",data["gender"])
