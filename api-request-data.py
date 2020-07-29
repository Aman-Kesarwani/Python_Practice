import requests
import config_key

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config_key.api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)

result = response.json()

print(result)

businesses = result['businesses']
print("Business List", businesses)

print(type(businesses))
for item in businesses:
    print("Company Name: ", item['name'])

names = [business['name']
         for business in businesses if business["rating"] > 4.5]
print(names)
