import urllib.request
import json

url = 'https://api.github.com/users/Jvribeirof/events'

with urllib.request.urlopen(url) as response:
    data = response.read()
    json_data = json.loads(data)

for action in json_data:
    print('Repositóry:', action['repo']['name'][11:])
    print('Type: ', action['type'])
    print('Last Modification: ', action['created_at'][:10])
    print('--------------------------------------------------')