import requests
x=0
for i in range(1,10246):
    response = requests.get("https://api.fda.gov/animalandveterinary/event.json?limit=100" + f'&skip={x}')
    print(response)
    print(response.json())
    x=x+100