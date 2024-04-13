import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud exitosa')
    print('Datos:', data)
else:
    print('Error en la solicitud' , response.text)