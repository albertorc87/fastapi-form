import requests

url = 'http://127.0.0.1:8000/create_user'

"""
Para enviar archivos hay que añadir esta cabecera
pero al enviar el parámetro files al realizar la petición
ya nos añade automáticamente la cabecera por lo que no sería necesario añadirla
de todas formas os dejo por aquí como sería
"""
# headers = {
#     'Content-type': 'multipart/form-data'
# }

params = {
    'username': 'requestalber',
    'password': 'admin123',
}

filename = 'fastapi.jpg'
route_file = f'./tmp/{filename}'

files = {
    'photo': (filename, open(route_file, 'rb'), 'image/jpeg')
}

r = requests.post(url, data=params, files=files)

print(f'Status http: {r.status_code}')
print(f'Response: {r.json()}')