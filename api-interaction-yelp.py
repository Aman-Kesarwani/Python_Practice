import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "XSCSZRe5lWdnqBlnK3ekEntbfC6JsQ3rYjaHAdBk9JzfGRUzEQem_qPtKU4VCDHgn0FqyLk-Co6qPfpeaYL8JlW6FMURVv0Z3JZWY6gtJJ650bjPaa8gosZbMGcdX3Yx"
headers = {
    "Authorization": "Bearer " + api_key
}

#amank2408@gmail.com - yelp.com

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
