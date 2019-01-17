import requests

url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)

my_json = response.json()

my_list = []

for photo in my_json:
	my_list.append(photo['url'])

print(len(my_list))

print(len(set(my_list)))