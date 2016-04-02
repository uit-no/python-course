import requests

baseurl = 'https://swapi.co/api/{type}/{n}'

def iter_people():
    for n in range(1, 10):
        response = requests.get(baseurl.format(type='people', n=n))
        yield response.json()
        
        if response.status_code == 404:
            return

for p in iter_people():
    print(p['name'])
