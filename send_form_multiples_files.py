import requests

url = 'http://127.0.0.1:8000/upload_multiple_files'

files = [
    ('files', ('fastapi.jpg', open('./tmp/fastapi.jpg', 'rb'), 'image/jpeg')),
    ('files', ('fastapi2.jpg', open('./tmp/fastapi2.jpg', 'rb'), 'image/jpeg')),
]

r = requests.post(url, files=files)

print(f'Status http: {r.status_code}')
print(f'Response: {r.json()}')