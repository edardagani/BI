import requests

x = mycol.insert_one(mydict)
list_of_db = client.list_database_names()
print(list_of_db)


if "test-database" in list_of_db:
    print("The database exists.")


x = 0

while True:
    response = requests.get("https://api.fda.gov/animalandveterinary/event.json?limit=1000" + f'&skip={x}')
    x = x + 1000
    header = response.links.get("next")
    print(header)
    if header is None:
        break
    else:
        url = response.links["next"]["url"]
        reaction = response.json()
        results = (reaction['results'])
        print(results)




